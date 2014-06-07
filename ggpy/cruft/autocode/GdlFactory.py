#!/usr/bin/env python
""" generated source for module GdlFactory """
# package: org.ggp.base.util.gdl.factory
from symbol.grammar import Symbol, SymbolList, SymbolAtom

class GdlFactory(object):
    """ generated source for class GdlFactory """
    @classmethod
    def create(cls, string):
        """ generated source for method create """
        return cls.create(SymbolFactory.create(string))

    @classmethod
    def create_0(cls, symbol):
        """ generated source for method create_0 """
        try:
            return createGdl(symbol)
        except Exception as e:
            createGdl(symbol)
            raise GdlFormatException(symbol)

    @classmethod
    def createConstant(cls, atom):
        """ generated source for method createConstant """
        return GdlPool.getConstant(atom.getValue())

    @classmethod
    def createDistinct(cls, list_):
        """ generated source for method createDistinct """
        arg1 = createTerm(list_.get(1))
        arg2 = createTerm(list_.get(2))
        return GdlPool.getDistinct(arg1, arg2)

    @classmethod
    def createFunction(cls, list_):
        """ generated source for method createFunction """
        name = cls.createConstant(list_.get(0))
        body = ArrayList()
        i = 1
        while i < len(list_):
            body.add(createTerm(list_.get(i)))
            i += 1
        return GdlPool.getFunction(name, body)

    @classmethod
    def createGdl(cls, symbol):
        """ generated source for method createGdl """
        if isinstance(symbol, (SymbolList, )):
            if type_.getValue() == "<=":
                return createRule(list_)
        return createSentence(symbol)

    @classmethod
    def createLiteral(cls, symbol):
        """ generated source for method createLiteral """
        if isinstance(symbol, (SymbolList, )):
            if type_.getValue().lower() == "distinct":
                return cls.createDistinct(list_)
            elif type_.getValue().lower() == "not":
                return createNot(list_)
            elif type_.getValue().lower() == "or":
                return createOr(list_)
        return createSentence(symbol)

    @classmethod
    def createNot(cls, list_):
        """ generated source for method createNot """
        return GdlPool.getNot(cls.createLiteral(list_.get(1)))

    @classmethod
    def createOr(cls, list_):
        """ generated source for method createOr """
        disjuncts = ArrayList()
        i = 1
        while i < len(list_):
            disjuncts.add(cls.createLiteral(list_.get(i)))
            i += 1
        return GdlPool.getOr(disjuncts)

    @classmethod
    def createProposition(cls, atom):
        """ generated source for method createProposition """
        return GdlPool.getProposition(cls.createConstant(atom))

    @classmethod
    def createRelation(cls, list_):
        """ generated source for method createRelation """
        name = cls.createConstant(list_.get(0))
        body = ArrayList()
        i = 1
        while i < len(list_):
            body.add(createTerm(list_.get(i)))
            i += 1
        return GdlPool.getRelation(name, body)

    @classmethod
    def createRule(cls, list_):
        """ generated source for method createRule """
        head = createSentence(list_.get(1))
        body = ArrayList()
        i = 2
        while i < len(list_):
            body.add(cls.createLiteral(list_.get(i)))
            i += 1
        return GdlPool.getRule(head, body)

    @classmethod
    def createSentence(cls, symbol):
        """ generated source for method createSentence """
        if isinstance(symbol, (SymbolAtom, )):
            return cls.createProposition(symbol)
        else:
            return cls.createRelation(symbol)

    @classmethod
    @overloaded
    def createTerm(cls, string):
        """ generated source for method createTerm """
        return cls.createTerm(SymbolFactory.create(string))

    @classmethod
    @createTerm.register(object, Symbol)
    def createTerm_0(cls, symbol):
        """ generated source for method createTerm_0 """
        if isinstance(symbol, (SymbolAtom, )):
            if atom.getValue().charAt(0) == '?':
                return createVariable(atom)
            else:
                return cls.createConstant(atom)
        else:
            return cls.createFunction(symbol)

    @classmethod
    def createVariable(cls, atom):
        """ generated source for method createVariable """
        return GdlPool.getVariable(atom.getValue())

