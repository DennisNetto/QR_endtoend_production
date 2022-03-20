import io
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import binascii
import qrcode
import jwt
import hashlib


def cryupt(a, b, c, d):
    # secret for the jwt verifacation then sets the id_number to type byte for encoding after that its make into a JWT
    secret = 'secrete'
    a1 = bytes(a, "utf-8")
    encoded = jwt.encode({"id_number": a, "First_name": b, "Last_name": c, "DOB": d}, secret, algorithm="HS256")

    # Creates a temperary directory to handle the function then creates pems for encrtption and decrytion

    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    # Hashes the id_number to be used later
    hash = hashlib.sha256()
    hash.update(a1)
    hash1 = (hash.hexdigest())
    h = str(hash1)

    # Encrypts the JWT then adds the hash to the end and turns it all into a qrcode
    data = encoded.encode("utf-8")

    recipient_key = RSA.import_key(public_key)
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    content = [x for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
    content = content[0] + content[1] + content[2] + content[3]
    content = bytes(content)
    result = binascii.hexlify(content)
    h = bytes(h, 'utf-8')
    result = result + h
    qr = qrcode.make(result)
    img_byte_arr = io.BytesIO()
    qr.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return {'prikey': private_key, 'qrccode': img_byte_arr}



