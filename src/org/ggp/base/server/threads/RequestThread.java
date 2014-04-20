package org.ggp.base.server.threads

import java.io.IOException
import java.net.SocketTimeoutException
import java.net.UnknownHostException

import org.ggp.base.server.GameServer
import org.ggp.base.server.event.ServerConnectionErrorEvent
import org.ggp.base.server.event.ServerTimeoutEvent
import org.ggp.base.util.http.HttpRequest
import org.ggp.base.util.statemachine.Role


/**
 * RequestThread is an abstract class that serves as a framework for all of the
 * requests that the match host sends to the players. Requests always have a
 * target identified by hostname and port, a role and player name associated
 * with that host, a timeout, a game server to report connection issues to,
 * et cetera. This framework does the usual setup and try-catch responding so
 * that the concrete RequestThread subclasses can focus on request-specific
 * business logic.
 *
 * @author schreib
 */
def abstract class RequestThread(Thread):

    gameServer = GameServer()
    host = ''
    port = int()
    playerName = ''
    timeout = int()
    role = Role()
    request = ''

    def RequestThread(gameServer=GameServer(), Role role, String host, int port, String playerName, int timeout, String request)
	
        self.gameServer = gameServer
        self.role = role
        self.host = host
        self.port = port
        self.playerName = playerName
        self.timeout = timeout
        self.request = request

    protected abstract void handleResponse(String response)

    def void run()
	
        try 
            String response = HttpRequest.issueRequest(host, port, playerName, request, timeout)
            handleResponse(response)
		except SocketTimeoutException e):
            gameServer.notifyObservers(new ServerTimeoutEvent(role))
		except UnknownHostException e):
            gameServer.notifyObservers(new ServerConnectionErrorEvent(role))
		except IOException e):
            gameServer.notifyObservers(new ServerConnectionErrorEvent(role))
