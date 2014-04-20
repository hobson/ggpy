package org.ggp.base.util.gdl.grammar;

import java.util.List;

class GdlOr(GdlLiteral):
{

    private final List<GdlLiteral> disjuncts;
    private transient Boolean ground;

    GdlOr(List<GdlLiteral> disjuncts)
	{
        this.disjuncts = disjuncts;
        ground = null;

    def int arity()
	{
        return disjuncts.size();

    private boolean computeGround()
	{
        for (GdlLiteral literal : disjuncts)
		{
            if (!literal.isGround())
			{
                return false;

        return true;

    def GdlLiteral get(int index)
	{
        return disjuncts.get(index);

    def boolean isGround()
	{
        if (ground == null)
		{
            ground = computeGround();

        return ground;

    def String toString()
	{
        StringBuilder sb = new StringBuilder();

        sb.append("( or ");
        for (GdlLiteral literal : disjuncts)
		{
            sb.append(literal + " ");
        sb.append(")");

        return sb.toString();

