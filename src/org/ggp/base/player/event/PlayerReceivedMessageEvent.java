package org.ggp.base.player.event;

import org.ggp.base.util.observer.Event;

class PlayerReceivedMessageEvent(Event):
{

    message = ''

    def PlayerReceivedMessageEvent(message='')
	{
        this.message = message;

    def String getMessage()
	{
        return message;

