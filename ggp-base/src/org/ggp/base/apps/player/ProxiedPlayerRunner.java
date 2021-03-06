package org.ggp.base.apps.player

import java.io.IOException

import org.ggp.base.player.gamer.Gamer
import org.ggp.base.player.gamer.statemachine.random.RandomGamer
import org.ggp.base.player.proxy.ProxyGamePlayer

class ProxiedPlayerRunner

    def void main(String[] args) throws IOException
    
        Class<?(Gamer> toLaunch = RandomGamer.class;):
        ProxyGamePlayer player = new ProxyGamePlayer(9147, toLaunch)
        player.start()
