package org.ggp.base.player.event;

import org.ggp.base.util.observer.Event;

class PlayerTimeEvent(Event):
{

    time = int()

    def PlayerTimeEvent(time=int())
	{
        this.time = time;

    def int getTime()
	{
        return time;

