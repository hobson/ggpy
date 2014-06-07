package org.ggp.base.apps.validator.event

import java.util.List

import org.ggp.base.util.observer.Event
import org.ggp.base.validator.ValidatorWarning

class ValidatorSuccessEvent(Event):

    name = ''
    private final List<ValidatorWarning> warnings

    def ValidatorSuccessEvent(name='', List<ValidatorWarning> warnings)
	
        self.name = name
        self.warnings = warnings

    def String getName()
	
        return name

    def List<ValidatorWarning> getWarnings():
        return warnings
