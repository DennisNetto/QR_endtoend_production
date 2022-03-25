import socket
import threading
from tojwt import check
from android_reencrypt import rsa_encrypt

HEADER = 5000
PORT = 5050
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)
        if msg:
            pubkey = conn.recv(HEADER).decode(FORMAT)
            msg = str(msg)
            pubkey = str(pubkey)
            retun = check(msg)
            retun = str(retun)
            pubkey = str(pubkey)
            encrypted = rsa_encrypt(pubkey, retun)
            retun = str(encrypted)
            conn.send(retun.encode(FORMAT))
            print("Message returned")
            connected = False

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()