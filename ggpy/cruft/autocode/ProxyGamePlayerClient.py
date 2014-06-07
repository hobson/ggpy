#!/usr/bin/env python
""" generated source for module ProxyGamePlayerClient """
# package: org.ggp.base.player.proxy
import java.io.BufferedReader

import java.io.IOException

import java.io.InputStreamReader

import java.io.PrintStream

import java.net.Socket

import java.util.ArrayList

import java.util.List

import org.ggp.base.player.event.PlayerDroppedPacketEvent

import org.ggp.base.player.event.PlayerReceivedMessageEvent

import org.ggp.base.player.event.PlayerSentMessageEvent

import org.ggp.base.player.gamer.Gamer

import org.ggp.base.player.gamer.statemachine.random.RandomGamer

import org.ggp.base.player.request.factory.RequestFactory

import org.ggp.base.player.request.grammar.AbortRequest

import org.ggp.base.player.request.grammar.Request

import org.ggp.base.player.request.grammar.StartRequest

import org.ggp.base.player.request.grammar.StopRequest

import org.ggp.base.util.logging.GamerLogger

import org.ggp.base.util.observer.Event

import org.ggp.base.util.observer.Observer

import org.ggp.base.util.observer.Subject

import org.ggp.base.util.reflection.ProjectSearcher

import com.google.common.collect.Lists

class ProxyGamePlayerClient(Thread, Subject, Observer):
    """ generated source for class ProxyGamePlayerClient """
    gamer = Gamer()
    observers = List()
    theConnection = Socket()
    theInput = BufferedReader()
    theOutput = PrintStream()

    # 
    #      * @param args
    #      * Command line arguments:
    #      *  ProxyGamePlayerClient gamer port
    #      
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        GamerLogger.setSpilloverLogfile("spilloverLog")
        GamerLogger.log("Proxy", "Starting the ProxyGamePlayerClient program.")
        if not (len(args)):
            GamerLogger.logError("Proxy", "Usage is: \n\tProxyGamePlayerClient gamer port")
            return
        port = 9147
        gamer = None
        try:
            port = Integer.valueOf(args[1])
        except Exception as e:
            GamerLogger.logError("Proxy", args[1] + " is not a valid port.")
            return
        gamers = Lists.newArrayList(ProjectSearcher.GAMERS.getConcreteClasses())
        gamerNames = ArrayList()
        if len(gamerNames) != len(gamers):
            for c in gamers:
                gamerNames.add(c.__name__.replaceAll("^.*\\.", ""))
        idx = gamerNames.indexOf(args[0])
        if idx == -1:
            GamerLogger.logError("Proxy", args[0] + " is not a subclass of gamer.  Valid options are:")
            for s in gamerNames:
                GamerLogger.logError("Proxy", "\t" + s)
            return
        try:
            gamer = (gamers.get(idx).newInstance())
        except Exception as ex:
            GamerLogger.logError("Proxy", "Cannot create instance of " + args[0])
            return
        try:
            theClient.start()
        except IOException as e:
            GamerLogger.logStackTrace("Proxy", e)

    def __init__(self, port, gamer):
        """ generated source for method __init__ """
        super(ProxyGamePlayerClient, self).__init__()
        self.observers = ArrayList()
        self.theConnection = Socket("127.0.0.1", port)
        self.theOutput = PrintStream(self.theConnection.getOutputStream())
        self.theInput = BufferedReader(InputStreamReader(self.theConnection.getInputStream()))
        self.gamer = gamer
        gamer.addObserver(self)

    def addObserver(self, observer):
        """ generated source for method addObserver """
        self.observers.add(observer)

    def notifyObservers(self, event):
        """ generated source for method notifyObservers """
        for observer in observers:
            observer.observe(event)

    theCode = long()

    def run(self):
        """ generated source for method run """
        while not isInterrupted():
            try:
                GamerLogger.log("Proxy", "[ProxyClient] Got message: " + theMessage)
                self.theCode = theMessage.messageCode
                self.notifyObservers(PlayerReceivedMessageEvent(in_))
                if isinstance(request, (StartRequest, )):
                    RequestFactory().create(theDefaultGamer, in_).process(1)
                    GamerLogger.startFileLogging(theDefaultGamer.getMatch(), theDefaultGamer.getRoleName().__str__())
                    GamerLogger.log("Proxy", "[ProxyClient] Got message: " + theMessage)
                outMessage.writeTo(self.theOutput)
                GamerLogger.log("Proxy", "[ProxyClient] Sent message: " + outMessage)
                self.notifyObservers(PlayerSentMessageEvent(out))
                if isinstance(request, (StopRequest, )):
                    GamerLogger.log("Proxy", "[ProxyClient] Got stop request, shutting down.")
                    System.exit(0)
                if isinstance(request, (AbortRequest, )):
                    GamerLogger.log("Proxy", "[ProxyClient] Got abort request, shutting down.")
                    System.exit(0)
            except Exception as e:
                GamerLogger.logStackTrace("Proxy", e)
                self.notifyObservers(PlayerDroppedPacketEvent())
        GamerLogger.log("Proxy", "[ProxyClient] Got interrupted, shutting down.")

    def observe(self, event):
        """ generated source for method observe """
        if isinstance(event, (WorkingResponseSelectedEvent, )):
            theMessage.writeTo(self.theOutput)
            GamerLogger.log("Proxy", "[ProxyClient] Sent message: " + theMessage)


if __name__ == '__main__':
    import sys
    ProxyGamePlayerClient.main(sys.argv)

