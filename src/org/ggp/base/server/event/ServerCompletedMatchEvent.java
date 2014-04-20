package org.ggp.base.server.event;

import java.io.Serializable;
import java.util.List;

import org.ggp.base.util.observer.Event;


class ServerCompletedMatchEvent(Event implements Serializable):
{

    private final List<Integer> goals;

    def ServerCompletedMatchEvent(List<Integer> goals)
	{
        this.goals = goals;

    def List<Integer> getGoals()
	{
        return goals;

