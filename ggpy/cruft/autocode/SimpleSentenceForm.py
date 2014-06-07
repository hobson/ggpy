#!/usr/bin/env python
""" generated source for module SimpleSentenceForm """
# package: org.ggp.base.util.gdl.model
import java.util.List

import java.util.Map

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlFunction

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import com.google.common.base.Preconditions

import com.google.common.collect.ImmutableMap

import com.google.common.collect.Lists

import com.google.common.collect.Maps

class SimpleSentenceForm(AbstractSentenceForm):
    """ generated source for class SimpleSentenceForm """
    name = GdlConstant()

    # The arity is the same as the arity of the GdlSentence object, i.e.
    # how many terms there are at the first level (including functions).
    arity = int()

    # We cheat a little by reusing sentence forms as function forms.
    # Map from the index (< arity) to the function definition.
    functions = ImmutableMap()

    # The tuple size is the total number of constants and/or variables
    # within the entire sentence, including inside functions.
    tupleSize = int()

    @classmethod
    @overloaded
    def create(cls, sentence):
        """ generated source for method create """
        name = sentence.__name__
        arity = sentence.arity()
        tupleSize = 0
        functions = Maps.newHashMap()
        i = 0
        while i < arity:
            if isinstance(term, (GdlFunction, )):
                functions.put(i, functionForm)
                tupleSize += functionForm.getTupleSize()
            else:
                tupleSize += 1
            i += 1
        return SimpleSentenceForm(name, arity, ImmutableMap.copyOf(functions), tupleSize)

    @classmethod
    @create.register(object, GdlFunction)
    def create_0(cls, function_):
        """ generated source for method create_0 """
        name = function_.__name__
        arity = function_.arity()
        tupleSize = 0
        functions = Maps.newHashMap()
        i = 0
        while i < arity:
            if isinstance(term, (GdlFunction, )):
                functions.put(i, functionForm)
                tupleSize += functionForm.getTupleSize()
            else:
                tupleSize += 1
            i += 1
        return SimpleSentenceForm(name, arity, ImmutableMap.copyOf(functions), tupleSize)

    def __init__(self, name, arity, functions, tupleSize):
        """ generated source for method __init__ """
        super(SimpleSentenceForm, self).__init__()
        self.name = name
        self.arity = arity
        self.functions = functions
        self.tupleSize = tupleSize

    def getName(self):
        """ generated source for method getName """
        return self.name

    def withName(self, newName):
        """ generated source for method withName """
        return SimpleSentenceForm(newName, self.arity, self.functions, self.tupleSize)

    @overloaded
    def matches(self, sentence):
        """ generated source for method matches """
        if not sentence.__name__ == self.name:
            return False
        if sentence.arity() != self.arity:
            return False
        i = 0
        while i < sentence.arity():
            if self.functions.containsKey(i) and not (isinstance(term, (GdlFunction, ))):
                return False
            elif isinstance(term, (GdlFunction, )):
                if not self.functions.containsKey(i):
                    return False
                if not functionForm.matches(function_):
                    return False
            i += 1
        return True

    @matches.register(object, GdlFunction)
    def matches_0(self, function_):
        """ generated source for method matches_0 """
        if not function_.__name__ == self.name:
            return False
        if function_.arity() != self.arity:
            return False
        i = 0
        while i < function_.arity():
            if self.functions.containsKey(i) and not (isinstance(term, (GdlFunction, ))):
                return False
            elif isinstance(term, (GdlFunction, )):
                if not self.functions.containsKey(i):
                    return False
                if not functionForm.matches(innerFunction):
                    return False
            i += 1
        return True

    def getTupleSize(self):
        """ generated source for method getTupleSize """
        return self.tupleSize

    def getSentenceFromTuple(self, tuple_):
        """ generated source for method getSentenceFromTuple """
        if len(tuple_) != self.tupleSize:
            raise IllegalArgumentException("Passed tuple of the wrong size to a sentence form: " + "tuple was " + tuple_ + ", sentence form is " + self)
        if len(tuple_) < self.arity:
            raise IllegalStateException("Something is very wrong, probably fixable by the GdlCleaner; name: " + self.name + "; arity: " + self.arity + "; tupleSize: " + self.tupleSize)
        sentenceBody = Lists.newArrayList()
        curIndex = 0
        i = 0
        while i < self.arity:
            Preconditions.checkArgument(not (isinstance(term, (GdlFunction, ))))
            if self.functions.containsKey(i):
                sentenceBody.add(functionForm.getFunctionFromTuple(tuple_, curIndex))
                curIndex += functionForm.getTupleSize()
            else:
                sentenceBody.add(term)
                curIndex += 1
            i += 1
        if self.arity == 0:
            return GdlPool.getProposition(self.name)
        else:
            return GdlPool.getRelation(self.name, sentenceBody)

    def getFunctionFromTuple(self, tuple_, curIndex):
        """ generated source for method getFunctionFromTuple """
        functionBody = Lists.newArrayList()
        i = 0
        while i < self.arity:
            Preconditions.checkArgument(not (isinstance(term, (GdlFunction, ))))
            if self.functions.containsKey(i):
                functionBody.add(functionForm.getFunctionFromTuple(tuple_, curIndex))
                curIndex += functionForm.getTupleSize()
            else:
                functionBody.add(term)
                curIndex += 1
            i += 1
        return GdlPool.getFunction(self.name, functionBody)

