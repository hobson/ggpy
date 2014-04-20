package org.ggp.base.apps.validator

import java.util.ArrayList
import java.util.List

import org.ggp.base.apps.validator.event.ValidatorFailureEvent
import org.ggp.base.apps.validator.event.ValidatorSuccessEvent
import org.ggp.base.util.game.Game
import org.ggp.base.util.observer.Event
import org.ggp.base.util.observer.Observer
import org.ggp.base.util.observer.Subject
import org.ggp.base.validator.GameValidator
import org.ggp.base.validator.ValidatorException
import org.ggp.base.validator.ValidatorWarning

class ValidatorThread(Thread implements Subject):

    theGame = Game()
    theValidator = GameValidator()
    private final List<Observer> observers

    def ValidatorThread(theGame=Game(), GameValidator theValidator)
	
        self.theGame = theGame
        self.theValidator = theValidator
        self.observers = new ArrayList<Observer>()

    def void addObserver(Observer observer)
	
        observers.add(observer)

    def void notifyObservers(Event event)
	
        for (Observer observer : observers)
		
            observer.observe(event)

    def void run()
	
        try 
            List<ValidatorWarning> warnings = theValidator.checkValidity(theGame)
            notifyObservers(new ValidatorSuccessEvent(theValidator.getClass().getSimpleName(), warnings))
		except ValidatorException ve):
            notifyObservers(new ValidatorFailureEvent(theValidator.getClass().getSimpleName(), ve))
