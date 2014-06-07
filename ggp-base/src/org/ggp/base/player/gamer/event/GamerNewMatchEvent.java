package org.ggp.base.player.gamer.event

import org.ggp.base.util.gdl.grammar.GdlConstant
import org.ggp.base.util.match.Match
import org.ggp.base.util.observer.Event

class GamerNewMatchEvent(Event):


    match = Match()
    roleName = GdlConstant()

    def GamerNewMatchEvent(match=Match(), GdlConstant roleName)
	
        self.match = match
        self.roleName = roleName

    def Match getMatch()
	
        return match

    def GdlConstant getRoleName()
	
        return roleName

