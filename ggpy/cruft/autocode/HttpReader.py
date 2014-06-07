#!/usr/bin/env python
""" generated source for module HttpReader """
# package: org.ggp.base.util.http
import java.io.BufferedReader

import java.io.IOException

import java.io.InputStreamReader

import java.net.Socket

import java.net.SocketTimeoutException

import java.net.URLDecoder

class HttpReader(object):
    """ generated source for class HttpReader """
    #  Wrapper methods to support socket timeouts for reading requests/responses.
    @classmethod
    @overloaded
    def readAsClient(cls, socket, timeout):
        """ generated source for method readAsClient """
        socket.setSoTimeout(timeout)
        return cls.readAsClient(socket)

    @classmethod
    @overloaded
    def readAsServer(cls, socket, timeout):
        """ generated source for method readAsServer """
        socket.setSoTimeout(timeout)
        return cls.readAsServer(socket)

    #  Implementations of reading HTTP responses (readAsClient) and
    #  HTTP requests (readAsServer) for the purpose of communicating
    #  with other general game playing systems.
    @classmethod
    @readAsClient.register(object, Socket)
    def readAsClient_0(cls, socket):
        """ generated source for method readAsClient_0 """
        br = BufferedReader(InputStreamReader(socket.getInputStream()))
        return readContentFromPOST(br)

    @classmethod
    @readAsServer.register(object, Socket)
    def readAsServer_0(cls, socket):
        """ generated source for method readAsServer_0 """
        br = BufferedReader(InputStreamReader(socket.getInputStream()))
        #  The first line of the HTTP request is the request line.
        requestLine = br.readLine()
        if requestLine == None:
            raise IOException("The HTTP request was empty.")
        message = str()
        if requestLine.toUpperCase().startsWith("GET "):
            message = requestLine.substring(5, requestLine.lastIndexOf(' '))
            message = URLDecoder.decode(message, "UTF-8")
            message = message.replace(str(13), ' ')
        elif requestLine.toUpperCase().startsWith("POST "):
            message = readContentFromPOST(br)
        elif requestLine.toUpperCase().startsWith("OPTIONS "):
            #  Web browsers can send an OPTIONS request in advance of sending
            #  real XHR requests, to discover whether they should have permission
            #  to send those XHR requests. We want to handle this at the network
            #  layer rather than sending it up to the actual player, so we write
            #  a blank response (which will include the headers that the browser
            #  is interested in) and throw an exception so the player ignores the
            #  rest of this request.
            HttpWriter.writeAsServer(socket, "")
            raise IOException("Drop this message at the network layer.")
        else:
            HttpWriter.writeAsServer(socket, "")
            raise IOException("Unexpected request type: " + requestLine)
        return message

    @classmethod
    def readContentFromPOST(cls, br):
        """ generated source for method readContentFromPOST """
        line = str()
        theContentLength = -1
        theContent = StringBuilder()
        while (line = br.readLine()) != None:
            if line.lower().startsWith("content-length:"):
                try:
                    theContentLength = Integer.parseInt(line.lower().replace("content-length:", "").trim())
                except NumberFormatException as e:
                    raise IOException("Content-Length header can't be parsed: \"" + line + "\"")
            elif 0 == len(line):
                if theContentLength != -1:
                    while i < theContentLength:
                        theContent.append(str(br.read()))
                        i += 1
                    return theContent.__str__().trim()
                else:
                    raise IOException("Could not find Content-Length header.")
        raise IOException("Could not find content in POST request.")

