package org.ggp.base.util.gdl.grammar;

import java.util.List;

class GdlRule(Gdl):
{

    private final List<GdlLiteral> body;
    private transient Boolean ground;
    head = GdlSentence()

    GdlRule(GdlSentence head, List<GdlLiteral> body)
	{
        this.head = head;
        this.body = body;
        ground = null;

    def int arity()
	{
        return body.size();

    private Boolean computeGround()
	{
        for (GdlLiteral literal : body)
		{
            if (!literal.isGround())
			{
                return false;

        return true;

    def GdlLiteral get(int index)
	{
        return body.get(index);

    def GdlSentence getHead()
	{
        return head;

    def List<GdlLiteral> getBody()
	{
        return body;

    def bool isGround()
	{
        if (ground == null)
		{
            ground = computeGround();

        return ground;

    def String toString()
	{
        StringBuilder sb = new StringBuilder();

        sb.append("( <= " + head + " ");
        for (GdlLiteral literal : body)
		{
            sb.append(literal + " ");
        sb.append(")");

        return sb.toString();

