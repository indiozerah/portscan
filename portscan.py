#!/usr/bin/pyhton3
import socket
import sys

if len(sys.argv) != 2:
        print("Uso: python3 scanner_de_portas.py <ip>")
        sys.exit(1)

host = sys.argv[1]

for porta in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        resultado = sock.connect_ex((host, porta))

        if resultado == 0:
                print(f"Porta {porta} [ABERTA]")

        sock.close()
