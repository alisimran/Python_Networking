#!/usr/bin/env python

import socket

# To get socket time out and change it

def get_socket_timeout():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	Dtimeout = sock.gettimeout()
	print(f'Default socket timeout : {Dtimeout}')
	sock.settimeout(140)
	Ctimeout = sock.gettimeout()
	print(f'Modified socket timeout : {Ctimeout}')
if __name__ == '__main__':
	get_socket_timeout()
