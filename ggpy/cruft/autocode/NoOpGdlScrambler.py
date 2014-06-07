#!/usr/bin/env python
""" generated source for module NoOpGdlScrambler """
# package: org.ggp.base.util.gdl.scrambler
import org.ggp.base.util.gdl.factory.GdlFactory

import org.ggp.base.util.gdl.factory.exceptions.GdlFormatException

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.symbol.factory.exceptions.SymbolFormatException

class NoOpGdlScrambler(GdlScrambler):
    """ generated source for class NoOpGdlScrambler """
    def scramble(self, x):
        """ generated source for method scramble """
        return x.__str__()

    def unscramble(self, x):
        """ generated source for method unscramble """
        return GdlFactory.create(x)

    def scrambles(self):
        """ generated source for method scrambles """
        return False

