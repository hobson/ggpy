package org.ggp.base.apps.validator.event

import org.ggp.base.util.observer.Event

class ValidatorFailureEvent(Event):

    name = ''
    exception = Exception()

    def ValidatorFailureEvent(name='', Exception exception)
	
        self.name = name
        self.exception = exception

    def String getName()
	
        return name

    def Exception getException()
	
        return exception

