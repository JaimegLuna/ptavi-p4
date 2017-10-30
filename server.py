#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco de un UDP simple
"""


import socketserver
import sys

class SIPRegistHandler(socketserver.DatagramRequestHandler):
	"""
	Echo server class
	"""

	dicc = {}
	def handle(self):
		"""
		handle method of the server class
		(all requests will be handled by this method)
		"""
		self.wfile.write(b"Hemos recibido tu peticion")
		for line in self.rfile:
			if data:
				if data[3] == '0':
					del self.dicc[data[2]]
					self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
				elif int(data[3]) >=0:
					self.dicc[data[2]] = self.client_add[0], data[3]
					print(self.dicc)
						
			

if __name__ == "__main__":
	#Listens at localhost('') port 6001
	#and calls the EchoHandler class to manage the request 
	serv = socketserver.UDPserver(('', int(sys.argv[1])), SIPRegistHandler)
	
	print("Lanzando servidor UDP de eco...")
	try:
		serv.serve_forever()
	except KeyboardInterrupt:
		print("Finalizado servidor")
