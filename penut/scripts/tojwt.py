import jwt
from get_private import pri
from Crypto.Cipher import AES
import binascii
from .Sec_key import jwtauth


def check(a):
    key = jwtauth()

    qr = bytes(a, "UTF-8")

    ln = len(qr) - 64
    data = qr[:ln]
    hash = qr[ln:]
    hash = str(hash)
    hash = hash[2:-1]

    result = binascii.unhexlify(data)

    private_key = pri(hash)

    length = len(result) - 32
    first = 16 + length
    nonce = result[:-first]
    tag = result[16:-length]
    ciphertext = result[32:]
    # let's assume that the key is somehow available again
    cipher = AES.new(private_key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    javaweb = (data.decode("utf-8"))

    try:
        final = jwt.decode(javaweb, key, algorithms="HS256")

        return final
    except jwt.exceptions.InvalidSignatureError:
        return "Information Is Wrong Try Again"
