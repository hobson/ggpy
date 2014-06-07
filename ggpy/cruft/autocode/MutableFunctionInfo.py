#!/usr/bin/env python
""" generated source for module MutableFunctionInfo """
# package: org.ggp.base.util.gdl.model.assignments
import java.util.ArrayList

import java.util.Collection

import java.util.Collections

import java.util.List

import java.util.Map

import java.util.Set

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.gdl.model.SentenceForm

import com.google.common.collect.ImmutableList

import com.google.common.collect.ImmutableMap

import com.google.common.collect.ImmutableSet

import com.google.common.collect.Lists

import com.google.common.collect.Maps

# 
#  * Defines a {@link FunctionInfo} that can have values added to it (but
#  * not removed from it) over time. This allows the functional
#  * info to stay correct as new values are added with minimal
#  * additional computation.
#  *
#  * Not thread-safe.
#  
class MutableFunctionInfo(AddibleFunctionInfo):
    """ generated source for class MutableFunctionInfo """
    form = SentenceForm()
    dependentSlots = ArrayList()
    valueMaps = Lists.newArrayList()

    def __init__(self, form):
        """ generated source for method __init__ """
        super(MutableFunctionInfo, self).__init__()
        self.form = form
        i = 0
        while i < form.getTupleSize():
            self.dependentSlots.add(True)
            self.valueMaps.add(Maps.newHashMap())
            i += 1

    @classmethod
    @overloaded
    def create(cls, form):
        """ generated source for method create """
        return cls.create(form, ImmutableSet.of())

    @classmethod
    @create.register(object, SentenceForm, Collection)
    def create_0(cls, form, initialSentences):
        """ generated source for method create_0 """
        functionInfo = MutableFunctionInfo(form)
        for sentence in initialSentences:
            functionInfo.addTuple(GdlUtils.getTupleFromGroundSentence(sentence))
        return functionInfo

    def getSentenceForm(self):
        """ generated source for method getSentenceForm """
        return self.form

    def addTuple(self, sentenceTuple):
        """ generated source for method addTuple """
        if len(sentenceTuple) != self.form.getTupleSize():
            raise IllegalArgumentException()
        # For each slot...
        i = 0
        while i < len(sentenceTuple):
            if self.dependentSlots.get(i):
                # Either add to that entry, or invalidate the slot
                lookupTuple.remove(i)
                if curValue == None:
                    # Just add to the map
                    valueMap.put(ImmutableList.copyOf(lookupTuple), newValue)
                else:
                    # If this isn't the existing sentence, invalidate this slot
                    if curValue != newValue:
                        self.dependentSlots.set(i, False)
                        self.valueMaps.set(i, ImmutableMap.of())
            i += 1

    def getDependentSlots(self):
        """ generated source for method getDependentSlots """
        return Collections.unmodifiableList(self.dependentSlots)

    def getProducibleVars(self, sentence):
        """ generated source for method getProducibleVars """
        return FunctionInfos.getProducibleVars(self, sentence)

    def getValueMap(self, varIndex):
        """ generated source for method getValueMap """
        return Collections.unmodifiableMap(self.valueMaps.get(varIndex))

    def addSentence(self, sentence):
        """ generated source for method addSentence """
        self.addTuple(GdlUtils.getTupleFromGroundSentence(sentence))

    def __str__(self):
        """ generated source for method toString """
        return "MutableFunctionInfo [form=" + self.form + ", dependentSlots=" + self.dependentSlots + ", valueMaps=" + self.valueMaps + "]"

