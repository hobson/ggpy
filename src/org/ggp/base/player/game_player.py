#!/usr/bin/env python

import socket



class Socket:
    '''from python.org docs
    
    demonstration class only -- coded for clarity, not efficiency
    '''

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == '':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return ''.join(chunks)

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        '''Attach an observer to this subject so it's methods are called when required

        in Sam's java this is `Subject.addObserver()`'''
        if not observer in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        '''Dettach an observer from this subject so it's methods are no longer called when the Subject is updated

        in Sam's java there is no `Subject.removeObserver()`'''
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        '''Notify observers of a change in state

        in Sam's java this is `Subject.notifyObserver()`'''
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Gamer(Subject):
    """ 
    The Gamer class defines methods for both meta-gaming and move selection in a
    pre-specified amount of time. The Gamer class is based on the <i>algorithm</i>
    design pattern.
    """
    match = Match()
    roleName = GdlConstant()

    def __init__(self):
        """ generated source for method __init__ """
        super(Gamer, self).__init__()
        observers = ArrayList()
        #  When not playing a match, the variables 'match'
        #  and 'roleName' should be NULL. This indicates that
        #  the player is available for starting a new match.
        self.match = None
        self.roleName = None

    #  The following values are recommendations to the implementations
    #    * for the minimum length of time to leave between the stated timeout
    #    * and when you actually return from metaGame and selectMove. They are
    #    * stored here so they can be shared amongst all Gamers. 
    PREFERRED_METAGAME_BUFFER = 3900
    PREFERRED_PLAY_BUFFER = 1900

    #  ==== The Gaming Algorithms ====
    def metaGame(self, timeout):
        """ generated source for method metaGame """

    def selectMove(self, timeout):
        """ generated source for method selectMove """

    #  Note that the match's goal values will not necessarily be known when
    #    * stop() is called, as we only know the final set of moves and haven't
    #    * interpreted them yet. To get the final goal values, process the final
    #    * moves of the game.
    #    
    def stop(self):
        """ generated source for method stop """

    #  Cleanly stop playing the match
    def abort(self):
        """ generated source for method abort """

    #  Abruptly stop playing the match
    def preview(self, g, timeout):
        """ generated source for method preview """

    #  Preview a game
    #  ==== Gamer Profile and Configuration ====
    def getName(self):
        """ generated source for method getName """

    def getSpecies(self):
        """ generated source for method getSpecies """
        return None

    def isComputerPlayer(self):
        """ generated source for method isComputerPlayer """
        return True

    def getConfigPanel(self):
        """ generated source for method getConfigPanel """
        return EmptyConfigPanel()

    def getDetailPanel(self):
        """ generated source for method getDetailPanel """
        return EmptyDetailPanel()

    #  ==== Accessors ====
    def getMatch(self):
        """ generated source for method getMatch """
        return self.match

    def setMatch(self, match):
        """ generated source for method setMatch """
        self.match = match

    def getRoleName(self):
        """ generated source for method getRoleName """
        return self.roleName

    def setRoleName(self, roleName):
        """ generated source for method setRoleName """
        self.roleName = roleName


class GamePlayer(Thread, Subject):
    '''A game-playing `threading.Thread` that listens to a `player.Subject`

    The `player.Subject` is associated with a match/game this GamePlayer is playing.
    '''
    port = int()
    gamer = Gamer()
    listener = ServerSocket()
    observers = List()

    def __init__(self, port, gamer):
        """ generated source for method __init__ """
        super(GamePlayer, self).__init__()
        self.observers = ArrayList()
        self.listener = None
        while self.listener == None:
            try:
                self.listener = ServerSocket(port)
            except IOException as ex:
                self.listener = None
                port += 1
                System.err.println("Failed to start gamer on port: " + (port - 1) + " trying port " + port)
        self.port = port
        self.gamer = gamer

    def getGamerPort(self):
        """ generated source for method getGamerPort """
        return self.port

    def getGamer(self):
        """ generated source for method getGamer """
        return self.gamer

    def run(self):
        """ generated source for method run """
        while not isInterrupted():
            try:
                if 0 == len(in_):
                    raise IOException("Empty message received.")
                self.notifyObservers(PlayerReceivedMessageEvent(in_))
                GamerLogger.log("GamePlayer", "[Received at " + System.currentTimeMillis() + "] " + in_, GamerLogger.LOG_LEVEL_DATA_DUMP)
                HttpWriter.writeAsServer(connection, out)
                connection.close()
                self.notifyObservers(PlayerSentMessageEvent(out))
                GamerLogger.log("GamePlayer", "[Sent at " + System.currentTimeMillis() + "] " + out, GamerLogger.LOG_LEVEL_DATA_DUMP)
            except Exception as e:
                self.notifyObservers(PlayerDroppedPacketEvent())

    #  Simple main function that starts a RandomGamer on a specified port.
    #  It might make sense to factor this out into a separate app sometime,
    #  so that the GamePlayer class doesn't have to import RandomGamer.
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        if len(args):
            System.err.println("Usage: GamePlayer <port>")
            System.exit(1)
        try:
            player.run()
        except NumberFormatException as e:
            System.err.println("Illegal port number: " + args[0])
            e.printStackTrace()
            System.exit(2)
        except IOException as e:
            System.err.println("IO Exception: " + e)
            e.printStackTrace()
            System.exit(3)


if __name__ == '__main__':
    import sys
    GamePlayer.main(sys.argv)

