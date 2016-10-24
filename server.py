#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""
import sys
import socketserver

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    
    def handle(self):

        self.wfile.write(b"Hemos recibido tu peticion")
        IP=self.client_address
        print("IP: " + IP)
        PORT=self.client_address
        print("PORT: " + str(PORT))

        while 1:
            line = self.rfile.read()
            print("El cliente nos manda: " + line.decode(utf-8))
            
if __name__ == "__main__":
    try:
        serv = socketserver.UDPServer(('', 6001), SIPRegisterHandler)
        print("Lanzando servidor UDP de eco...")
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
