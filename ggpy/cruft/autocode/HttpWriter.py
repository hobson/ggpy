#!/usr/bin/env python
""" generated source for module HttpWriter """
# package: org.ggp.base.util.http
import java.io.IOException

import java.io.PrintWriter

import java.net.Socket

import java.net.URLEncoder

class HttpWriter(object):
    """ generated source for class HttpWriter """
    @classmethod
    def writeAsClientGET(cls, socket, hostField, data, playerName):
        """ generated source for method writeAsClientGET """
        pw = PrintWriter(socket.getOutputStream())
        pw.print_("GET /" + URLEncoder.encode(data, "UTF-8") + " HTTP/1.0\r\n")
        pw.print_("Accept: text/delim\r\n")
        pw.print_("Host: " + hostField + "\r\n")
        pw.print_("Sender: GAMESERVER\r\n")
        pw.print_("Receiver: " + playerName + "\r\n")
        pw.print_("\r\n")
        pw.print_("\r\n")
        pw.flush()

    @classmethod
    def writeAsClient(cls, socket, hostField, data, playerName):
        """ generated source for method writeAsClient """
        pw = PrintWriter(socket.getOutputStream())
        pw.print_("POST / HTTP/1.0\r\n")
        pw.print_("Accept: text/delim\r\n")
        pw.print_("Host: " + hostField + "\r\n")
        pw.print_("Sender: GAMESERVER\r\n")
        pw.print_("Receiver: " + playerName + "\r\n")
        pw.print_("Content-Type: text/acl\r\n")
        pw.print_("Content-Length: " + len(data) + "\r\n")
        pw.print_("\r\n")
        pw.print_(data)
        pw.flush()

    @classmethod
    def writeAsServer(cls, socket, data):
        """ generated source for method writeAsServer """
        pw = PrintWriter(socket.getOutputStream())
        pw.print_("HTTP/1.0 200 OK\r\n")
        pw.print_("Content-type: text/acl\r\n")
        pw.print_("Content-length: " + len(data) + "\r\n")
        pw.print_("Access-Control-Allow-Origin: *\r\n")
        pw.print_("Access-Control-Allow-Methods: POST, GET, OPTIONS\r\n")
        pw.print_("Access-Control-Allow-Headers: Content-Type\r\n")
        pw.print_("Access-Control-Allow-Age: 86400\r\n")
        pw.print_("\r\n")
        pw.print_(data)
        pw.flush()

