package org.ggp.base.player.request.grammar;

public abstract class Request
{

    def abstract String process(long receptionTime);

    def abstract String getMatchId();

    def abstract String toString();

