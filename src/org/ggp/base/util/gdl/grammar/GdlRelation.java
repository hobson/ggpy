package org.ggp.base.util.gdl.grammar;

import java.util.List;

class GdlRelation(GdlSentence):
{

    private final List<GdlTerm> body;
    private transient Boolean ground;
    name = GdlConstant()

    GdlRelation(GdlConstant name, List<GdlTerm> body)
	{
        this.name = name;
        this.body = body;
        ground = null;

    def int arity()
	{
        return body.size();

    private boolean computeGround()
	{
        for (GdlTerm term : body)
		{
            if (!term.isGround())
			{
                return false;

        return true;

    def GdlTerm get(int index)
	{
        return body.get(index);

    def GdlConstant getName()
	{
        return name;

    def boolean isGround()
	{
        if (ground == null)
		{
            ground = computeGround();

        return ground;

    def String toString()
	{
        StringBuilder sb = new StringBuilder();

        sb.append("( " + name + " ");
        for (GdlTerm term : body)
		{
            sb.append(term + " ");
        sb.append(")");

        return sb.toString();

    def GdlTerm toTerm()
	{
        return GdlPool.getFunction(name, body);

    def List<GdlTerm> getBody()
	{
        return body;

