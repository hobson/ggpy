package org.ggp.base.util.propnet.architecture.components

import org.ggp.base.util.propnet.architecture.Component

/**
 * The Or class is designed to represent logical OR gates.
 */
class Or(Component):

	/**
	 * Returns true if and only if at least one of the inputs to the or is true.
	 *
	 * @see org.ggp.base.util.propnet.architecture.Component#getValue()
	 */
    def bool getValue()
	
        for ( Component component : getInputs() )
		
            if ( component.getValue() )
			
                return true
        return false

	/**
	 * @see org.ggp.base.util.propnet.architecture.Component#toString()
	 */
    def String toString()
	
        return toDot("ellipse", "grey", "OR")
