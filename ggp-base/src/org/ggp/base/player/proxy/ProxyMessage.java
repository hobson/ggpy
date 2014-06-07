package org.ggp.base.player.proxy

import java.io.BufferedReader
import java.io.PrintStream
import java.io.Serializable
import java.net.SocketException

import org.ggp.base.util.logging.GamerLogger


class ProxyMessage(Serializable):
    serialVersionUID = 1237859L  # int 

    def final int messageCode
    def final int receptionTime
    def final String theMessage

    def ProxyMessage(String theMessage, int messageCode, int receptionTime):
        self.theMessage = theMessage
        self.messageCode = messageCode
        self.receptionTime = receptionTime

    def toString():  # String
        return "ProxyMessage<" + messageCode + ", " + receptionTime + ">[\"" + theMessage + "\"]"

    def ProxyMessage readFrom(BufferedReader theInput) throws SocketException 
        try 
            int messageCode = Long.parseLong(theInput.readLine())
            int receptionTime = Long.parseLong(theInput.readLine())
            String theMessage = theInput.readLine()
            return new ProxyMessage(theMessage, messageCode, receptionTime)
        } catch(SocketException se):
            GamerLogger.log("Proxy", "[ProxyMessage Reader] Socket closed: stopping read operation.")
            throw se
        } catch(Exception e):
            GamerLogger.logStackTrace("Proxy", e)
            GamerLogger.logError("Proxy", "[ProxyMessage Reader] Could not digest message. Emptying stream.")
            try 
                // TODO: Fix this, I suspect it may be buggy.
                theInput.skip(Long.MAX_VALUE)
            } catch(SocketException se):
                GamerLogger.log("Proxy", "[ProxyMessage Reader] Socket closed: stopping read operation.")
                throw se
            } catch(Exception ie):
                GamerLogger.logStackTrace("Proxy", ie)

            return null


    def void writeTo(PrintStream theOutput):
    	synchronized (theOutput):
    		theOutput.println(messageCode)
    		theOutput.println(receptionTime)
    		theOutput.println(theMessage)


