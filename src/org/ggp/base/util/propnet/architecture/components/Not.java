package org.ggp.base.util.propnet.architecture.components

import org.ggp.base.util.propnet.architecture.Component

/**
 * The Not class is designed to represent logical NOT gates.
 */
class Not(Component):

	/**
	 * Returns the inverse of the input to the not.
	 *
	 * @see org.ggp.base.util.propnet.architecture.Component#getValue()
	 */
    def bool getValue()
	
        return !getSingleInput().getValue()

	/**
	 * @see org.ggp.base.util.propnet.architecture.Component#toString()
	 */
    def String toString()
	
        return toDot("invtriangle", "grey", "NOT")
