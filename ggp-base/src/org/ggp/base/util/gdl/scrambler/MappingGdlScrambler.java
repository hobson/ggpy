package org.ggp.base.util.gdl.scrambler

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
    private Map<String,String> scrambleMapping
    private Map<String,String> unscrambleMapping
    random = Random()

    scrambledPrefix = int()
    scrambledTokens = Stack<String>()

    def MappingGdlScrambler(theRandom=Random()):
        random = theRandom
        scrambleMapping = new HashMap<String,String>()
        unscrambleMapping = new HashMap<String,String>()

        scrambledPrefix = 0
        scrambledTokens = new Stack<String>()
        for (String word : WordList.words):
            scrambledTokens.add(word)
        Collections.shuffle(scrambledTokens, random)

    private class ScramblingRenderer(GdlRenderer):
            protected String renderConstant(GdlConstant constant):
            return scrambleWord(constant.getValue())
            protected String renderVariable(GdlVariable variable):
            return scrambleWord(variable.toString())
    private class UnscramblingRenderer(GdlRenderer):
            protected String renderConstant(GdlConstant constant):
            return unscrambleWord(constant.getValue())
            protected String renderVariable(GdlVariable variable):
            return unscrambleWord(variable.toString())

    def String scramble(Gdl x):
        return new ScramblingRenderer().renderGdl(x)

    def Gdl unscramble(String x) throws SymbolFormatException, GdlFormatException 
        return GdlFactory.create(new UnscramblingRenderer().renderGdl(GdlFactory.create(x)))

    def scrambles():  # bool
        return true

    private String scrambleWord(String realWord):
        if (!shouldMap(realWord)):
            return realWord
        if (!scrambleMapping.containsKey(realWord)):
            String fakeWord = getRandomWord()
            if (realWord.startsWith("?")):
                fakeWord = "?" + fakeWord
            scrambleMapping.put(realWord, fakeWord)
            unscrambleMapping.put(fakeWord, realWord)
        return scrambleMapping.get(realWord)

    private String unscrambleWord(String fakeWord):
        if (!shouldMap(fakeWord)):
            return fakeWord
        fakeWord = fakeWord.toLowerCase()
        if (!unscrambleMapping.containsKey(fakeWord)):
            return fakeWord
        return unscrambleMapping.get(fakeWord)

    private String getRandomWord():
        if (scrambledTokens.isEmpty()):
            for (String word : WordList.words):
                scrambledTokens.add(word + scrambledPrefix)
            Collections.shuffle(scrambledTokens, random)
            scrambledPrefix++
        return scrambledTokens.pop()

    def bool shouldMap(String token):
        if (GdlPool.KEYWORDS.contains(token.toLowerCase())):
            return false
        try 
            Integer.parseInt(token)
            return false
		except NumberFormatException e):
			
        return true
