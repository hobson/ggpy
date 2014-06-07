package org.ggp.base.util.gdl.scrambler

import org.ggp.base.util.gdl.factory.exceptions.GdlFormatException
import org.ggp.base.util.gdl.grammar.Gdl
import org.ggp.base.util.symbol.factory.exceptions.SymbolFormatException

def interface GdlScrambler 
    def String scramble(Gdl x)
    def Gdl unscramble(String x) throws SymbolFormatException, GdlFormatException
    def bool scrambles()
