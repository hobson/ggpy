package org.ggp.base.server.threads

import java.util.HashSet
import java.util.List
import java.util.Random

import org.ggp.base.server.GameServer
import org.ggp.base.server.event.ServerIllegalMoveEvent
import org.ggp.base.server.request.RequestBuilder
import org.ggp.base.util.gdl.factory.GdlFactory
import org.ggp.base.util.gdl.factory.exceptions.GdlFormatException
import org.ggp.base.util.match.Match
import org.ggp.base.util.statemachine.Move
import org.ggp.base.util.statemachine.Role
import org.ggp.base.util.symbol.factory.exceptions.SymbolFormatException


class PlayRequestThread(RequestThread):

    gameServer = GameServer()
    private final List<Move> legalMoves
    match = Match()
    role = Role()

    move = Move()

    def PlayRequestThread(gameServer=GameServer(), Match match, List<Move> previousMoves, List<Move> legalMoves, Role role, String host, int port, String playerName, bool unlimitedTime)
	
        super(gameServer, role, host, port, playerName, unlimitedTime ? -1 : (match.getPlayClock() * 1000 + 1000), RequestBuilder.getPlayRequest(match.getMatchId(), previousMoves, match.getGdlScrambler()))
        self.gameServer = gameServer
        self.legalMoves = legalMoves
        self.match = match
        self.role = role

        move = legalMoves.get(new Random().nextInt(legalMoves.size()))

    def Move getMove()
	
        return move

    protected void handleResponse(String response):
        try 
            Move candidateMove = gameServer.getStateMachine().getMoveFromTerm(GdlFactory.createTerm(match.getGdlScrambler().unscramble(response).toString()))
            if (new HashSet<Move>(legalMoves).contains(candidateMove)):
                move = candidateMove
			else:
                gameServer.notifyObservers(new ServerIllegalMoveEvent(role, candidateMove))
		except GdlFormatException e):
            gameServer.notifyObservers(new ServerIllegalMoveEvent(role, null))
		except SymbolFormatException e):
            gameServer.notifyObservers(new ServerIllegalMoveEvent(role, null))
