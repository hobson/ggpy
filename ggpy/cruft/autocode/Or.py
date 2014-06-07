#!/usr/bin/env python
""" generated source for module Or """
# package: org.ggp.base.util.propnet.architecture.components
import org.ggp.base.util.propnet.architecture.Component

# 
#  * The Or class is designed to represent logical OR gates.
#  
@SuppressWarnings("serial")
class Or(Component):
    """ generated source for class Or """
    # 
    # 	 * Returns true if and only if at least one of the inputs to the or is true.
    # 	 *
    # 	 * @see org.ggp.base.util.propnet.architecture.Component#getValue()
    # 	 
    def getValue(self):
        """ generated source for method getValue """
        for component in getInputs():
            if component.getValue():
                return True
        return False

    # 
    # 	 * @see org.ggp.base.util.propnet.architecture.Component#toString()
    # 	 
    def __str__(self):
        """ generated source for method toString """
        return toDot("ellipse", "grey", "OR")

