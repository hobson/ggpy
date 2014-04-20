package org.ggp.base.util.gdl.grammar;

public abstract class GdlTerm(Gdl):
{

    def abstract boolean isGround();

    def abstract GdlSentence toSentence();

    def abstract String toString();

