#!/usr/bin/env python
import socket

# To get service name by passing port no and protocol
def findServiceInfo():
	protocolName = 'tcp'
	portArr = [80, 25, 443, 22]
	for port in portArr:
		service = socket.getservbyport(port, protocolName)
		print("Port: %s   ----- service name: %s" %(port, service))
if __name__ == '__main__':
	findServiceInfo()
