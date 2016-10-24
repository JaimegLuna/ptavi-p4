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

    dicc = {}

    def get_expires(self, mensaje):
        time = mensaje.split("EXPIRES: ")[1]
        time = time.split("\r")[0]
        return (int(time))

    def handle(self):

        IP = self.client_address[0]
        print("IP: " + IP)
        PORT = self.client_address[1]
        print("PORT: " + str(PORT))
        self.wfile.write(b"Hemos recibido tu peticion")
        line = self.rfile.read()
        mensaje_reci = line.decode('utf-8')
        tipo_mensaje = mensaje_reci.split(' ')[0]

        if tipo_mensaje == "Regsiter":
            print("El cliente nos manda: " + tipo_mensaje)
            nombre = self.get_nombre(mensaje_reci)
            time_expires = self.get_expires(mensaje_reci)
            self.dicc[nombre] = IP
            print(self.dicc)
            self.wfile.write(b"SIP/2.0 200 ok\r\n\r\n")

        if time_expires == 0:
            print("usuario eliminado")
            del self.dicc[nombre]
        else:
            print("tiempo no expirado, no borro nada")

        self.wfile.write(b"SIP/2.0 200 ok\r\n\r\n")

        while 1:
            line = self.rfile.read()
            print("El cliente nos manda: " + line.decode('utf-8'))
            mensaje_reci = line.decode('utf-8')
            print("El cliente nos manda: " + mensaje_reci)

            if not line:
                break
if __name__ == "__main__":
    try:
        serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)
        print("Lanzando servidor UDP de eco...")
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
