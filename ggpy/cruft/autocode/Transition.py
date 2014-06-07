#!/usr/bin/env python
""" generated source for module Transition """
# package: org.ggp.base.util.propnet.architecture.components
import org.ggp.base.util.propnet.architecture.Component

# 
#  * The Transition class is designed to represent pass-through gates.
#  
@SuppressWarnings("serial")
class Transition(Component):
    """ generated source for class Transition """
    # 
    # 	 * Returns the value of the input to the transition.
    # 	 *
    # 	 * @see org.ggp.base.util.propnet.architecture.Component#getValue()
    # 	 
    def getValue(self):
        """ generated source for method getValue """
        return getSingleInput().getValue()

    # 
    # 	 * @see org.ggp.base.util.propnet.architecture.Component#toString()
    # 	 
    def __str__(self):
        """ generated source for method toString """
        return toDot("box", "grey", "TRANSITION")

