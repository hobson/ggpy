#!/usr/bin/env python
""" generated source for module Proposition """
# package: org.ggp.base.util.propnet.architecture.components
import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.propnet.architecture.Component

# 
#  * The Proposition class is designed to represent named latches.
#  
@SuppressWarnings("serial")
class Proposition(Component):
    """ generated source for class Proposition """
    name = GdlSentence()
    value = bool()

    # 
    # 	 * Creates a new Proposition with name <tt>name</tt>.
    # 	 *
    # 	 * @param name
    # 	 
    def __init__(self, name):
        """ generated source for method __init__ """
        super(Proposition, self).__init__()
        self.name = name
        self.value = False

    # 
    # 	 * Getter method.
    # 	 *
    # 	 
    def getName(self):
        """ generated source for method getName """
        return self.name

    # 
    #      * Setter method.
    #      *
    #      * This should only be rarely used; the name of a proposition
    #      * is usually constant over its entire lifetime.
    #      *
    #      
    def setName(self, newName):
        """ generated source for method setName """
        self.name = newName

    # 
    # 	 *
    # 	 * @see org.ggp.base.util.propnet.architecture.Component#getValue()
    # 	 
    def getValue(self):
        """ generated source for method getValue """
        return self.value

    # 
    # 	 * Setter method.
    # 	 *
    # 	 * @param value
    # 	 
    def setValue(self, value):
        """ generated source for method setValue """
        self.value = value

    # 
    # 	 * @see org.ggp.base.util.propnet.architecture.Component#toString()
    # 	 
    def __str__(self):
        """ generated source for method toString """
        return toDot("circle", "red" if self.value else "white", self.name.__str__())

Proposition.#  The name of the Proposition. 

Proposition.#  The value of the Proposition. 

Proposition.# 	 *            The name of the Proposition.

Proposition.# 	 * @return The name of the Proposition.

Proposition.#      * @return The name of the Proposition.

Proposition.# 	 * Returns the current value of the Proposition.

Proposition.# 	 *            The new value of the Proposition.

