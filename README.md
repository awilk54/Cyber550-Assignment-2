# Cyber550-Assignment-2
Assignment 2


Repo contains two sets of files. UDP client/server AES encryption sample. This model sends a secret message from client to server encrypted using AES and then the server decrpts it and sends it back to client in clear text.

Second set of files are for TCP client/server AES example. First run TCP server and then run TCP_ClientA.py. ClientA will ask for a secret message to be entered. Once you enter a message, it will encrypt with AES and send it to the server, then close clientA's connection to server. Lastly run ClientB.py which will connect to the same server. Once ClientB connects, the server will send the decrypted message to clientB terminal output. 

Both ClientA and Server contain the same shared cipher_Key and Nonce for validation and decryption. 
