#!/usr/bin/env python
""" generated source for module SymbolFactory """
# package: org.ggp.base.util.symbol.factory
import java.util.ArrayList

import java.util.LinkedList

import java.util.List

import org.ggp.base.util.symbol.factory.exceptions.SymbolFormatException

import org.ggp.base.util.symbol.grammar.Symbol

import org.ggp.base.util.symbol.grammar.SymbolAtom

import org.ggp.base.util.symbol.grammar.SymbolList

import org.ggp.base.util.symbol.grammar.SymbolPool

class SymbolFactory(object):
    """ generated source for class SymbolFactory """
    @classmethod
    def create(cls, string):
        """ generated source for method create """
        try:
            return convert(LinkedList(tokens))
        except Exception as e:
            raise SymbolFormatException(string)

    #  Private, implementation-specific methods below here 
    @classmethod
    def convert(cls, tokens):
        """ generated source for method convert """
        if tokens.getFirst() == "(":
            return convertList(tokens)
        else:
            return convertAtom(tokens)

    @classmethod
    def convertAtom(cls, tokens):
        """ generated source for method convertAtom """
        return SymbolPool.getAtom(tokens.removeFirst())

    @classmethod
    def convertList(cls, tokens):
        """ generated source for method convertList """
        contents = ArrayList()
        tokens.removeFirst()
        while not tokens.getFirst() == ""):
            contents.add(cls.convert(tokens))
        tokens.removeFirst()
        return SymbolPool.getList(contents)

    @classmethod
    def lex(cls, string):
        """ generated source for method lex """
        tokens = ArrayList()
        for token in string.split(" "):
            tokens.add(token)
        return tokens

    @classmethod
    def preprocess(cls, string):
        """ generated source for method preprocess """
        string = string.replaceAll("\\(", " ( ")
        string = string.replaceAll("\\)", " ) ")
        string = string.replaceAll("\\s+", " ")
        string = string.trim()
        return string

