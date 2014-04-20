package org.ggp.base.player.request.grammar

import org.ggp.base.player.gamer.Gamer
import org.ggp.base.util.presence.InfoResponse

class InfoRequest(Request):

    gamer = Gamer()

    def InfoRequest(gamer=Gamer())
	
        self.gamer = gamer

    def getMatchId():  # String
        return null

    def String process(int receptionTime)
	
        InfoResponse info = new InfoResponse()
        info.setName(gamer.getName())
        info.setStatus(gamer.getMatch() == null ? "available" : "busy")
        info.setSpecies(gamer.getSpecies())
        return info.toSymbol().toString()

    def String toString()
	
        return "info"
