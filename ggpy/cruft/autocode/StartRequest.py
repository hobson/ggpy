#!/usr/bin/env python
""" generated source for module StartRequest """
# package: org.ggp.base.player.request.grammar
import org.ggp.base.player.event.PlayerTimeEvent

import org.ggp.base.player.gamer.Gamer

import org.ggp.base.player.gamer.event.GamerNewMatchEvent

import org.ggp.base.player.gamer.event.GamerUnrecognizedMatchEvent

import org.ggp.base.player.gamer.exception.MetaGamingException

import org.ggp.base.util.game.Game

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.logging.GamerLogger

import org.ggp.base.util.match.Match

class StartRequest(Request):
    """ generated source for class StartRequest """
    game = Game()
    gamer = Gamer()
    matchId = str()
    playClock = int()
    roleName = GdlConstant()
    startClock = int()

    def __init__(self, gamer, matchId, roleName, theGame, startClock, playClock):
        """ generated source for method __init__ """
        super(StartRequest, self).__init__()
        self.gamer = gamer
        self.matchId = matchId
        self.roleName = roleName
        self.game = theGame
        self.startClock = startClock
        self.playClock = playClock

    def getMatchId(self):
        """ generated source for method getMatchId """
        return self.matchId

    def process(self, receptionTime):
        """ generated source for method process """
        #  Ensure that we aren't already playing a match. If we are,
        #  ignore the message, saying that we're busy.
        if self.gamer.getMatch() != None:
            GamerLogger.logError("GamePlayer", "Got start message while already busy playing a game: ignoring.")
            self.gamer.notifyObservers(GamerUnrecognizedMatchEvent(self.matchId))
            return "busy"
        #  Create the new match, and handle all of the associated logistics
        #  in the gamer to indicate that we're starting a new match.
        match = Match(self.matchId, -1, self.startClock, self.playClock, self.game)
        self.gamer.setMatch(match)
        self.gamer.setRoleName(self.roleName)
        self.gamer.notifyObservers(GamerNewMatchEvent(match, self.roleName))
        #  Finally, have the gamer begin metagaming.
        try:
            self.gamer.notifyObservers(PlayerTimeEvent(self.gamer.getMatch().getStartClock() * 1000))
            self.gamer.metaGame(self.gamer.getMatch().getStartClock() * 1000 + receptionTime)
        except MetaGamingException as e:
            GamerLogger.logStackTrace("GamePlayer", e)
            #  Upon encountering an uncaught exception during metagaming,
            #  assume that indicates that we aren't actually able to play
            #  right now, and tell the server that we're busy.
            self.gamer.setMatch(None)
            self.gamer.setRoleName(None)
            return "busy"
        return "ready"

    def __str__(self):
        """ generated source for method toString """
        return "start"

