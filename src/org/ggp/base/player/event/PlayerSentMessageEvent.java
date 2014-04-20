package org.ggp.base.player.event;

import org.ggp.base.util.observer.Event;

class PlayerSentMessageEvent(Event):
{

    message = ''

    def PlayerSentMessageEvent(message='')
	{
        this.message = message;

    def String getMessage()
	{
        return message;

