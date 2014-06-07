#!/usr/bin/env python
""" generated source for module PreviewRequest """
# package: org.ggp.base.player.request.grammar
import org.ggp.base.player.gamer.Gamer

import org.ggp.base.player.gamer.exception.GamePreviewException

import org.ggp.base.util.game.Game

import org.ggp.base.util.logging.GamerLogger

class PreviewRequest(Request):
    """ generated source for class PreviewRequest """
    game = Game()
    gamer = Gamer()
    previewClock = int()

    def __init__(self, gamer, theGame, previewClock):
        """ generated source for method __init__ """
        super(PreviewRequest, self).__init__()
        self.gamer = gamer
        self.game = theGame
        self.previewClock = previewClock

    def getMatchId(self):
        """ generated source for method getMatchId """
        return None

    def process(self, receptionTime):
        """ generated source for method process """
        #  Ensure that we aren't already playing a match. If we are,
        #  ignore the message, saying that we're busy.
        if self.gamer.getMatch() != None:
            GamerLogger.logError("GamePlayer", "Got preview message while already busy playing a game: ignoring.")
            # gamer.notifyObservers(new GamerUnrecognizedMatchEvent(matchId));
            return "busy"
        #  Otherwise, if we're not busy, have the gamer start previewing.
        try:
            # gamer.notifyObservers(new PlayerTimeEvent(gamer.getMatch().getStartClock() * 1000));
            self.gamer.preview(self.game, self.previewClock * 1000 + receptionTime)
            # gamer.metaGame(gamer.getMatch().getStartClock() * 1000 + receptionTime);
        except GamePreviewException as e:
            GamerLogger.logStackTrace("GamePlayer", e)
            #  Upon encountering an uncaught exception during previewing,
            #  assume that indicates that we aren't actually able to play
            #  right now, and tell the server that we're busy.
            return "busy"
        return "ready"

    def __str__(self):
        """ generated source for method toString """
        return "start"

