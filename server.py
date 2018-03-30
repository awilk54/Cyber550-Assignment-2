import socket
import sys
from Cryptodome.Cipher import AES


UDP_SERVER_IP = "127.0.0.1"
UDP_BUFFER=2048
PORT= 9000
CIPHER_KEY=b'12345678sixteen!'


UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Create UDP Socket
UDPSocket.bind((UDP_SERVER_IP, PORT)) #Bind the socket to IP/Port


while True:
	data,addr=UDPSocket.recvfrom(UDP_BUFFER)
	print ("Cipher Text Recieved:",data)
	ciphertext=data
	data,addr=UDPSocket.recvfrom(UDP_BUFFER)
	print ("Nonce Key Recieved:",data)
	nonce=data
	cipher = AES.new(CIPHER_KEY, AES.MODE_EAX, nonce=nonce)
	plaintext = cipher.decrypt(ciphertext)
	print(plaintext)
	UDPSocket.sendto(plaintext,addr)
	print("sent client password back in clear text")
	break
	
UDPSocket.close()