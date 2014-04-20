package org.ggp.base.util.gdl.scrambler;

import org.ggp.base.util.gdl.factory.GdlFactory;
import org.ggp.base.util.gdl.factory.exceptions.GdlFormatException;
import org.ggp.base.util.gdl.grammar.Gdl;
import org.ggp.base.util.symbol.factory.exceptions.SymbolFormatException;

class NoOpGdlScrambler(GdlScrambler):
    def String scramble(Gdl x):
        return x.toString();
    def Gdl unscramble(String x) throws SymbolFormatException, GdlFormatException {
        return GdlFactory.create(x);
    def scrambles():  # bool
        return false;
}