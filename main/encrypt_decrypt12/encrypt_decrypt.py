import base64
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
import sys
from loguru import logger

try:
    key = "key1"
    iv = "my_username_pass"   # Must be 16 bytes
    salt = "salt"

    if not (key and iv and salt):
        raise Exception("Error while fetching details for key/iv/salt")
except Exception as e:
    logger.error(f"Error occurred. Details: {e}")
    sys.exit(0)

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[-1:])]

def get_private_key():
    Salt = salt.encode("utf-8")
    kdf = PBKDF2(key, Salt, 64, count=1000)
    return kdf[:32]  # AES-256 key

def encrypt(raw: str) -> str:
    raw = pad(raw).encode("utf-8")
    cipher = AES.new(get_private_key(), AES.MODE_CBC, iv.encode("utf-8"))
    return base64.b64encode(cipher.encrypt(raw)).decode("utf-8")

def decrypt(enc: str) -> str:
    cipher = AES.new(get_private_key(), AES.MODE_CBC, iv.encode("utf-8"))
    decrypted = cipher.decrypt(base64.b64decode(enc))
    return unpad(decrypted.decode("utf-8"))

# Test
ciphertext = encrypt("Sb@712306")
print("Encrypted:", ciphertext)

plaintext = decrypt(ciphertext)
print("Decrypted:", plaintext)
