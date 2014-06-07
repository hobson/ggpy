#!/usr/bin/env python
""" generated source for module GdlScrambler """
# package: org.ggp.base.util.gdl.scrambler
import org.ggp.base.util.gdl.factory.exceptions.GdlFormatException

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.symbol.factory.exceptions.SymbolFormatException

class GdlScrambler(object):
    """ generated source for interface GdlScrambler """
    __metaclass__ = ABCMeta
    @abstractmethod
    def scramble(self, x):
        """ generated source for method scramble """

    @abstractmethod
    def unscramble(self, x):
        """ generated source for method unscramble """

    @abstractmethod
    def scrambles(self):
        """ generated source for method scrambles """

