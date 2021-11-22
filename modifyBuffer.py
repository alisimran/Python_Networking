#!/usr/bin/env python

# To modify the default buffer size
import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buffer():
	# Make a socket instance
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# get the size of the socket's send buffer
	defbuffsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
	print(f'Buffer size [BEFORE]: {defbuffsize}')
	sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)
	newbufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
	print(f'Buffer size [AFTER]: {newbufsize}')

if __name__ == '__main__':
	modify_buffer() 
