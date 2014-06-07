#!/usr/bin/env python
""" generated source for module HumanTimeoutEvent """
# package: org.ggp.base.player.gamer.statemachine.human.event
import org.ggp.base.player.gamer.statemachine.human.HumanGamer

import org.ggp.base.util.observer.Event

class HumanTimeoutEvent(Event):
    """ generated source for class HumanTimeoutEvent """
    humanPlayer = HumanGamer()

    def __init__(self, humanPlayer):
        """ generated source for method __init__ """
        super(HumanTimeoutEvent, self).__init__()
        self.humanPlayer = humanPlayer

    def getHumanPlayer(self):
        """ generated source for method getHumanPlayer """
        return self.humanPlayer

