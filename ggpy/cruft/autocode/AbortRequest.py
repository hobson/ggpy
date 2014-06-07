#!/usr/bin/env python
""" generated source for module AbortRequest """
# package: org.ggp.base.player.request.grammar
import org.ggp.base.player.gamer.Gamer

import org.ggp.base.player.gamer.event.GamerAbortedMatchEvent

import org.ggp.base.player.gamer.event.GamerUnrecognizedMatchEvent

import org.ggp.base.player.gamer.exception.AbortingException

import org.ggp.base.util.logging.GamerLogger

class AbortRequest(Request):
    """ generated source for class AbortRequest """
    gamer = Gamer()
    matchId = str()

    def __init__(self, gamer, matchId):
        """ generated source for method __init__ """
        super(AbortRequest, self).__init__()
        self.gamer = gamer
        self.matchId = matchId

    def getMatchId(self):
        """ generated source for method getMatchId """
        return self.matchId

    def process(self, receptionTime):
        """ generated source for method process """
        #  First, check to ensure that this abort request is for the match
        #  we're currently playing. If we're not playing a match, or we're
        #  playing a different match, send back "busy".
        if self.gamer.getMatch() == None or not self.gamer.getMatch().getMatchId() == self.matchId:
            GamerLogger.logError("GamePlayer", "Got abort message not intended for current game: ignoring.")
            self.gamer.notifyObservers(GamerUnrecognizedMatchEvent(self.matchId))
            return "busy"
        self.gamer.getMatch().markAborted()
        self.gamer.notifyObservers(GamerAbortedMatchEvent())
        try:
            self.gamer.abort()
        except AbortingException as e:
            GamerLogger.logStackTrace("GamePlayer", e)
        self.gamer.setRoleName(None)
        self.gamer.setMatch(None)
        return "aborted"

    def __str__(self):
        """ generated source for method toString """
        return "abort"

