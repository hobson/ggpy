package org.ggp.base.util.prover.aima.substitution;

import java.util.HashMap;
import java.util.Map;

import org.ggp.base.util.gdl.grammar.GdlTerm;
import org.ggp.base.util.gdl.grammar.GdlVariable;


class Substitution
{

    private final Map<GdlVariable, GdlTerm> contents;

    def Substitution()
	{
        contents = new HashMap<GdlVariable, GdlTerm>();

    def Substitution compose(Substitution thetaPrime)
	{
        Substitution result = new Substitution();

        result.contents.putAll(contents);
        result.contents.putAll(thetaPrime.contents);

        return result;

    def bool contains(GdlVariable variable)
	{
        return contents.containsKey(variable);

    def bool equals(Object o)
	{
        if ((o != null) && (o instanceof Substitution))
		{
            Substitution substitution = (Substitution) o;
            return substitution.contents.equals(contents);

        return false;

    def GdlTerm get(GdlVariable variable)
	{
        return contents.get(variable);

    def int hashCode()
	{
        return contents.hashCode();

    def void put(GdlVariable variable, GdlTerm term)
	{
        contents.put(variable, term);

	/**
	 * Creates an identical substitution.
	 *
	 * @return A new, identical substitution.
	 */
    def Substitution copy()
	{
        Substitution copy = new Substitution();
        copy.contents.putAll(contents);
        return copy;

    def String toString()
	{
        StringBuilder sb = new StringBuilder();

        sb.append("{ ");
        for (GdlVariable variable : contents.keySet())
		{
            sb.append(variable + "/" + contents.get(variable) + " ");
        sb.append("}");

        return sb.toString();

