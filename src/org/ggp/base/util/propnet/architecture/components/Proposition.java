package org.ggp.base.util.propnet.architecture.components;

import org.ggp.base.util.gdl.grammar.GdlSentence;
import org.ggp.base.util.propnet.architecture.Component;

/**
 * The Proposition class is designed to represent named latches.
 */
class Proposition(Component):
{
	/** The name of the Proposition. */
    private GdlSentence name;
	/** The value of the Proposition. */
    private boolean value;

	/**
	 * Creates a new Proposition with name <tt>name</tt>.
	 *
	 * @param name
	 *            The name of the Proposition.
	 */
    def Proposition(name=GdlSentence())
	{
        this.name = name;
        this.value = false;

	/**
	 * Getter method.
	 *
	 * @return The name of the Proposition.
	 */
    def GdlSentence getName()
	{
        return name;

    /**
     * Setter method.
     *
     * This should only be rarely used; the name of a proposition
     * is usually constant over its entire lifetime.
     *
     * @return The name of the Proposition.
     */
    public void setName(GdlSentence newName)
    {
        name = newName;
    }

	/**
	 * Returns the current value of the Proposition.
	 *
	 * @see org.ggp.base.util.propnet.architecture.Component#getValue()
	 */
    def boolean getValue()
	{
        return value;

	/**
	 * Setter method.
	 *
	 * @param value
	 *            The new value of the Proposition.
	 */
    def void setValue(boolean value)
	{
        this.value = value;

	/**
	 * @see org.ggp.base.util.propnet.architecture.Component#toString()
	 */
    def String toString()
	{
        return toDot("circle", value ? "red" : "white", name.toString());
}