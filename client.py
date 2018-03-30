import socket
import sys
import re
from Cryptodome.Cipher import AES

UDP_SERVER_IP = "127.0.0.1"
UDP_BUFFER=2048
CIPHER_KEY=b'12345678sixteen!'





ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Create UDP Socket

while True:
		Message=input("Enter Message: ")
		Secret_Message= bytes(Message, 'utf-8')
		CIPHER = AES.new(CIPHER_KEY, AES.MODE_EAX)
		nonce = CIPHER.nonce
		ciphertext, tag = CIPHER.encrypt_and_digest(Secret_Message)
		print("Cipher Text Sent To Server: ",ciphertext)
		#print("Cipher Tag:",tag)
		#print("Cipher Key:",CIPHER_KEY)
		#print("Nonce:",nonce)
		ClientSocket.sendto(ciphertext,(UDP_SERVER_IP,9000)) #send ciphertext
		ClientSocket.sendto(nonce,(UDP_SERVER_IP,9000)) #send nonce
		print()
		data,addr=ClientSocket.recvfrom(UDP_BUFFER)
		payload_data=data.decode("utf-8") #decode payload data to string
		payload_data2=payload_data.split(",") #split payload by comma
		TEXT=payload_data2[0]
		#CLEAR_TEXT=re.sub('[^A-Za-z0-9]+', '', TEXT)#strip crap
	
		print("Server decrypted the following message:", TEXT)
		break
ClientSocket.close()