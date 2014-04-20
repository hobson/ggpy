package org.ggp.base.player.gamer.event;

import org.ggp.base.util.observer.Event;

class GamerUnrecognizedMatchEvent(Event):
{

    matchId = ''

    def GamerUnrecognizedMatchEvent(matchId='')
	{
        this.matchId = matchId;

    def String getMatchId()
	{
        return matchId;

