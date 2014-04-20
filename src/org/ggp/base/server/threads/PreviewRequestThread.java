package org.ggp.base.server.threads;

import org.ggp.base.server.GameServer;
import org.ggp.base.server.request.RequestBuilder;
import org.ggp.base.util.match.Match;
import org.ggp.base.util.statemachine.Role;


class PreviewRequestThread(RequestThread):
{
    def PreviewRequestThread(gameServer=GameServer(), Match match, Role role, String host, int port, String playerName)
	{
        super(gameServer, role, host, port, playerName, match.getPreviewClock() * 1000, RequestBuilder.getPreviewRequest(match.getGame().getRules(), match.getPreviewClock(), match.getGdlScrambler()));

    protected void handleResponse(String response):
		;
}