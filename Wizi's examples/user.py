from socket import *

IP_ADDR = 'localhost'
PORT = 9090

def sendBlock(nameoffile):
	sock = socket(AF_INET, SOCK_DGRAM)
	f = open(nameoffile,'rb')

	while True:
		data = f.readline()
		
		if (data == b''):
			sock.sendto(b'~EOF~',(IP_ADDR, PORT))
			break

		sock.sendto(data, (IP_ADDR, PORT))