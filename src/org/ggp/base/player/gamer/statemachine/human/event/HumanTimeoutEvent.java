package org.ggp.base.player.gamer.statemachine.human.event;

import org.ggp.base.player.gamer.statemachine.human.HumanGamer;
import org.ggp.base.util.observer.Event;


class HumanTimeoutEvent(Event):
{

    humanPlayer = HumanGamer()

    def HumanTimeoutEvent(humanPlayer=HumanGamer())
	{
        this.humanPlayer = humanPlayer;

    def HumanGamer getHumanPlayer()
	{
        return humanPlayer;

