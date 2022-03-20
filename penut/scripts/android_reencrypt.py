from Crypto.Cipher import PKCS1_v1_5
import binascii
from base64 import b64decode
from Crypto.PublicKey import RSA


def rsa_encrypt(s):

    pub = s.replace("OpenSSLRSAPublicKey{modulus=", "").replace("publicExponent=", "").replace(",10001}", "")
    e = int('10001', 16)
    n = int(pub, 16)
    w = RSA.construct((n, e)).publickey().exportKey()
    w = str(w)
    w = w.replace("b'-----BEGIN PUBLIC KEY-----", "").replace("-----END PUBLIC KEY-----'", "").replace(r"\n", "")

    public_key = w
    public_key = public_key.replace(r"\n", "")
    key = b64decode(public_key)
    key = RSA.importKey(key)

    cipher = PKCS1_v1_5.new(key)
    ciphertext = cipher.encrypt(bytes("thats the stuff", "utf-8"))
    ciphertext = binascii.hexlify(ciphertext)
    ciphertext = str(ciphertext)
    return ciphertext

