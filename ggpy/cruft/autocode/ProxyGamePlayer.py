#!/usr/bin/env python
""" generated source for module ProxyGamePlayer """
# package: org.ggp.base.player.proxy
import java.io.BufferedReader

import java.io.IOException

import java.io.InputStream

import java.io.InputStreamReader

import java.io.PrintStream

import java.net.ServerSocket

import java.net.Socket

import java.net.SocketException

import java.util.ArrayList

import java.util.List

import java.util.Random

import java.util.concurrent.ArrayBlockingQueue

import java.util.concurrent.BlockingQueue

import org.ggp.base.player.event.PlayerDroppedPacketEvent

import org.ggp.base.player.event.PlayerReceivedMessageEvent

import org.ggp.base.player.event.PlayerSentMessageEvent

import org.ggp.base.player.gamer.Gamer

import org.ggp.base.player.gamer.statemachine.random.RandomGamer

import org.ggp.base.player.request.factory.RequestFactory

import org.ggp.base.player.request.grammar.AbortRequest

import org.ggp.base.player.request.grammar.InfoRequest

import org.ggp.base.player.request.grammar.PlayRequest

import org.ggp.base.player.request.grammar.Request

import org.ggp.base.player.request.grammar.StartRequest

import org.ggp.base.player.request.grammar.StopRequest

import org.ggp.base.util.configuration.GamerConfiguration

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.http.HttpReader

import org.ggp.base.util.http.HttpWriter

import org.ggp.base.util.logging.GamerLogger

import org.ggp.base.util.observer.Event

import org.ggp.base.util.observer.Observer

import org.ggp.base.util.observer.Subject

import org.ggp.base.util.symbol.grammar.SymbolPool

# 
#  * ProxyGamePlayer starts a separate process running an instance of the Gamer
#  * class that is passed in as a parameter. It serves as a proxy between this
#  * Gamer process and the GGP server: it ensures that legal moves are sent back
#  * to the server on time, accepts and stores working moves, and so on.
#  *
#  * This class is not necessary, unless you are interested in adding another
#  * layer of bullet-proofing to your player in preparation for a tournament
#  * or for running your player for long periods of time.
#  *
#  * There are advantages and disadvantages to this approach. The advantages are:
#  *
#  *  1. Even if the Gamer process stalls, for example due to garbage collection,
#  *     you will always send a legal move back to the server in time.
#  *
#  *  2. You can send "working moves" to the proxy, so that if your Gamer process
#  *     stalls, you can send back your best-guess move from before the stall.
#  *
#  * The disadvantage is very simple:
#  *
#  *  1. If the proxy breaks, you can revert to playing extremely poorly
#  *     even though your real Gamer process is fully functional.
#  *
#  * The advantages are very important, and so my response to the disadvantage
#  * has been to shake as many bugs out of the proxy as I can. While the code is
#  * fairly complex, this proxy has proven to be decently reliable in my testing.
#  * So, that's progress.
#  *
#  * @author Sam Schreiber
#  
class ProxyGamePlayer(Thread, Subject):
    """ generated source for class ProxyGamePlayer """
    gamerName = str()
    listener = ServerSocket()
    clientListener = ServerSocket()
    observers = List()
    theClientManager = ClientManager()
    theDefaultGamer = Gamer()

    class ClientManager(Thread):
        """ generated source for class ClientManager """
        theClientProcess = Process()
        theClientConnection = Socket()
        theOutput = PrintStream()
        theInput = BufferedReader()
        outConnector = StreamConnector()
        errConnector = StreamConnector()
        pleaseStop = False
        expectStop = False
        parentThread = Thread()

        def __init__(self, parentThread):
            """ generated source for method __init__ """
            super(ClientManager, self).__init__()
            self.parentThread = parentThread
            command = GamerConfiguration.getCommandForJava()
            processArgs = ArrayList()
            processArgs.add(command)
            processArgs.add("-mx" + GamerConfiguration.getMemoryForGamer() + "m")
            processArgs.add("-server")
            processArgs.add("-XX:-DontCompileHugeMethods")
            processArgs.add("-XX:MinHeapFreeRatio=10")
            processArgs.add("-XX:MaxHeapFreeRatio=10")
            processArgs.add("-classpath")
            processArgs.add(System.getProperty("java.class.path"))
            processArgs.add("org.ggp.base.player.proxy.ProxyGamePlayerClient")
            processArgs.add(self.gamerName)
            processArgs.add("" + self.clientListener.getLocalPort())
            if GamerConfiguration.runningOnLinux():
                processArgs.add(0, "nice")
            pb = ProcessBuilder(processArgs)
            try:
                GamerLogger.log("Proxy", "[PROXY] Starting a new proxy client, using gamer " + self.gamerName + ".")
                self.theClientProcess = pb.start()
                self.outConnector = StreamConnector(self.theClientProcess.getErrorStream(), System.err)
                self.errConnector = StreamConnector(self.theClientProcess.getInputStream(), System.out)
                self.outConnector.start()
                self.errConnector.start()
                self.theClientConnection = self.clientListener.accept()
                self.theOutput = PrintStream(self.theClientConnection.getOutputStream())
                self.theInput = BufferedReader(InputStreamReader(self.theClientConnection.getInputStream()))
                GamerLogger.log("Proxy", "[PROXY] Proxy client started.")
            except IOException as e:
                GamerLogger.logStackTrace("Proxy", e)

        #  TODO: remove this class if nothing is being sent over it
        class StreamConnector(Thread):
            """ generated source for class StreamConnector """
            theInput = InputStream()
            theOutput = PrintStream()
            pleaseStop = False

            def __init__(self, theInput, theOutput):
                """ generated source for method __init__ """
                super(StreamConnector, self).__init__()
                self.theInput = theInput
                self.theOutput = theOutput

            def isPrintableChar(self, c):
                """ generated source for method isPrintableChar """
                if not Character.isDefined(c):
                    return False
                if Character.isIdentifierIgnorable(c):
                    return False
                return True

            def run(self):
                """ generated source for method run """
                try:
                    while not self.pleaseStop:
                        if next == -1:
                            break
                        if not self.isPrintableChar(str(next)):
                            next = '@'
                        self.theOutput.write(next)
                except IOException as e:
                    GamerLogger.log("Proxy", "Might be okay:")
                    GamerLogger.logStackTrace("Proxy", e)
                except Exception as e:
                    GamerLogger.logStackTrace("Proxy", e)
                except Error as e:
                    GamerLogger.logStackTrace("Proxy", e)

        def sendMessage(self, theMessage):
            """ generated source for method sendMessage """
            if self.theOutput != None:
                theMessage.writeTo(self.theOutput)
                GamerLogger.log("Proxy", "[PROXY] Wrote message to client: " + theMessage)

        def run(self):
            """ generated source for method run """
            while self.theInput != None:
                try:
                    if self.pleaseStop:
                        return
                    GamerLogger.log("Proxy", "[PROXY] Got message from client: " + in_)
                    if in_ == None:
                        continue 
                    processClientResponse(in_, self.parentThread)
                except SocketException as se:
                    if self.expectStop:
                        return
                    GamerLogger.logStackTrace("Proxy", se)
                    GamerLogger.logError("Proxy", "Shutting down reader as consequence of socket exception. Presumably this is because the gamer client crashed.")
                    break
                except Exception as e:
                    GamerLogger.logStackTrace("Proxy", e)
                except Error as e:
                    GamerLogger.logStackTrace("Proxy", e)

        def closeClient(self):
            """ generated source for method closeClient """
            try:
                self.outConnector.pleaseStop = True
                self.errConnector.pleaseStop = True
                self.theClientConnection.close()
                self.theInput = None
                self.theOutput = None
            except IOException as e:
                GamerLogger.logStackTrace("Proxy", e)
            self.theClientProcess.destroy()

    myPort = int()

    def __init__(self, port, gamer):
        """ generated source for method __init__ """
        super(ProxyGamePlayer, self).__init__()
        #  Use a random gamer as our "default" gamer, that we fall back to
        #  in the event that we don't get a message from the client, or if
        #  we need to handle a simple request (START or STOP).
        self.theDefaultGamer = RandomGamer()
        self.observers = ArrayList()
        self.listener = None
        while self.listener == None:
            try:
                self.listener = ServerSocket(port)
            except Exception as ex:
                self.listener = None
                port += 1
                GamerLogger.logError("Proxy", "Failed to start gamer on port: " + (port - 1) + " trying port " + port)
        self.myPort = port
        #  Start up the socket for communicating with clients
        clientPort = 17147
        while self.clientListener == None:
            try:
                self.clientListener = ServerSocket(clientPort)
            except Exception as ex:
                self.clientListener = None
                clientPort += 1
        GamerLogger.log("Proxy", "[PROXY] Opened client communication socket on port " + clientPort + ".")
        #  Start up the first ProxyClient
        self.gamerName = gamer.getSimpleName()

    def getGamerPort(self):
        """ generated source for method getGamerPort """
        return self.myPort

    def addObserver(self, observer):
        """ generated source for method addObserver """
        self.observers.add(observer)

    def notifyObservers(self, event):
        """ generated source for method notifyObservers """
        for observer in observers:
            observer.observe(event)

    theRandomGenerator = Random()
    currentMoveCode = 0L
    receivedClientMove = False
    needRestart = False

    def run(self):
        """ generated source for method run """
        GamerConfiguration.showConfiguration()
        GamerLogger.setSpilloverLogfile("spilloverLog")
        #  Start up the client manager
        self.theClientManager = self.ClientManager(Thread.currentThread())
        self.theClientManager.start()
        #  Start up the input queue listener
        inputQueue = ArrayBlockingQueue(100)
        inputConnectionQueue = ArrayBlockingQueue(100)
        theListener = QueueListenerThread()
        theListener.start()
        while True:
            try:
                #  First, read a message from the server.
                self.notifyObservers(PlayerReceivedMessageEvent(in_))
                GamerLogger.log("Proxy", "[PROXY] Got incoming message:" + in_)
                #  Formulate a request, and see how the legal gamer responds.
                try:
                    legalProxiedResponse = request.process(receptionTime)
                except OutOfMemoryError as e:
                    #  Something went horribly wrong -- our baseline prover failed.
                    System.gc()
                    GamerLogger.logStackTrace("Proxy", e)
                    legalProxiedResponse = "SORRY"
                latestProxiedResponse = legalProxiedResponse
                GamerLogger.log("Proxy", "[PROXY] Selected fallback move:" + latestProxiedResponse)
                if not (isinstance(request, (InfoRequest, ))):
                    #  Update the move codes and prepare to send the request on to the client.
                    self.receivedClientMove = False
                    self.currentMoveCode = 1 + self.theRandomGenerator.nextLong()
                    if isinstance(request, (StopRequest, )) or isinstance(request, (AbortRequest, )):
                        self.theClientManager.expectStop = True
                    #  Send the request on to the client, along with the move code.
                    self.theClientManager.sendMessage(theMessage)
                    if not (isinstance(request, (PlayRequest, ))):
                        self.currentMoveCode = 0L
                    #  the default gamer handle it by switching move code.
                    #  Wait the appropriate amount of time for the request.
                    proxyProcessRequest(request, receptionTime)
                else:
                    self.receivedClientMove = True
                #  Get the latest response, and complain if it's the default response, or isn't a valid response.
                if not self.receivedClientMove and (isinstance(request, (PlayRequest, ))):
                    GamerLogger.logError("Proxy", "[PROXY] Did not receive any move information from client for this turn; falling back to first legal move.")
                    GamerLogger.logError("ExecutiveSummary", "Proxy did not receive any move information from client this turn: used first legal move.")
                #  Cycle the move codes again so that we will ignore any more responses
                #  that the client sends along to us.
                self.currentMoveCode = 0L
                #  And finally write the latest response out to the server.
                GamerLogger.log("Proxy", "[PROXY] Wrote outgoing message:" + out)
                HttpWriter.writeAsServer(connection, out)
                connection.close()
                self.notifyObservers(PlayerSentMessageEvent(out))
                #  Once everything is said and done, restart the client if we're
                #  due for a restart (having finished playing a game).
                if self.needRestart:
                    self.theClientManager.closeClient()
                    self.theClientManager.pleaseStop = True
                    if GamerConfiguration.runningOnLinux():
                        #  Clean up the working directory and terminate any orphan processes.
                        Thread.sleep(500)
                        GamerLogger.log("Proxy", "[PROXY] Calling cleanup scripts.")
                        try:
                            Runtime.getRuntime().exec_("./cleanup.sh").waitFor()
                        except IOException as e:
                            GamerLogger.logStackTrace("Proxy", e)
                        Thread.sleep(500)
                    self.theClientManager = self.ClientManager(Thread.currentThread())
                    self.theClientManager.start()
                    self.theDefaultGamer = RandomGamer()
                    GdlPool.drainPool()
                    SymbolPool.drainPool()
                    GamerLogger.log("Proxy", "[PROXY] Before collection, using " + usedMemoryInMegs + "mb of memory as proxy.")
                    while i < 10:
                        System.gc()
                        Thread.sleep(100)
                        i += 1
                    usedMemory = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory()
                    usedMemoryInMegs = usedMemory / 1024.0 / 1024.0
                    GamerLogger.log("Proxy", "[PROXY] After collection, using a non-transient " + usedMemoryInMegs + "mb of memory as proxy.")
                    print "Cleaned up completed match, with a residual " + usedMemoryInMegs + "mb of memory as proxy."
                    self.needRestart = False
            except Exception as e:
                GamerLogger.logStackTrace("Proxy", e)
                self.notifyObservers(PlayerDroppedPacketEvent())
            except Error as e:
                GamerLogger.logStackTrace("Proxy", e)
                self.notifyObservers(PlayerDroppedPacketEvent())

    METAGAME_BUFFER = Gamer.PREFERRED_METAGAME_BUFFER + 100
    PLAY_BUFFER = Gamer.PREFERRED_PLAY_BUFFER + 100

    def proxyProcessRequest(self, theRequest, receptionTime):
        """ generated source for method proxyProcessRequest """
        startSleeping = System.currentTimeMillis()
        timeToFinish = receptionTime
        timeToSleep = 0L
        try:
            if isinstance(theRequest, (PlayRequest, )):
                if self.theDefaultGamer.getMatch() != None:
                    timeToFinish = receptionTime + self.theDefaultGamer.getMatch().getPlayClock() * 1000 - self.PLAY_BUFFER
                else:
                    timeToFinish = System.currentTimeMillis()
                timeToSleep = timeToFinish - System.currentTimeMillis()
                if timeToSleep > 0:
                    Thread.sleep(timeToSleep)
            elif isinstance(theRequest, (StartRequest, )):
                GamerLogger.startFileLogging(self.theDefaultGamer.getMatch(), self.theDefaultGamer.getRoleName().__str__())
                print "Started playing " + self.theDefaultGamer.getMatch().getMatchId() + "."
                timeToFinish = receptionTime + self.theDefaultGamer.getMatch().getStartClock() * 1000 - self.METAGAME_BUFFER
                timeToSleep = timeToFinish - System.currentTimeMillis()
                if timeToSleep > 0:
                    Thread.sleep(timeToSleep)
            elif isinstance(theRequest, (StopRequest, )) or isinstance(theRequest, (AbortRequest, )):
                GamerLogger.stopFileLogging()
                self.needRestart = True
        except InterruptedException as ie:
            GamerLogger.log("Proxy", "[PROXY] Got woken up by final move!")
        GamerLogger.log("Proxy", "[PROXY] Proxy slept for " + (System.currentTimeMillis() - startSleeping) + ", and woke up " + (System.currentTimeMillis() - timeToFinish) + "ms late (started " + (startSleeping - receptionTime) + "ms after receiving message).")

    latestProxiedResponse = str()

    def processClientResponse(self, in_, toWakeUp):
        """ generated source for method processClientResponse """
        theirTag = in_.theMessage.substring(0, 5)
        theirMessage = in_.theMessage.substring(5)
        if not (in_.messageCode == self.currentMoveCode):
            if self.currentMoveCode > 0:
                GamerLogger.logError("Proxy", "CODE MISMATCH: " + self.currentMoveCode + " vs " + in_.messageCode)
            return
        if theirTag == "WORK:":
            self.latestProxiedResponse = theirMessage
            GamerLogger.log("Proxy", "[PROXY] Got latest working move: " + self.latestProxiedResponse)
            self.receivedClientMove = True
        elif theirTag == "DONE:":
            self.latestProxiedResponse = theirMessage
            GamerLogger.log("Proxy", "[PROXY] Got a final move: " + self.latestProxiedResponse)
            self.receivedClientMove = True
            self.currentMoveCode = 0L
            toWakeUp.interrupt()

    inputQueue = BlockingQueue()
    inputConnectionQueue = BlockingQueue()

    class QueueListenerThread(Thread):
        """ generated source for class QueueListenerThread """
        def run(self):
            """ generated source for method run """
            while True:
                try:
                    if self.inputQueue.remainingCapacity() > 0:
                        self.inputQueue.add(ProxyMessage(in_, 0L, receptionTime))
                        self.inputConnectionQueue.add(connection)
                        GamerLogger.log("Proxy", "[PROXY QueueListener] Got incoming message from game server: " + in_ + ". Added to queue in position " + len(self.inputQueue) + ".")
                    else:
                        GamerLogger.logError("Proxy", "[PROXY QueueListener] Got incoming message from game server: " + in_ + ". Could not add to queue, because queue is full!")
                except Exception as e:
                    GamerLogger.logStackTrace("Proxy", e)
                except Error as e:
                    GamerLogger.logStackTrace("Proxy", e)

