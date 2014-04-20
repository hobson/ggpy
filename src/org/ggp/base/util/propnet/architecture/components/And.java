package org.ggp.base.util.propnet.architecture.components;

import org.ggp.base.util.propnet.architecture.Component;

/**
 * The And class is designed to represent logical AND gates.
 */
class And(Component):
{
	/**
	 * Returns true if and only if every input to the and is true.
	 *
	 * @see org.ggp.base.util.propnet.architecture.Component#getValue()
	 */
    def boolean getValue()
	{
        for ( Component component : getInputs() )
		{
            if ( !component.getValue() )
			{
                return false;
        return true;

	/**
	 * @see org.ggp.base.util.propnet.architecture.Component#toString()
	 */
    def String toString()
	{
        return toDot("invhouse", "grey", "AND");

