#!/usr/bin/env python
""" generated source for module PlayerPresence """
from threading import RLock

_locks = {}
def lock_for_object(obj, locks=_locks):
    return locks.setdefault(id(obj), RLock())


def synchronized(call):
    def inner(*args, **kwds):
        with lock_for_object(call):
            return call(*args, **kwds)
    return inner

# package: org.ggp.base.util.presence
import java.io.IOException

import org.ggp.base.server.request.RequestBuilder

import org.ggp.base.util.http.HttpRequest

class PlayerPresence(object):
    """ generated source for class PlayerPresence """
    host = str()
    port = int()
    name = str()
    status = str()
    statusTime = long()

    def __init__(self, host, port):
        """ generated source for method __init__ """
        self.host = host
        self.port = port
        self.name = None
        self.status = None
        self.statusTime = 0

    def updateInfo(self):
        """ generated source for method updateInfo """
        info = InfoResponse()
        try:
            info = InfoResponse.create(infoFull)
        except IOException as e:
            info = InfoResponse()
            info.setName(None)
            info.setStatus("error")
        with lock_for_object(self):
            self.name = info.__name__
            self.status = info.getStatus()
            self.statusTime = System.currentTimeMillis()

    @synchronized
    def getName(self):
        """ generated source for method getName """
        return self.name

    @synchronized
    def getStatus(self):
        """ generated source for method getStatus """
        return self.status

    @synchronized
    def getStatusAge(self):
        """ generated source for method getStatusAge """
        return System.currentTimeMillis() - self.statusTime

    def getHost(self):
        """ generated source for method getHost """
        return self.host

    def getPort(self):
        """ generated source for method getPort """
        return self.port

