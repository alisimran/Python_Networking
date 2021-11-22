#!/usr/bin/env python

import socket
import sys
import argparse

host = '127.0.0.1'

def echo_client(port):
	"""A simple echo client"""
	# create a tcp client
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (host, port)
	print(f'Connecting to {port} port {host}')
	sock.connect(server_address)
	# Looking for response from the server
	try:
		msg = " Testing. Echo this message."
		print(f'Sending {msg}')
		sock.sendall(msg.encode('utf-8'))
		# Response
		amount_recv = 0
		amount_exp = len(msg)
		while amount_recv < amount_exp:
			data = sock.recv(16)
			amount_recv += len(data)
			print(f'Received {data}')
	except socket.error as e:
		print(f'Socket Error {e}')
	except Exception as e:
		print(f'Other exception {e}')
	finally:
		print('Closing connection to the server')
		sock.close()
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Socket Server Example')
	parser.add_argument('--port', action='store', dest='port', type=int, required=True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_client(port)
