#!/usr/bin/env python

import socket
import sys
import argparse

host = '127.0.0.1'
data_payload = 2048
# back log limits the maximum no of client request when the server is not accepting

backlog = 5

def echo_server(port):
	"""A simple echo server """
	# Create a TCP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Enabling reuse of address and port
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# Binding the socket to a port
	server_address = (host, port)
	print(f'Starting up the server on {port} at {host}..... ')
	sock.bind(server_address)
	# Listem to clients 
	sock.listen(backlog)
	while True:
		print('Waiting to receive message form client')
		# accepting the connections
		client, address = sock.accept()
		data = client.recv(data_payload)
		if data:
			print(f'Data: {data}')
			# sending back the data
			client.send(data)
			print(f'sent {data} bytes back to the {address}')
		# ending the connection
		client.close()

if __name__ == '__main__':
	# To take argument provided by the client
	parser = argparse.ArgumentParser(description='Socket Server example')
	parser.add_argument('--port', action='store', dest='port', type=int, required=True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_server(port)
