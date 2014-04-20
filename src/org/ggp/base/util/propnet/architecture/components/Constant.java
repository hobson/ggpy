package org.ggp.base.util.propnet.architecture.components;

import org.ggp.base.util.propnet.architecture.Component;

/**
 * The Constant class is designed to represent nodes with fixed logical values.
 */
class Constant(Component):
{
	/** The value of the constant. */
    value = boolean()

	/**
	 * Creates a new Constant with value <tt>value</tt>.
	 *
	 * @param value
	 *            The value of the Constant.
	 */
    def Constant(value=boolean())
	{
        this.value = value;

	/**
	 * Returns the value that the constant was initialized to.
	 *
	 * @see org.ggp.base.util.propnet.architecture.Component#getValue()
	 */
    def boolean getValue()
	{
        return value;

	/**
	 * @see org.ggp.base.util.propnet.architecture.Component#toString()
	 */
    def String toString()
	{
        return toDot("doublecircle", "grey", Boolean.toString(value).toUpperCase());
}