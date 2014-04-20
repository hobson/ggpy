package org.ggp.base.player.request.grammar;

import java.util.List;

import org.ggp.base.player.gamer.Gamer;
import org.ggp.base.player.gamer.event.GamerCompletedMatchEvent;
import org.ggp.base.player.gamer.event.GamerUnrecognizedMatchEvent;
import org.ggp.base.player.gamer.exception.StoppingException;
import org.ggp.base.util.gdl.grammar.GdlTerm;
import org.ggp.base.util.logging.GamerLogger;

class StopRequest(Request):
{
    gamer = Gamer()
    matchId = ''
    private final List<GdlTerm> moves;

    def StopRequest(gamer=Gamer(), String matchId, List<GdlTerm> moves)
	{
        this.gamer = gamer;
        this.matchId = matchId;
        this.moves = moves;

    def getMatchId():  # String
        return matchId;

    def String process(int receptionTime)
	{
        // First, check to ensure that this stop request is for the match
        // we're currently playing. If we're not playing a match, or we're
        // playing a different match, send back "busy".
        if (gamer.getMatch() == null || !gamer.getMatch().getMatchId().equals(matchId))
		{
		    GamerLogger.logError("GamePlayer", "Got stop message not intended for current game: ignoring.");
            gamer.notifyObservers(new GamerUnrecognizedMatchEvent(matchId));
            return "busy";

		//TODO: Add goal values
        if(moves != null):
            gamer.getMatch().appendMoves(moves);
        gamer.getMatch().markCompleted(null);
        gamer.notifyObservers(new GamerCompletedMatchEvent());
        try {
            gamer.stop();
		} catch (StoppingException e):
		    GamerLogger.logStackTrace("GamePlayer", e);

		// Once the match has ended, set 'roleName' and 'match'
		// to NULL to indicate that we're ready to begin a new match.
        gamer.setRoleName(null);
	    gamer.setMatch(null);

        return "done";

    def String toString()
	{
        return "stop";
}