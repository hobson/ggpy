package org.ggp.base.player.event;

import org.ggp.base.util.observer.Event;

class PlayerTimeEvent(Event):
{

    time = long()

    def PlayerTimeEvent(time=long())
	{
        this.time = time;

    def long getTime()
	{
        return time;

