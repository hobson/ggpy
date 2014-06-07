#!/usr/bin/env python
""" generated source for module Not """
# package: org.ggp.base.util.propnet.architecture.components
import org.ggp.base.util.propnet.architecture.Component

# 
#  * The Not class is designed to represent logical NOT gates.
#  
@SuppressWarnings("serial")
class Not(Component):
    """ generated source for class Not """
    # 
    # 	 * Returns the inverse of the input to the not.
    # 	 *
    # 	 * @see org.ggp.base.util.propnet.architecture.Component#getValue()
    # 	 
    def getValue(self):
        """ generated source for method getValue """
        return not getSingleInput().getValue()

    # 
    # 	 * @see org.ggp.base.util.propnet.architecture.Component#toString()
    # 	 
    def __str__(self):
        """ generated source for method toString """
        return toDot("invtriangle", "grey", "NOT")

