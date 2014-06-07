package org.ggp.base.util.presence

import java.util.ArrayList
import java.util.List

import org.ggp.base.util.symbol.factory.SymbolFactory
import org.ggp.base.util.symbol.factory.exceptions.SymbolFormatException
import org.ggp.base.util.symbol.grammar.Symbol
import org.ggp.base.util.symbol.grammar.SymbolAtom
import org.ggp.base.util.symbol.grammar.SymbolList
import org.ggp.base.util.symbol.grammar.SymbolPool

/**
 * Wherein we poorly reinvent JSON, so that we can keep INFO responses
 * consistent with the Symbol-based KIF format that the other GGP protocol
 * messages are in.
 *
 * @author schreib
 */

class InfoResponse(object):
    name = String()
    status = String()
    species = String()

    def InfoResponse():
		

    def void setName(String name):
        self.name = name

    def void setStatus(String status):
        self.status = status

    def void setSpecies(String species):
        self.species = species

    def getName():  # String
        return name

    def getStatus():  # String
        return status

    def getSpecies():  # String
        return species

    def InfoResponse(symbol=Symbol()):
        if (symbol instanceof SymbolList):
            SymbolList pairs = (SymbolList)symbol
            for (int i = 0; i < pairs.size(); i++):
                Symbol pairSymbol = pairs.get(i)
                if (pairSymbol instanceof SymbolList):
                    SymbolList pair = (SymbolList)pairSymbol
                    if (pair.size() < 2) continue
                    String key = pair.get(0).toString().toLowerCase()
                    String value = ""
                    for (int j = 1; j < pair.size(); j++):
                        value += pair.get(j).toString()
                    if (key.equals("name")):
                        name = value
					elif (key.equals("status")):
                        status = value
					elif (key.equals("species")):
                        species = value
		elif (symbol instanceof SymbolAtom):
            status = ((SymbolAtom) symbol).getValue()

    def static InfoResponse create(String original):
        try 
            return new InfoResponse(SymbolFactory.create(original))
		except SymbolFormatException e):
            return new InfoResponse()

    private Symbol getKeyValueSymbol(String key, String value):
        Symbol keySymbol = SymbolPool.getAtom(key)
        Symbol valueSymbol = SymbolPool.getAtom(value)
        return SymbolPool.getList(new Symbol[] keySymbol, valueSymbol} )

    def toSymbol():  # Symbol
        List<Symbol> infoList = new ArrayList<Symbol>()
        if (name != null):
            infoList.add(getKeyValueSymbol("name", name))
        if (status != null):
            infoList.add(getKeyValueSymbol("status", status))
        if (species != null):
            infoList.add(getKeyValueSymbol("species", species))
        return SymbolPool.getList(infoList)
