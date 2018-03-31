import socket
import sys
import re
import getpass
from Cryptodome.Cipher import AES

SERVER_IP = "127.0.0.1"    #server IP of 127.0.0.1 LOOPBACK used for testing
SERVER_PORT = 9000         # server Port
CIPHER_KEY=b'12345678sixteen!' #Shared Key
NONCE=b'12345678998765$$' #shared NONCE key for validity

clientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP socket creation
clientA.connect((SERVER_IP, SERVER_PORT)) #TCP connection


while True:
	Secret_Message_Input= getpass.getpass(prompt='Enter Secret Message.. : ' )
	print("Message will Encrypt with AES")
	print()
	raw_message=Secret_Message_Input.encode()
	CIPHER = AES.new(CIPHER_KEY, AES.MODE_EAX, NONCE)
	ciphertext, tag = CIPHER.encrypt_and_digest(raw_message)
	clientA.send(ciphertext)
	clientA.close()
	print()
	break

clientA.close()
print('Message Sent..Goodbye')
print()