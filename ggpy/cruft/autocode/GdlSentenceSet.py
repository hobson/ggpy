#!/usr/bin/env python
""" generated source for module GdlSentenceSet """
# package: org.ggp.base.util.reasoner.gdl
import java.util.Collections

import java.util.Map

import java.util.Map.Entry

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.model.SentenceForm

import org.ggp.base.util.gdl.model.assignments.AddibleFunctionInfo

import org.ggp.base.util.gdl.model.assignments.MutableFunctionInfo

import com.google.common.collect.HashMultimap

import com.google.common.collect.Maps

import com.google.common.collect.Multimap

import com.google.common.collect.Multimaps

import com.google.common.collect.SetMultimap

# 
#  * Contains a set of GdlSentences arranged by SentenceForm and the
#  * associated FunctionInfo for each SentenceForm. The FunctionInfos
#  * are continually and automatically maintained as sentences are
#  * added to the set.
#  *
#  * Note that this class is not thread-safe.
#  
class GdlSentenceSet(object):
    """ generated source for class GdlSentenceSet """
    sentences = SetMultimap()
    functionInfoMap = Map()

    def __init__(self):
        """ generated source for method __init__ """
        self.sentences = HashMultimap.create()
        self.functionInfoMap = Maps.newHashMap()

    @classmethod
    @overloaded
    def create(cls):
        """ generated source for method create """
        return GdlSentenceSet()

    @classmethod
    @create.register(object, Multimap)
    def create_0(cls, sentences):
        """ generated source for method create_0 """
        result = cls.create()
        result.putAll(sentences)
        return result

    # 
    # 	 * Returns an unmodifiable view of the sentences in this set.
    # 	 * Note that this view may change if the collection is concurrently
    # 	 * modified.
    # 	 
    def getSentences(self):
        """ generated source for method getSentences """
        return Multimaps.unmodifiableSetMultimap(self.sentences)

    # 
    # 	 * Returns true iff the given sentence is in this set of sentences.
    # 	 
    def containsSentence(self, form, sentence):
        """ generated source for method containsSentence """
        return self.sentences.containsEntry(form, sentence)

    def putAll(self, newSentences):
        """ generated source for method putAll """
        for entry in newSentences.entries():
            put(entry.getKey(), entry.getValue())

    def put(self, form, sentence):
        """ generated source for method put """
        if not self.containsSentence(form, sentence):
            self.sentences.put(form, sentence)
            if not self.functionInfoMap.containsKey(form):
                self.functionInfoMap.put(form, MutableFunctionInfo.create(form))
            self.functionInfoMap.get(form).addSentence(sentence)

    # 
    # 	 * Returns an unmodifiable view of the function information
    # 	 
    def getFunctionInfo(self):
        """ generated source for method getFunctionInfo """
        return Collections.unmodifiableMap(self.functionInfoMap)

