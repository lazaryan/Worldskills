from socket import *

IP_ADDR = 'localhost'
PORT = 9090

def takeBlock(nameoffile):

	sock = socket(AF_INET, SOCK_DGRAM)
	sock.bind((IP_ADDR, PORT))

	f = open(nameoffile, 'a+')

	while True:
		
		data = sock.recv(1024)
		data = data.decode()

		if (data == '~EOF~'):
			f.close()
			sock.close()
			break

		f.write(data)