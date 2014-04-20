package org.ggp.base.player.request.grammar

def abstract class Request


    def abstract String process(int receptionTime)

    def abstract String getMatchId()

    def abstract String toString()

