#!/usr/bin/env python
""" generated source for module PlayRequest """
# package: org.ggp.base.player.request.grammar
import java.util.List

import org.ggp.base.player.event.PlayerTimeEvent

import org.ggp.base.player.gamer.Gamer

import org.ggp.base.player.gamer.event.GamerUnrecognizedMatchEvent

import org.ggp.base.player.gamer.exception.MoveSelectionException

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.logging.GamerLogger

class PlayRequest(Request):
    """ generated source for class PlayRequest """
    gamer = Gamer()
    matchId = str()
    moves = List()

    def __init__(self, gamer, matchId, moves):
        """ generated source for method __init__ """
        super(PlayRequest, self).__init__()
        self.gamer = gamer
        self.matchId = matchId
        self.moves = moves

    def getMatchId(self):
        """ generated source for method getMatchId """
        return self.matchId

    def process(self, receptionTime):
        """ generated source for method process """
        #  First, check to ensure that this play request is for the match
        #  we're currently playing. If we're not playing a match, or we're
        #  playing a different match, send back "busy".
        if self.gamer.getMatch() == None or not self.gamer.getMatch().getMatchId() == self.matchId:
            self.gamer.notifyObservers(GamerUnrecognizedMatchEvent(self.matchId))
            GamerLogger.logError("GamePlayer", "Got play message not intended for current game: ignoring.")
            return "busy"
        if self.moves != None:
            self.gamer.getMatch().appendMoves(self.moves)
        try:
            self.gamer.notifyObservers(PlayerTimeEvent(self.gamer.getMatch().getPlayClock() * 1000))
            return self.gamer.selectMove(self.gamer.getMatch().getPlayClock() * 1000 + receptionTime).__str__()
        except MoveSelectionException as e:
            GamerLogger.logStackTrace("GamePlayer", e)
            return "nil"

    def __str__(self):
        """ generated source for method toString """
        return "play"

