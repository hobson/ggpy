#!/usr/bin/env python
""" generated source for module Test_Http """
# package: org.ggp.base.util.http
import java.io.BufferedWriter

import java.io.IOException

import java.io.OutputStreamWriter

import java.io.PrintWriter

import java.net.ServerSocket

import java.net.Socket

import java.net.URLEncoder

import junit.framework.TestCase

# 
#  * Unit tests for the HttpReader/HttpWriter pair, which are the way that
#  * game players and game servers communicate. Please update these tests
#  * as needed when bugs are discovered, to prevent regressions.
#  *
#  * @author Sam
#  
class Test_Http(TestCase):
    """ generated source for class Test_Http """
    def testSimpleEcho(self):
        """ generated source for method testSimpleEcho """
        testPair = SocketPair()
        doSimpleEchoCheck(testPair, "Hello World", "SamplePlayer")

    def testPathologicalEchos(self):
        """ generated source for method testPathologicalEchos """
        testPair = SocketPair()
        doSimpleEchoCheck(testPair, "", "")
        doSimpleEchoCheck(testPair, "", "SamplePlayer")
        doSimpleEchoCheck(testPair, "123 456 ^&!*! // 2198725 !@#$%^&*() DATA", "SamplePlayer")
        doSimpleEchoCheck(testPair, "abcdefgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "SamplePlayer")
        doSimpleEchoCheck(testPair, "Test String", "")
        doSimpleEchoCheck(testPair, "Test String", "!@#$%^&*()1234567890")
        doSimpleEchoCheck(testPair, "Test String", "abcdefgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def testGenericPOSTs(self):
        """ generated source for method testGenericPOSTs """
        testPair = SocketPair()
        doClientEchoCheckOverPOST(testPair, "", "")
        doClientEchoCheckOverPOST(testPair, "Test String", "")
        doClientEchoCheckOverPOST(testPair, "Test String", "Accept: text/delim\nSender: GAMESERVER")
        doClientEchoCheckOverPOST(testPair, "1234567890abcdefgijklmnopqrstuvwxyz!@#$%^&*()1234567890", "")

    def testGenericGETs(self):
        """ generated source for method testGenericGETs """
        testPair = SocketPair()
        doClientEchoCheckOverGET(testPair, "", "")
        doClientEchoCheckOverGET(testPair, "Test String", "")
        doClientEchoCheckOverGET(testPair, "Test String", "Accept: text/delim\nSender: GAMESERVER")
        doClientEchoCheckOverGET(testPair, "1234567890abcdefgijklmnopqrstuvwxyz!@#$%^&*()1234567890", "")

    #  Helper functions for running specific checks.
    def doSimpleEchoCheck(self, p, data, playerName):
        """ generated source for method doSimpleEchoCheck """
        HttpWriter.writeAsClient(p.client, "", data, playerName)
        readData = HttpReader.readAsServer(p.server)
        assertEquals(readData.toUpperCase(), data.toUpperCase())
        HttpWriter.writeAsServer(p.server, data)
        readData = HttpReader.readAsClient(p.client)
        assertEquals(readData.toUpperCase(), data.toUpperCase())

    def doClientEchoCheckOverPOST(self, p, data, headers):
        """ generated source for method doClientEchoCheckOverPOST """
        writeClientPostHTTP(p.client, headers, data)
        readData = HttpReader.readAsServer(p.server)
        assertEquals(readData.toUpperCase(), data.toUpperCase())

    def doClientEchoCheckOverGET(self, p, data, headers):
        """ generated source for method doClientEchoCheckOverGET """
        writeClientGetHTTP(p.client, headers, data)
        readData = HttpReader.readAsServer(p.server)
        assertEquals(readData.toUpperCase(), data.toUpperCase())

    #  Helper functions for testing different types of HTTP interactions.
    def writeClientPostHTTP(self, writeOutTo, headers, data):
        """ generated source for method writeClientPostHTTP """
        bw = BufferedWriter(OutputStreamWriter(writeOutTo.getOutputStream()))
        pw = PrintWriter(bw)
        pw.println("POST / HTTP/1.0")
        if 0 > len(headers):
            pw.println(headers)
        pw.println("Content-length: " + len(data))
        pw.println()
        pw.println(data)
        pw.flush()

    def writeClientGetHTTP(self, writeOutTo, headers, data):
        """ generated source for method writeClientGetHTTP """
        bw = BufferedWriter(OutputStreamWriter(writeOutTo.getOutputStream()))
        pw = PrintWriter(bw)
        pw.println("GET /" + URLEncoder.encode(data, "UTF-8") + " HTTP/1.0")
        if 0 > len(headers):
            pw.println(headers)
        pw.println("Content-length: 0")
        pw.println()
        pw.println()
        pw.flush()

    #  Utility class to create a pair of client/server sockets
    #  on the local machine that are connected to each other.
    class SocketPair(object):
        """ generated source for class SocketPair """
        client = Socket()
        server = Socket()

        def __init__(self):
            """ generated source for method __init__ """
            #  Create a server socket on the first available port.
            defaultTestingPort = 13174
            ss = None
            while True:
                try:
                    ss = ServerSocket(defaultTestingPort)
                except Exception as e:
                    ss = None
                    defaultTestingPort += 1
                if not ((ss == None)):
                    break
            try:
                self.client = Socket("127.0.0.1", defaultTestingPort)
                self.server = ss.accept()
            except Exception as e:
                fail("Could not establish connection: " + e)
                e.printStackTrace()
            assertNotNull(self.client)
            assertNotNull(self.server)

