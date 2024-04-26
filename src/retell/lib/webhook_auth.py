import re
import hmac
import time
import base64
import hashlib

from cryptography.exceptions import InvalidSignature  # type: ignore
from cryptography.hazmat.primitives import hashes  # type: ignore
from cryptography.hazmat.primitives.asymmetric import padding  # type: ignore
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key  # type: ignore

FIVE_MINUTES = 5 * 60 * 1000


def make_secure_webhooks(get_signer, get_verifier):  # type: ignore
    def sign(input_str, secret_or_private_key, timestamp=None):  # type: ignore
        if timestamp is None:
            timestamp = int(time.time() * 1000)
        signer = get_signer(secret_or_private_key)  # type: ignore
        return f"v={timestamp},d={signer(input_str + str(timestamp))}"  # type: ignore

    def verify(input_str, secret_or_public_key, signature, opts=None):  # type: ignore
        if opts is None:
            opts = {}
        match = re.search(r"v=(\d+),d=(.*)", signature)  # type: ignore
        if not match:
            return False
        poststamp = int(match.group(1))
        post_digest = match.group(2)
        timestamp = opts.get("timestamp", int(time.time() * 1000))  # type: ignore
        timeout = opts.get("timeout", FIVE_MINUTES)  # type: ignore
        difference = abs(timestamp - poststamp)  # type: ignore
        if difference > timeout:
            return False
        verifier = get_verifier(secret_or_public_key)  # type: ignore
        return verifier(input_str + str(poststamp), post_digest)  # type: ignore

    return {"sign": sign, "verify": verify}  # type: ignore


def symmetric_get_signer(secret):  # type: ignore
    def signer(input_str):  # type: ignore
        return hashlib.sha256(secret.encode() + input_str.encode()).hexdigest()  # type: ignore

    return signer  # type: ignore


def symmetric_get_verifier(secret):  # type: ignore
    def verifier(input_str, digest):  # type: ignore
        algo = hashlib.sha256
        hmac_instance = hmac.new(secret.encode(), digestmod=algo)  # type: ignore
        hmac_instance.update(input_str.encode())  # type: ignore
        return hmac_instance.hexdigest() == digest  # type: ignore

    return verifier  # type: ignore


def asymmetric_get_signer(private_key):  # type: ignore
    def signer(input_str):  # type: ignore
        private_key_obj = load_pem_private_key(private_key.encode(), password=None)  # type: ignore
        signature = private_key_obj.sign(  # type: ignore
            input_str.encode(),  # type: ignore
            padding.PSS(  # type: ignore
                mgf=padding.MGF1(hashes.SHA256()),  # type: ignore
                salt_length=padding.PSS.MAX_LENGTH,  # type: ignore
            ),
            hashes.SHA256(),  # type: ignore
        )
        return base64.b64encode(signature).decode()  # type: ignore

    return signer  # type: ignore


def asymmetric_get_verifier(public_key):  # type: ignore
    def verifier(input_str, digest):  # type: ignore
        public_key_obj = load_pem_public_key(public_key.encode())  # type: ignore
        try:
            public_key_obj.verify(  # type: ignore
                base64.b64decode(digest),  # type: ignore
                input_str.encode(),  # type: ignore
                padding.PSS(  # type: ignore
                    mgf=padding.MGF1(hashes.SHA256()),  # type: ignore
                    salt_length=padding.PSS.MAX_LENGTH,  # type: ignore
                ),
                hashes.SHA256(),  # type: ignore
            )
            return True
        except InvalidSignature:
            return False

    return verifier  # type: ignore


symmetric = make_secure_webhooks(symmetric_get_signer, symmetric_get_verifier)  # type: ignore


def verify(body, api_key, signature):  # type: ignore
    return symmetric["verify"](body, api_key, signature)  # type: ignore
