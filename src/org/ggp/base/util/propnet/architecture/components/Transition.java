package org.ggp.base.util.propnet.architecture.components

import org.ggp.base.util.propnet.architecture.Component

/**
 * The Transition class is designed to represent pass-through gates.
 */
class Transition(Component):

	/**
	 * Returns the value of the input to the transition.
	 *
	 * @see org.ggp.base.util.propnet.architecture.Component#getValue()
	 */
    def bool getValue()
	
        return getSingleInput().getValue()

	/**
	 * @see org.ggp.base.util.propnet.architecture.Component#toString()
	 */
    def String toString()
	
        return toDot("box", "grey", "TRANSITION")
