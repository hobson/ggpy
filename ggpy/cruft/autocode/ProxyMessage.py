#!/usr/bin/env python
""" generated source for module ProxyMessage """
from threading import RLock

_locks = {}
def lock_for_object(obj, locks=_locks):
    return locks.setdefault(id(obj), RLock())


def synchronized(call):
    def inner(*args, **kwds):
        with lock_for_object(call):
            return call(*args, **kwds)
    return inner

# package: org.ggp.base.player.proxy
import java.io.BufferedReader

import java.io.PrintStream

import java.io.Serializable

import java.net.SocketException

import org.ggp.base.util.logging.GamerLogger

class ProxyMessage(Serializable):
    """ generated source for class ProxyMessage """
    serialVersionUID = 1237859L
    messageCode = long()
    receptionTime = long()
    theMessage = str()

    def __init__(self, theMessage, messageCode, receptionTime):
        """ generated source for method __init__ """
        super(ProxyMessage, self).__init__()
        self.theMessage = theMessage
        self.messageCode = messageCode
        self.receptionTime = receptionTime

    def __str__(self):
        """ generated source for method toString """
        return "ProxyMessage<" + self.messageCode + ", " + self.receptionTime + ">[\"" + self.theMessage + "\"]"

    @classmethod
    def readFrom(cls, theInput):
        """ generated source for method readFrom """
        try:
            return ProxyMessage(cls.theMessage, cls.messageCode, cls.receptionTime)
        except SocketException as se:
            GamerLogger.log("Proxy", "[ProxyMessage Reader] Socket closed: stopping read operation.")
            raise se
        except Exception as e:
            GamerLogger.logStackTrace("Proxy", e)
            GamerLogger.logError("Proxy", "[ProxyMessage Reader] Could not digest message. Emptying stream.")
            try:
                #  TODO: Fix this, I suspect it may be buggy.
                theInput.skip(Long.MAX_VALUE)
            except SocketException as se:
                GamerLogger.log("Proxy", "[ProxyMessage Reader] Socket closed: stopping read operation.")
                raise se
            except Exception as ie:
                GamerLogger.logStackTrace("Proxy", ie)
            return None

    def writeTo(self, theOutput):
        """ generated source for method writeTo """
        with lock_for_object(theOutput):
            theOutput.println(self.messageCode)
            theOutput.println(self.receptionTime)
            theOutput.println(self.theMessage)

