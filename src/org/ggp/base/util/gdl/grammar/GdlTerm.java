package org.ggp.base.util.gdl.grammar;

def abstract class GdlTerm(Gdl):
{

    def abstract bool isGround();

    def abstract GdlSentence toSentence();

    def abstract String toString();

