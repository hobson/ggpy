#!/usr/bin/env python
""" generated source for module GoalDefinitionException """
# package: org.ggp.base.util.statemachine.exceptions
import org.ggp.base.util.statemachine.MachineState

import org.ggp.base.util.statemachine.Role

@SuppressWarnings("serial")
class GoalDefinitionException(Exception):
    """ generated source for class GoalDefinitionException """
    role = Role()
    state = MachineState()

    def __init__(self, state, role):
        """ generated source for method __init__ """
        super(GoalDefinitionException, self).__init__()
        self.state = state
        self.role = role

    def getRole(self):
        """ generated source for method getRole """
        return self.role

    def getState(self):
        """ generated source for method getState """
        return self.state

    def __str__(self):
        """ generated source for method toString """
        return "Goal is poorly defined for " + self.role + " in " + self.state

