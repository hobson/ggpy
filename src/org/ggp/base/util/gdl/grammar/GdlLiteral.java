package org.ggp.base.util.gdl.grammar;

def abstract class GdlLiteral(Gdl):
{

    def abstract bool isGround();

    def abstract String toString();

