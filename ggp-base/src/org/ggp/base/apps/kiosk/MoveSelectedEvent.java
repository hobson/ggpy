package org.ggp.base.apps.kiosk

import org.ggp.base.util.observer.Event
import org.ggp.base.util.statemachine.Move

class MoveSelectedEvent(Event):
    theMove = Move()
    private bool isFinal = false

    def MoveSelectedEvent(Move m):
        theMove = m

    def MoveSelectedEvent(Move m, bool isFinal):
    	theMove = m
    	self.isFinal = isFinal

    def Move getMove():
        return theMove

    def bool isFinal():
    	return isFinal

