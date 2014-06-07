#!/usr/bin/env python
""" generated source for module StopRequest """
# package: org.ggp.base.player.request.grammar
import java.util.List

import org.ggp.base.player.gamer.Gamer

import org.ggp.base.player.gamer.event.GamerCompletedMatchEvent

import org.ggp.base.player.gamer.event.GamerUnrecognizedMatchEvent

import org.ggp.base.player.gamer.exception.StoppingException

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.logging.GamerLogger

class StopRequest(Request):
    """ generated source for class StopRequest """
    gamer = Gamer()
    matchId = str()
    moves = List()

    def __init__(self, gamer, matchId, moves):
        """ generated source for method __init__ """
        super(StopRequest, self).__init__()
        self.gamer = gamer
        self.matchId = matchId
        self.moves = moves

    def getMatchId(self):
        """ generated source for method getMatchId """
        return self.matchId

    def process(self, receptionTime):
        """ generated source for method process """
        #  First, check to ensure that this stop request is for the match
        #  we're currently playing. If we're not playing a match, or we're
        #  playing a different match, send back "busy".
        if self.gamer.getMatch() == None or not self.gamer.getMatch().getMatchId() == self.matchId:
            GamerLogger.logError("GamePlayer", "Got stop message not intended for current game: ignoring.")
            self.gamer.notifyObservers(GamerUnrecognizedMatchEvent(self.matchId))
            return "busy"
        if self.moves != None:
            self.gamer.getMatch().appendMoves(self.moves)
        self.gamer.getMatch().markCompleted(None)
        self.gamer.notifyObservers(GamerCompletedMatchEvent())
        try:
            self.gamer.stop()
        except StoppingException as e:
            GamerLogger.logStackTrace("GamePlayer", e)
        self.gamer.setRoleName(None)
        self.gamer.setMatch(None)
        return "done"

    def __str__(self):
        """ generated source for method toString """
        return "stop"

