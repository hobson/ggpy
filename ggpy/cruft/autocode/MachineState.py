#!/usr/bin/env python
""" generated source for module MachineState """
# package: org.ggp.base.util.statemachine
import java.util.HashSet

import java.util.Set

import org.ggp.base.util.gdl.grammar.GdlSentence

class MachineState(object):
    """ generated source for class MachineState """
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        self.contents = None

    # 
    #      * want to do more advanced things can subclass this implementation, but for
    #      * many cases this will do exactly what we want.
    #      
    contents = Set()

    @__init__.register(object, Set)
    def __init___0(self, contents):
        """ generated source for method __init___0 """
        self.contents = contents

    # 
    #      * getContents returns the GDL sentences which determine the current state
    #      * of the game being played. Two given states with identical GDL sentences
    #      * should be identical states of the game.
    #      
    def getContents(self):
        """ generated source for method getContents """
        return self.contents

    def clone(self):
        """ generated source for method clone """
        return MachineState(HashSet(self.contents))

    #  Utility methods 
    def hashCode(self):
        """ generated source for method hashCode """
        return self.getContents().hashCode()

    def __str__(self):
        """ generated source for method toString """
        contents = self.getContents()
        if contents == None:
            return "(MachineState with null contents)"
        else:
            return contents.__str__()

    def equals(self, o):
        """ generated source for method equals """
        if (o != None) and (isinstance(o, (MachineState, ))):
            return state.getContents() == self.getContents()
        return False

MachineState.#      * Starts with a simple implementation of a MachineState. StateMachines that

