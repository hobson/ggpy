#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
#import sys
import SocketServer
import time
from traceback import print_exc

class Server(object):
    '''Consider using SocketServer instead: https://docs.python.org/2/library/socketserver.html'''
    host = 'localhost'
    port0 = 9147
    listeners = {-1: None}

    class TCPEchoer(SocketServer.StreamRequestHandler):

        def handle(self):
            # self.rfile is a file-like object created by the handler;
            # we can now use e.g. readline() instead of raw recv() calls
            self.data = self.rfile.readline().strip()
            print "{} wrote:".format(self.client_address[0])
            print self.data
            # Likewise, self.wfile is a file-like object used to write back
            # to the client
            self.wfile.write(self.data.upper())

    def __init__(self, num=0, host='localhost', port=9147):

        # TODO: reuse closed socket IDs
        if num is None:
            self.num = max(Server.listeners) + 1
        else:
            self.num = num
        if not self.num is None:
            self.port = self.port0 + self.num  # Reserve a port for this game player
        self.host = self.host or 'localhost'    
        
        try:
            self.listener = SocketServer.TCPServer((self.host, self.port), self.TCPEchoer)
            Server.listeners[self.num] = self.listener
        except:  # can't find a more specific Exception for 
            self.shutdown()
            self.__init__(num=self.num + 1)

    def shutdown(self):
        try:
            self.listener.shutdown()
            self.listener = None
        except:
            pass
        if self.num in Server.listeners:
            del(Server.listeners[self.num])

    def serve_forever(self):
        try: 
            self.listener.serve_forever()
        except KeyboardInterrupt:
            self.shutdown()
        except Exception as e:
            print repr(e)
            print_exc()


class Client(object):
    host, port0 = Server.host, Server.port0
    packet_len = 1024
    eol = '\n'
    delay = 0
    verbosity = 1

    def __init__(self, host=None, port=None, header=''):
        if host:
            self.host = host
        if port:
            self.port = port
        else:
            self.port = self.port0
        #.join(sys.argv[1:])
        # Create a socket (SOCK_STREAM means a TCP socket)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def send(self, messages='', delay=None, eol=None, verbosity=None, keep_open=False):
        if eol is None:
            eol = self.eol
        if verbosity is None:
            verbosity = self.verbosity
        if delay is None:
            delay = self.delay
        if isinstance(messages, basestring):
            messages = [messages]
        try:
            if keep_open:
                self.sock.connect((self.host, self.port))
            for msg in messages:
                self.msg = msg
                # Connect to server and send data
                self.msg += eol if not msg.endswith(eol) else ''
                if not keep_open:
                    self.sock.connect((self.host, self.port))
                self.sock.sendall(self.msg)
                # Receive data from the server and shut down
                self.received = self.sock.recv(self.packet_len)
                if not keep_open:
                    self.sock.close()
                if verbosity:
                    print "Sent:        {}".format(self.msg)
                    print "   Received: {}".format(self.received)
                if delay:
                    time.sleep(self.delay)
        finally:  # this should capture CTRL-C keyboard interrupts and kill signals
            if keep_open:
                self.sock.close()
