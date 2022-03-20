import os
import jwt
from Crypto.PublicKey import RSA
from get_private import pri
from Crypto.Cipher import AES, PKCS1_OAEP
import binascii
from comfirm import conff


def check(a):
    key = 'secrete'

    qr = bytes(a, "UTF-8")

    ln = len(qr) - 64
    data = qr[:ln]
    hash = qr[ln:]
    hash = str(hash)
    hash = hash[2:-1]

    result = binascii.unhexlify(data)
    with open('test.bin', 'wb') as f:
        f.write(result)

    file_in = open("test.bin", "rb")
    pri(hash)
    private_key = RSA.import_key(open(hash + ".pem").read())

    enc_session_key, nonce, tag, ciphertext = \
        [file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

    # Decrypt the session key with the private RSA key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Decrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    javaweb = (data.decode("utf-8"))

    final = jwt.decode(javaweb, key, algorithms="HS256")

    res = conff(final['id_number'])
    if res[0] == final['First_name'] and res[1] == final['Last_name'] and res[2] == final['DOB']:
        os.remove(hash + ".pem")
        return res
    else:
        return "Information Is Wrong Try Again"