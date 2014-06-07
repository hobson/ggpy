#!/usr/bin/env python
""" generated source for module MappingGdlScrambler """
# package: org.ggp.base.util.gdl.scrambler
import java.util.Collections

import java.util.HashMap

import java.util.Map

import java.util.Random

import java.util.Stack

import org.ggp.base.util.gdl.factory.GdlFactory

import org.ggp.base.util.gdl.factory.exceptions.GdlFormatException

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.symbol.factory.exceptions.SymbolFormatException

class MappingGdlScrambler(GdlScrambler):
    """ generated source for class MappingGdlScrambler """
    scrambleMapping = Map()
    unscrambleMapping = Map()
    random = Random()
    scrambledPrefix = int()
    scrambledTokens = Stack()

    def __init__(self, theRandom):
        """ generated source for method __init__ """
        super(MappingGdlScrambler, self).__init__()
        self.random = theRandom
        self.scrambleMapping = HashMap()
        self.unscrambleMapping = HashMap()
        self.scrambledPrefix = 0
        self.scrambledTokens = Stack()
        for word in WordList.words:
            self.scrambledTokens.add(word)
        Collections.shuffle(self.scrambledTokens, self.random)

    class ScramblingRenderer(GdlRenderer):
        """ generated source for class ScramblingRenderer """
        def renderConstant(self, constant):
            """ generated source for method renderConstant """
            return scrambleWord(constant.getValue())

        def renderVariable(self, variable):
            """ generated source for method renderVariable """
            return scrambleWord(variable.__str__())

    class UnscramblingRenderer(GdlRenderer):
        """ generated source for class UnscramblingRenderer """
        def renderConstant(self, constant):
            """ generated source for method renderConstant """
            return unscrambleWord(constant.getValue())

        def renderVariable(self, variable):
            """ generated source for method renderVariable """
            return unscrambleWord(variable.__str__())

    def scramble(self, x):
        """ generated source for method scramble """
        return self.ScramblingRenderer().renderGdl(x)

    def unscramble(self, x):
        """ generated source for method unscramble """
        return GdlFactory.create(self.UnscramblingRenderer().renderGdl(GdlFactory.create(x)))

    def scrambles(self):
        """ generated source for method scrambles """
        return True

    def scrambleWord(self, realWord):
        """ generated source for method scrambleWord """
        if not shouldMap(realWord):
            return realWord
        if not self.scrambleMapping.containsKey(realWord):
            if realWord.startsWith("?"):
                fakeWord = "?" + fakeWord
            self.scrambleMapping.put(realWord, fakeWord)
            self.unscrambleMapping.put(fakeWord, realWord)
        return self.scrambleMapping.get(realWord)

    def unscrambleWord(self, fakeWord):
        """ generated source for method unscrambleWord """
        if not shouldMap(fakeWord):
            return fakeWord
        fakeWord = fakeWord.lower()
        if not self.unscrambleMapping.containsKey(fakeWord):
            return fakeWord
        return self.unscrambleMapping.get(fakeWord)

    def getRandomWord(self):
        """ generated source for method getRandomWord """
        if self.scrambledTokens.isEmpty():
            for word in WordList.words:
                self.scrambledTokens.add(word + self.scrambledPrefix)
            Collections.shuffle(self.scrambledTokens, self.random)
            self.scrambledPrefix += 1
        return self.scrambledTokens.pop()

    @classmethod
    def shouldMap(cls, token):
        """ generated source for method shouldMap """
        if GdlPool.KEYWORDS.contains(token.lower()):
            return False
        try:
            Integer.parseInt(token)
            return False
        except NumberFormatException as e:
        return True

