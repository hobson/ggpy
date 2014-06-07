#!/usr/bin/env python
""" generated source for module SymbolFormatException """
# package: org.ggp.base.util.symbol.factory.exceptions
@SuppressWarnings("serial")
class SymbolFormatException(Exception):
    """ generated source for class SymbolFormatException """
    source = str()

    def __init__(self, source):
        """ generated source for method __init__ """
        super(SymbolFormatException, self).__init__()
        self.source = source

    def getSource(self):
        """ generated source for method getSource """
        return self.source

    def __str__(self):
        """ generated source for method toString """
        return "Improperly formatted symbolic expression: " + self.source

