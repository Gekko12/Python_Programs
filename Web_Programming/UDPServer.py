
import socket

serPort = 12000	#port for datagram protocol
serverSock = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)
serverSock.bind(('' ,serPort))

print ("The server is ready to receive ........")

while True :
	msg ,clientAddr = serverSock.recvfrom(2048)
	modified_msg = msg.upper()
	serverSock.sendto(modified_msg ,clientAddr)

