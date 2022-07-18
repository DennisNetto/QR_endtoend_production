import io
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import binascii
import qrcode
import jwt
import hashlib
import random


def cryupt(a, b, c, d):
    # secret for the jwt verifacation then sets the id_number to type byte for encoding after that its make into a JWT
    server_option_encrypt = False
    key = b'null'
    secret = 'secrete'
    a1 = bytes(a + b + c + d + str(random.randrange(0, 1000000000)), "utf-8")

    # Hashes the id_number to be used later
    hash = hashlib.sha256()
    hash.update(a1)
    hash1 = (hash.hexdigest())
    h = str(hash1)
    encoded = jwt.encode({"id_number": a, "Hash": h}, secret, algorithm="HS256")

    # Encrypts the JWT then adds the hash to the end and turns it all into a qrcode
    data = bytes(encoded, 'utf-8')

    # Encrypt the data with the AES session key
    if server_option_encrypt:
        key = get_random_bytes(16)
        key = binascii.hexlify(key)
        print(key)
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        content = [x for x in (cipher.nonce, tag, ciphertext)]
        content = content[0] + content[1] + content[2]
        content = bytes(content)
        result = binascii.hexlify(content)
        print(result)

    else:
        result = encoded
    if server_option_encrypt:
        result = result
    print(result)
    qr = qrcode.make(result)
    img_byte_arr = io.BytesIO()
    qr.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return {'prikey': key, 'qrccode': img_byte_arr, 'Hash': h}
