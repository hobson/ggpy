package org.ggp.base.player.request.grammar

import org.ggp.base.player.gamer.Gamer
import org.ggp.base.player.gamer.event.GamerAbortedMatchEvent
import org.ggp.base.player.gamer.event.GamerUnrecognizedMatchEvent
import org.ggp.base.player.gamer.exception.AbortingException
import org.ggp.base.util.logging.GamerLogger

class AbortRequest(Request):

    gamer = Gamer()
    matchId = ''

    def AbortRequest(gamer=Gamer(), String matchId)
	
        self.gamer = gamer
        self.matchId = matchId

    def getMatchId():  # String
        return matchId

    def String process(int receptionTime)
	
        // First, check to ensure that this abort request is for the match
        // we're currently playing. If we're not playing a match, or we're
        // playing a different match, send back "busy".
        if (gamer.getMatch() == null || !gamer.getMatch().getMatchId().equals(matchId))
		
		    GamerLogger.logError("GamePlayer", "Got abort message not intended for current game: ignoring.")
            gamer.notifyObservers(new GamerUnrecognizedMatchEvent(matchId))
            return "busy"

		// Mark the match as aborted and notify observers
        gamer.getMatch().markAborted()
        gamer.notifyObservers(new GamerAbortedMatchEvent())
        try 
            gamer.abort()
		except AbortingException e):
		    GamerLogger.logStackTrace("GamePlayer", e)

		// Once the match has ended, set 'roleName' and 'match'
		// to NULL to indicate that we're ready to begin a new match.
        gamer.setRoleName(null)
	    gamer.setMatch(null)

        return "aborted"

    def String toString()
	
        return "abort"
