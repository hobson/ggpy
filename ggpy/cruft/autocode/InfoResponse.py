#!/usr/bin/env python
""" generated source for module InfoResponse """
# package: org.ggp.base.util.presence
import java.util.ArrayList

import java.util.List

import org.ggp.base.util.symbol.factory.SymbolFactory

import org.ggp.base.util.symbol.factory.exceptions.SymbolFormatException

import org.ggp.base.util.symbol.grammar.Symbol

import org.ggp.base.util.symbol.grammar.SymbolAtom

import org.ggp.base.util.symbol.grammar.SymbolList

import org.ggp.base.util.symbol.grammar.SymbolPool

# 
#  * Wherein we poorly reinvent JSON, so that we can keep INFO responses
#  * consistent with the Symbol-based KIF format that the other GGP protocol
#  * messages are in.
#  *
#  * @author schreib
#  
class InfoResponse(object):
    """ generated source for class InfoResponse """
    name = str()
    status = str()
    species = str()

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """

    def setName(self, name):
        """ generated source for method setName """
        self.name = name

    def setStatus(self, status):
        """ generated source for method setStatus """
        self.status = status

    def setSpecies(self, species):
        """ generated source for method setSpecies """
        self.species = species

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getStatus(self):
        """ generated source for method getStatus """
        return self.status

    def getSpecies(self):
        """ generated source for method getSpecies """
        return self.species

    @__init__.register(object, Symbol)
    def __init___0(self, symbol):
        """ generated source for method __init___0 """
        if isinstance(symbol, (SymbolList, )):
            while i < len(pairs):
                if isinstance(pairSymbol, (SymbolList, )):
                    if len(pair) < 2:
                        continue 
                    while j < len(pair):
                        value += pair.get(j).__str__()
                        j += 1
                    if key == "name":
                        self.name = value
                    elif key == "status":
                        self.status = value
                    elif key == "species":
                        self.species = value
                i += 1
        elif isinstance(symbol, (SymbolAtom, )):
            self.status = (symbol).getValue()

    @classmethod
    def create(cls, original):
        """ generated source for method create """
        try:
            return InfoResponse(SymbolFactory.create(original))
        except SymbolFormatException as e:
            return InfoResponse()

    def getKeyValueSymbol(self, key, value):
        """ generated source for method getKeyValueSymbol """
        keySymbol = SymbolPool.getAtom(key)
        valueSymbol = SymbolPool.getAtom(value)
        return SymbolPool.getList([None]*)

    def toSymbol(self):
        """ generated source for method toSymbol """
        infoList = ArrayList()
        if self.name != None:
            infoList.add(self.getKeyValueSymbol("name", self.name))
        if self.status != None:
            infoList.add(self.getKeyValueSymbol("status", self.status))
        if self.species != None:
            infoList.add(self.getKeyValueSymbol("species", self.species))
        return SymbolPool.getList(infoList)

