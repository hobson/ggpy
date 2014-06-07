#!/usr/bin/env python
""" generated source for module And """
# package: org.ggp.base.util.propnet.architecture.components
import org.ggp.base.util.propnet.architecture.Component

# 
#  * The And class is designed to represent logical AND gates.
#  
@SuppressWarnings("serial")
class And(Component):
    """ generated source for class And """
    # 
    # 	 * Returns true if and only if every input to the and is true.
    # 	 *
    # 	 * @see org.ggp.base.util.propnet.architecture.Component#getValue()
    # 	 
    def getValue(self):
        """ generated source for method getValue """
        for component in getInputs():
            if not component.getValue():
                return False
        return True

    # 
    # 	 * @see org.ggp.base.util.propnet.architecture.Component#toString()
    # 	 
    def __str__(self):
        """ generated source for method toString """
        return toDot("invhouse", "grey", "AND")

