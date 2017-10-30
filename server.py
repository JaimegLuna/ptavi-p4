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
			dicc[SERVER] = port
			print("El cliente nos manda ", dicc[SERVER])

if __name__ == "__main__":
	#Listens at localhost('') port 6001
	#and calls the EchoHandler class to manage the request 
	serv = socketserver.UDPserver(('', 6001), EchoHandler)
	
	print("Lanzando servidor UDP de eco...")
	try:
		serv.serve_forever()
	except KeyboardInterrupt:
		print("Finalizado servidor")
