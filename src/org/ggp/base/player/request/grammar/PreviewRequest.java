package org.ggp.base.player.request.grammar

import org.ggp.base.player.gamer.Gamer
import org.ggp.base.player.gamer.exception.GamePreviewException
import org.ggp.base.util.game.Game
import org.ggp.base.util.logging.GamerLogger

class PreviewRequest(Request):

    game = Game()
    gamer = Gamer()
    previewClock = int()

    def PreviewRequest(gamer=Gamer(), Game theGame, int previewClock)
	
        self.gamer = gamer
        self.game = theGame
        self.previewClock = previewClock

    def getMatchId():  # String
        return null

    def String process(int receptionTime)
	
		// Ensure that we aren't already playing a match. If we are,
	    // ignore the message, saying that we're busy.
        if (gamer.getMatch() != null):
            GamerLogger.logError("GamePlayer", "Got preview message while already busy playing a game: ignoring.")
            //gamer.notifyObservers(new GamerUnrecognizedMatchEvent(matchId))
            return "busy"

		// Otherwise, if we're not busy, have the gamer start previewing.
        try 
			//gamer.notifyObservers(new PlayerTimeEvent(gamer.getMatch().getStartClock() * 1000))
            gamer.preview(game, previewClock * 1000 + receptionTime)
			//gamer.metaGame(gamer.getMatch().getStartClock() * 1000 + receptionTime)
		except GamePreviewException e):
		    GamerLogger.logStackTrace("GamePlayer", e)

		    // Upon encountering an uncaught exception during previewing,
		    // assume that indicates that we aren't actually able to play
		    // right now, and tell the server that we're busy.
            return "busy"

        return "ready"

    def String toString()
	
        return "start"
