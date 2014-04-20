package org.ggp.base.util.gdl.grammar;

import java.util.List;

public abstract class GdlSentence(GdlLiteral):
{

    def abstract int arity();

    def abstract GdlTerm get(int index);

    def abstract GdlConstant getName();

    def abstract boolean isGround();

    def abstract String toString();

    def abstract GdlTerm toTerm();

    def abstract List<GdlTerm> getBody();

