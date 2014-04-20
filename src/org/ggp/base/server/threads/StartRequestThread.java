package org.ggp.base.server.threads

import org.ggp.base.server.GameServer
import org.ggp.base.server.request.RequestBuilder
import org.ggp.base.util.match.Match
import org.ggp.base.util.statemachine.Role


class StartRequestThread(RequestThread):

    def StartRequestThread(gameServer=GameServer(), Match match, Role role, String host, int port, String playerName)
	
        super(gameServer, role, host, port, playerName, match.getStartClock() * 1000, RequestBuilder.getStartRequest(match.getMatchId(), role, match.getGame().getRules(), match.getStartClock(), match.getPlayClock(), match.getGdlScrambler()))

    protected void handleResponse(String response):
		
