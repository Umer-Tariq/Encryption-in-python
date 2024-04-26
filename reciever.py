import socket
from cryptography.fernet import Fernet

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 9998))

s.listen(1)

conn, addr = s.accept()

msg = conn.recv(1024)

with open('encrypted_key.txt', 'rb') as key_file:
    key = key_file.read()

cypher_suite = Fernet(key)

msg = cypher_suite.decrypt(msg).decode()

print(msg)

conn.close()
s.close()
