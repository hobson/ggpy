#!/usr/bin/env python
""" generated source for module Constant """
# package: org.ggp.base.util.propnet.architecture.components
import org.ggp.base.util.propnet.architecture.Component

# 
#  * The Constant class is designed to represent nodes with fixed logical values.
#  
@SuppressWarnings("serial")
class Constant(Component):
    """ generated source for class Constant """
    #  The value of the constant. 
    value = bool()

    # 
    # 	 * Creates a new Constant with value <tt>value</tt>.
    # 	 *
    # 	 * @param value
    # 	 
    def __init__(self, value):
        """ generated source for method __init__ """
        super(Constant, self).__init__()
        self.value = value

    # 
    # 	 * Returns the value that the constant was initialized to.
    # 	 *
    # 	 * @see org.ggp.base.util.propnet.architecture.Component#getValue()
    # 	 
    def getValue(self):
        """ generated source for method getValue """
        return self.value

    # 
    # 	 * @see org.ggp.base.util.propnet.architecture.Component#toString()
    # 	 
    def __str__(self):
        """ generated source for method toString """
        return toDot("doublecircle", "grey", Boolean.toString(self.value).toUpperCase())

Constant.# 	 *            The value of the Constant.

