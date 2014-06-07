#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()

host = socket.gethostname() # Get local machine name
port = 9147 # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close.close()  # Close the socket when done