from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os
from cryptography.hazmat.backends import default_backend  # Import backend

class RSACipher:
    def __init__(self, key_size=2048):
        self.key_size = key_size
        self.private_key_file = "private_key.pem"
        self.public_key_file = "public_key.pem"

    def generate_keys(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=self.key_size
        )
        public_key = private_key.public_key()

        with open(self.private_key_file, "wb") as private_file:
            private_file.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )

        with open(self.public_key_file, "wb") as public_file:
            public_file.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )

    def load_keys(self):
        if not os.path.exists(self.private_key_file) or not os.path.exists(self.public_key_file):
            raise FileNotFoundError("Keys not found. Please generate keys first.")

        # Load private key
        with open(self.private_key_file, "rb") as private_file:
            private_key = serialization.load_pem_private_key(
                private_file.read(),
                password=None
            )

        # Load public key
        with open(self.public_key_file, "rb") as public_file:
            public_key = serialization.load_pem_public_key(
                public_file.read()
            )

        return private_key, public_key


    def encrypt(self, message, public_key):
        encrypted_message = public_key.encrypt(
            message.encode(),
            padding.PKCS1v15()
        )
        return encrypted_message

    def decrypt(self, ciphertext, private_key):
        decrypted_message = private_key.decrypt(
            ciphertext,
            padding.PKCS1v15()
        )
        return decrypted_message.decode()

    def sign(self, message, private_key):
        signature = private_key.sign(
            message.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return signature

    def verify(self, message, signature, public_key):
        try:
            public_key.verify(  # Đảm bảo đây là public_key
                signature,
                message.encode(),
                padding.PKCS1v15(),
                hashes.SHA256()
            )
            return True
        except Exception as e:
            print(f"Verification failed: {e}")
            return False