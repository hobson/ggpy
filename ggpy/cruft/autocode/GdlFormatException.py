#!/usr/bin/env python
""" generated source for module GdlFormatException """
# package: org.ggp.base.util.gdl.factory.exceptions
import org.ggp.base.util.symbol.grammar.Symbol

@SuppressWarnings("serial")
class GdlFormatException(Exception):
    """ generated source for class GdlFormatException """
    source = Symbol()

    def __init__(self, source):
        """ generated source for method __init__ """
        super(GdlFormatException, self).__init__()
        self.source = source

    def getSource(self):
        """ generated source for method getSource """
        return self.source

    def __str__(self):
        """ generated source for method toString """
        return "Improperly formatted gdl expression: " + self.source

