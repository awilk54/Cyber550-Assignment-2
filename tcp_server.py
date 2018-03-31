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

conn, addr = TCPserver.accept()
print('Client A Connected From:', addr)
print()
conn1, addr2 = TCPserver.accept()
print('Client B Connected From:', addr)
print()


while True:
	print("Received Secret Encrypted Message...")
	print()
	print("Decrypting using Shared Key...")
	data=conn.recv(TCP_BUFFER)
	ciphertext=data
	print(ciphertext)
	#datanonce=conn.recv(TCP_BUFFER)
	#print(datanonce)
	#nonce=datanonce
	cipher = AES.new(CIPHER_KEY, AES.MODE_EAX,NONCE)
	plaintext = cipher.decrypt(ciphertext)
	print(plaintext)
	print("data:", data)
	#data1=conn1.recv(TCP_BUFFER)
	#print("data1:", data1)
	conn1.sendall(plaintext)
	break

TCPserver.close()