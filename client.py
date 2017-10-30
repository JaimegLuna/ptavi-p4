#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
SERVER = sys.argv[1]
PORT = int(sys.atgv[2])
LINE = sys.argv[4]
EXPIRES = sys.argv[5]
  
# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
def regist():
	DATA = " ".join(["REGISTER sip:" LINE, EXPIRES, "SIP/2.0\r\n\r\n"])
	my_socket.send(DATA, "utf-8"))
	
	

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
	my_socket.connect((SERVER, PORT))
	print("Enviando:", LINE)
	regist()
	
print("Socket terminado.")
