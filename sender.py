from cryptography.fernet import Fernet
import socket
import subprocess 
import time


text = 'Hello!'
encrpyt_key = Fernet.generate_key()
cypher_suite = Fernet(encrpyt_key)

encrpyt_msg = cypher_suite.encrypt(text.encode())

with open('encrypted_key.txt', 'wb') as key_file:
    key_file.write(encrpyt_key)

reciever_process = subprocess.Popen(['python', 'reciever.py'])

time.sleep(2)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 9998))

s.send(encrpyt_msg)

s.close()