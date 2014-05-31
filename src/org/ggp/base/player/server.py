#!/usr/bin/python           # This is server.py file

import socket               # Import socket module


class ServerSocket():
    '''Consider using SocketServer instead: https://docs.python.org/2/library/socketserver.html'''
    port0 = 9147
    listeners = {-1: None}

    def __init__(self, num=0):
        # TODO: reuse closed socket IDs
        if num is None:
            self.num = max(ServerSocket.listeners) + 1
        else:
            self.num = num
        self.listener = socket.socket()
        self.host = socket.gethostname()  # Get local machine name
        self.port = self.port0 + self.num  # Reserve a port for this game player

        try:
            self.listener.bind((self.host, self.port))  # Bind to the port
            ServerSocket.listeners[self.num] = self.listener
        except:  # can't find a more specific Exception for 
            self.listener.close()
            self.__init__(num=self.num + 1)

    def shutdown(self):
        self.listener.close()
        del(ServerSocket.listeners[self.num])

    def listen(self, backlog=5):
        try: 
            self.listener.listen(backlog)      # Now wait for client connection, allowing a backlog of up to 5 connections in the queue.
            while True:
               c, addr = self.listener.accept()     # Establish connection with client.
               print 'Got connection from', addr
               c.send('Thank you for connecting')
               c.close()                # Close the connection
        except KeyboardInterrupt:
            self.shutdown()
