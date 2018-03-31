#TCP server coded by Anthony Wilkinson
#Cyber550 Assignment 2
#Used code references from http://pycryptodome.readthedocs.io/en/latest/src/examples.html
#Used code references from https://docs.python.org/3.3/library/socket.html#socket.socket.settimeout

import socket
import sys
from Cryptodome.Cipher import AES

SERVER_IP = "127.0.0.1" #Server IP using Loopback for testing
SERVER_PORT = 9000   #Server Port
CIPHER_KEY=b'12345678sixteen!' #Shared Key
TCP_BUFFER= 1024 #Buffer for receiving data
NONCE=b'12345678998765$$'
          
TCPserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initialize TCP stream
TCPserver.bind((SERVER_IP, SERVER_PORT)) #Bind TCP Stream connectoin
TCPserver.listen(2) #Listen for two TCP connections

conn, addr = TCPserver.accept() #connection 1 which is clientA
print('Client A Connected From:', addr)
print()
conn1, addr2 = TCPserver.accept() #connection 2 which is clientB
print('Client B Connected From:', addr)
print()


while True:
	print("Received Secret Encrypted Message...")
	print()
	print("Decrypting using Shared Key...")
	data=conn.recv(TCP_BUFFER) #ClientA sending cipher message
	ciphertext=data
	#print(ciphertext)
	cipher = AES.new(CIPHER_KEY, AES.MODE_EAX,NONCE)
	plaintext = cipher.decrypt(ciphertext) #decryption of cipher message passed from client A
	#print(plaintext)
	#print("data:", data)
	conn1.sendall(plaintext)
	print()
	print("Decrypted Message Sent to ClientB!")
	break

print("Goodbye!")
TCPserver.close()