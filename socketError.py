#!/usr/bin/env python
import sys
import socket
import argparse

# To handle server errors

def main():
	# Setting up argument parsing
	parser = argparse.ArgumentParser(description="Socket Error Examples")
	parser.add_argument('--host', action="store", dest="host", required=False)
	parser.add_argument('--port', action="store", dest="port", type=int, required=False)
	parser.add_argument('--file', action="store", dest="file", required=False)
	
	given_args = parser.parse_args()
	host = given_args.host
	port = given_args.port
	filename = given_args.file
	
	# Try creating a socket
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error as e:
		print(f'Error creating socket: {e}')
		sys.exit(1)
	# Connct to a given host/port
	try:
		s.connect((host, port))
	#Gai : get address info: gives error if an invalid address
	except socket.gaierror as e:
		print(f'Address related error connecting to server : {e}')
	# Try sending data
	try:
		msg = "GET %s HTTP/1.0\r\n\r\n" %filename
		s.sendall(msg.encode('utf-8'))
	except socket.error as e:
		print(f'Error sending data {e}')
		sys.exit(1)
	while 1:
		# Wait for the reply
		try:
			buff = s.recv(2048)
		except socket.error as e:
			print(f'Error receiving data: {e}')
			sys.exit(1)
		if not len(buff):
			break
		# write the received data
		sys.stdout.write(buff.decode('utf-8'))
if __name__ ==  '__main__':
	main()
