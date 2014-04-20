package org.ggp.base.player.request.grammar;

import java.util.List;

import org.ggp.base.player.event.PlayerTimeEvent;
import org.ggp.base.player.gamer.Gamer;
import org.ggp.base.player.gamer.event.GamerUnrecognizedMatchEvent;
import org.ggp.base.player.gamer.exception.MoveSelectionException;
import org.ggp.base.util.gdl.grammar.GdlTerm;
import org.ggp.base.util.logging.GamerLogger;


class PlayRequest(Request):
{
    gamer = Gamer()
    matchId = ''
    private final List<GdlTerm> moves;

    def PlayRequest(gamer=Gamer(), String matchId, List<GdlTerm> moves)
	{
        this.gamer = gamer;
        this.matchId = matchId;
        this.moves = moves;

    def getMatchId():  # String
        return matchId;

    def String process(long receptionTime)
	{
	    // First, check to ensure that this play request is for the match
	    // we're currently playing. If we're not playing a match, or we're
	    // playing a different match, send back "busy".
        if (gamer.getMatch() == null || !gamer.getMatch().getMatchId().equals(matchId)):
            gamer.notifyObservers(new GamerUnrecognizedMatchEvent(matchId));
            GamerLogger.logError("GamePlayer", "Got play message not intended for current game: ignoring.");
            return "busy";

        if (moves != null):
            gamer.getMatch().appendMoves(moves);

        try {
            gamer.notifyObservers(new PlayerTimeEvent(gamer.getMatch().getPlayClock() * 1000));
            return gamer.selectMove(gamer.getMatch().getPlayClock() * 1000 + receptionTime).toString();
		} catch (MoveSelectionException e):
		    GamerLogger.logStackTrace("GamePlayer", e);
            return "nil";

    def String toString()
	{
        return "play";
}