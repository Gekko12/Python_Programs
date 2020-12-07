
import socket

serName = 'localhost'
serPort = 12000		# portName 12000 uses Datagram Protocol

clientSocket = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)	 # socket.SOCK_DGRAM is used for UDP datagram transfer

msg = raw_input('Enter sentence in lowercase :')	# as by default input() in py3 converts input into string ....to avoid that we use
											#raw_input ie. input in bytes
clientSocket.sendto(msg ,(serName ,serPort))
modified_msg ,serAddr = clientSocket.recvfrom(2048) 	# 2048 is the buffer size

print(modified_msg)

clientSocket.close()	#UDP connection close

