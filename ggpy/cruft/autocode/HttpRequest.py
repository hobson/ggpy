#!/usr/bin/env python
""" generated source for module HttpRequest """
# package: org.ggp.base.util.http
import java.io.IOException

import java.net.InetAddress

import java.net.InetSocketAddress

import java.net.Socket

# 
#  * HttpRequest is a helper class that encapsulates all of the code necessary
#  * for a match host to issue a long-lived HTTP request to a player, wait for
#  * the response, and return it. This is a key part of the GGP gaming protocol.
#  *
#  * @author schreib
#  
class HttpRequest(object):
    """ generated source for class HttpRequest """
    @classmethod
    def issueRequest(cls, targetHost, targetPort, forPlayerName, requestContent, timeoutClock):
        """ generated source for method issueRequest """
        socket = Socket()
        theHost = InetAddress.getByName(targetHost)
        socket.connect(InetSocketAddress(theHost.getHostAddress(), targetPort), 5000)
        HttpWriter.writeAsClient(socket, theHost.getHostName(), requestContent, forPlayerName)
        response = HttpReader.readAsClient(socket) if (timeoutClock < 0) else HttpReader.readAsClient(socket, timeoutClock)
        socket.close()
        return response

