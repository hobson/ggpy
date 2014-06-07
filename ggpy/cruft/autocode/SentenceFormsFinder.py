#!/usr/bin/env python
""" generated source for module SentenceFormsFinder """
from threading import RLock

_locks = {}
def lock_for_object(obj, locks=_locks):
    return locks.setdefault(id(obj), RLock())


def synchronized(call):
    def inner(*args, **kwds):
        with lock_for_object(call):
            return call(*args, **kwds)
    return inner

# package: org.ggp.base.util.gdl.model
import java.util.List

import java.util.Map

import java.util.Map.Entry

import java.util.Set

import org.ggp.base.util.concurrency.ConcurrencyUtils

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlFunction

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import com.google.common.base.Preconditions

import com.google.common.collect.ImmutableList

import com.google.common.collect.ImmutableMap

import com.google.common.collect.ImmutableSet

import com.google.common.collect.Lists

import com.google.common.collect.Maps

import com.google.common.collect.Sets

class SentenceFormsFinder(object):
    """ generated source for class SentenceFormsFinder """
    description = ImmutableList()
    sentencesModel = Maps.newHashMap()
    haveCreatedModel = False

    def __init__(self, description):
        """ generated source for method __init__ """
        self.description = description

    def findSentenceForms(self):
        """ generated source for method findSentenceForms """
        createModel()
        return ImmutableSet.copyOf(getSentenceFormsFromModel())

    def findCartesianDomains(self):
        """ generated source for method findCartesianDomains """
        createModel()
        return getCartesianDomainsFromModel()

    def createModel(self):
        """ generated source for method createModel """
        with lock_for_object(self):
            if not self.haveCreatedModel:
                addTrueSentencesToModel()
                applyRulesToModel()
                self.haveCreatedModel = True

    def getCartesianDomainsFromModel(self):
        """ generated source for method getCartesianDomainsFromModel """
        results = Maps.newHashMap()
        for sentenceEntry in sentencesModel.entrySet():
            ConcurrencyUtils.checkForInterruption()
            #  We'll end up taking the Cartesian product of the different
            #  types of terms we have available
            if nameAndArity.getArity() == 0:
                results.put(form, CartesianSentenceFormDomain.create(form, ImmutableList.of()))
            else:
                for terms in Sets.cartesianProduct(sampleTerms):
                    ConcurrencyUtils.checkForInterruption()
                    results.put(form, domain)
        return results

    def getDomain(self, form, sentence):
        """ generated source for method getDomain """
        domainContents = Lists.newArrayList()
        getDomainInternal(sentence.getBody(), self.sentencesModel.get(NameAndArity(sentence)), domainContents)
        return CartesianSentenceFormDomain.create(form, domainContents)

    # Appends to domainContents
    def getDomainInternal(self, body, bodyModel, domainContents):
        """ generated source for method getDomainInternal """
        if len(body) != len(bodyModel):
            raise IllegalStateException("Should have same arity in example as in model")
        i = 0
        while i < len(body):
            if isinstance(term, (GdlConstant, )):
                domainContents.add(termModel.getPossibleConstants())
            elif isinstance(term, (GdlFunction, )):
                self.getDomainInternal(function_.getBody(), functionBodyModel, domainContents)
            else:
                raise IllegalStateException()
            i += 1

    def getSentenceFormsFromModel(self):
        """ generated source for method getSentenceFormsFromModel """
        results = Sets.newHashSet()
        for sentenceEntry in sentencesModel.entrySet():
            #  We'll end up taking the Cartesian product of the different
            #  types of terms we have available
            if nameAndArity.getArity() == 0:
                results.add(SimpleSentenceForm.create(sentence))
            else:
                for terms in Sets.cartesianProduct(sampleTerms):
                    results.add(SimpleSentenceForm.create(sentence))
        return results

    @overloaded
    def toSampleTerms(self, bodyModels):
        """ generated source for method toSampleTerms """
        results = Lists.newArrayList()
        for termModel in bodyModels:
            results.add(self.toSampleTerms(termModel))
        return results

    @toSampleTerms.register(object, TermModel)
    def toSampleTerms_0(self, termModel):
        """ generated source for method toSampleTerms_0 """
        results = Sets.newHashSet()
        if not termModel.getPossibleConstants().isEmpty():
            results.add(termModel.getPossibleConstants().iterator().next())
        for nameAndArity in termModel.getPossibleFunctions().keySet():
            for functionBody in functionBodies:
                results.add(function_)
        return results

    def applyRulesToModel(self):
        """ generated source for method applyRulesToModel """
        changeMade = True
        while changeMade:
            changeMade = False
            for gdl in description:
                if isinstance(gdl, (GdlRule, )):
                    changeMade |= addRule(gdl)
            changeMade |= applyLanguageRules()

    def applyLanguageRules(self):
        """ generated source for method applyLanguageRules """
        changesMade = False
        changesMade |= applyInjection(NameAndArity(GdlPool.INIT, 1), NameAndArity(GdlPool.TRUE, 1))
        changesMade |= applyInjection(NameAndArity(GdlPool.NEXT, 1), NameAndArity(GdlPool.TRUE, 1))
        changesMade |= applyInjection(NameAndArity(GdlPool.LEGAL, 2), NameAndArity(GdlPool.DOES, 2))
        return changesMade

    def applyInjection(self, oldName, newName):
        """ generated source for method applyInjection """
        ConcurrencyUtils.checkForInterruption()
        Preconditions.checkArgument(oldName.getArity() == newName.getArity())
        changesMade = False
        if self.sentencesModel.containsKey(oldName):
            if not self.sentencesModel.containsKey(newName):
                changesMade = True
                self.sentencesModel.put(newName, getNTermModels(newName.arity))
            if len(oldModel) != len(newModel):
                raise IllegalStateException()
            while i < len(oldModel):
                ConcurrencyUtils.checkForInterruption()
                changesMade |= newModel.get(i).mergeIn(oldModel.get(i))
                i += 1
        return changesMade

    def addRule(self, rule):
        """ generated source for method addRule """
        headSentence = rule.getHead()
        varsToModelsMap = getVarsToModelsMap(rule)
        return addSentenceToModel(headSentence, varsToModelsMap)

    def getVarsToModelsMap(self, rule):
        """ generated source for method getVarsToModelsMap """
        varsToUse = Sets.newHashSet(GdlUtils.getVariables(rule.getHead()))
        varsToModelsMap = Maps.newHashMap()
        for var in varsToUse:
            varsToModelsMap.put(var, TermModel())
        for literal in rule.getBody():
            if isinstance(literal, (GdlRelation, )):
                if not self.sentencesModel.containsKey(nameAndArity):
                    self.sentencesModel.put(nameAndArity, getNTermModels(nameAndArity.getArity()))
                addVariablesToMap(literalBody, literalModel, varsToModelsMap)
        return varsToModelsMap

    def addVariablesToMap(self, body, model, varsToModelsMap):
        """ generated source for method addVariablesToMap """
        if len(body) != len(model):
            raise IllegalArgumentException("The term model and body sizes don't match: model is " + model + ", body is: " + body)
        i = 0
        while i < len(body):
            if isinstance(term, (GdlVariable, )):
                if varsToModelsMap.containsKey(var):
                    varsToModelsMap.get(var).mergeIn(termModel)
            elif isinstance(term, (GdlFunction, )):
                if functionBodyModel != None:
                    self.addVariablesToMap(function_.getBody(), functionBodyModel, varsToModelsMap)
            i += 1

    def addTrueSentencesToModel(self):
        """ generated source for method addTrueSentencesToModel """
        for gdl in description:
            ConcurrencyUtils.checkForInterruption()
            if isinstance(gdl, (GdlSentence, )):
                addSentenceToModel(gdl, ImmutableMap.of())

    def addSentenceToModel(self, sentence, varsToModelsMap):
        """ generated source for method addSentenceToModel """
        ConcurrencyUtils.checkForInterruption()
        changesMade = False
        sentenceName = NameAndArity(sentence)
        if not self.sentencesModel.containsKey(sentenceName):
            changesMade = True
            self.sentencesModel.put(sentenceName, getNTermModels(sentence.arity()))
        changesMade |= addBodyToModel(self.sentencesModel.get(sentenceName), sentence.getBody(), varsToModelsMap)
        return changesMade

    @classmethod
    def getNTermModels(cls, arity):
        """ generated source for method getNTermModels """
        result = Lists.newArrayListWithCapacity(arity)
        i = 0
        while i < arity:
            result.add(TermModel())
            i += 1
        return result

    @classmethod
    def addBodyToModel(cls, model, body, varsToModelsMap):
        """ generated source for method addBodyToModel """
        changesMade = False
        if len(model) != len(body):
            raise IllegalArgumentException("The term model and body sizes don't match: model is " + model + ", body is: " + body)
        i = 0
        while i < len(model):
            changesMade |= termModel.addTerm(term, varsToModelsMap)
            i += 1
        return changesMade

    class TermModel(object):
        """ generated source for class TermModel """
        possibleConstants = Sets.newHashSet()
        possibleFunctions = Maps.newHashMap()

        def getFunctionBodyModel(self, function_):
            """ generated source for method getFunctionBodyModel """
            return self.possibleFunctions.get(NameAndArity(function_))

        def getPossibleConstants(self):
            """ generated source for method getPossibleConstants """
            return self.possibleConstants

        def getPossibleFunctions(self):
            """ generated source for method getPossibleFunctions """
            return self.possibleFunctions

        def mergeIn(self, other):
            """ generated source for method mergeIn """
            changesMade = False
            changesMade |= self.possibleConstants.addAll(other.possibleConstants)
            for key in other.possibleFunctions.keySet():
                if not self.possibleFunctions.containsKey(key):
                    self.possibleFunctions.put(key, deepCopyOf(theirFunctionBodies))
                    changesMade = True
                else:
                    if len(ourFunctionBodies) != len(theirFunctionBodies):
                        raise IllegalStateException()
                    while i < len(ourFunctionBodies):
                        changesMade |= ourFunctionBodies.get(i).mergeIn(theirFunctionBodies.get(i))
                        i += 1
            return changesMade

        def __init__(self):
            """ generated source for method __init__ """

        def addTerm(self, term, varsToModelsMap):
            """ generated source for method addTerm """
            changesMade = False
            if isinstance(term, (GdlConstant, )):
                changesMade = self.possibleConstants.add(term)
            elif isinstance(term, (GdlFunction, )):
                if not self.possibleFunctions.containsKey(sentenceName):
                    changesMade = True
                    self.possibleFunctions.put(sentenceName, self.getNTermModels(function_.arity()))
                changesMade |= self.addBodyToModel(self.possibleFunctions.get(sentenceName), function_.getBody(), varsToModelsMap)
            elif isinstance(term, (GdlVariable, )):
                changesMade = self.mergeIn(varsToModelsMap.get(term))
            else:
                raise RuntimeException("Unrecognized term type " + term.__class__ + " for term " + term)
            return changesMade

        def __str__(self):
            """ generated source for method toString """
            return "NewTermModel [possibleConstants=" + self.possibleConstants + ", possibleFunctions=" + self.possibleFunctions + "]"

        @classmethod
        def copyOf(cls, originalTermModel):
            """ generated source for method copyOf """
            termModel = cls.TermModel()
            termModel.mergeIn(originalTermModel)
            return termModel

    class NameAndArity(object):
        """ generated source for class NameAndArity """
        name = GdlConstant()
        arity = int()

        @overloaded
        def __init__(self, sentence):
            """ generated source for method __init__ """
            self.name = sentence.__name__
            self.arity = sentence.arity()

        @__init__.register(object, GdlFunction)
        def __init___0(self, function_):
            """ generated source for method __init___0 """
            self.name = function_.__name__
            self.arity = function_.arity()

        @__init__.register(object, GdlConstant, int)
        def __init___1(self, name, arity):
            """ generated source for method __init___1 """
            self.name = name
            self.arity = arity

        def getName(self):
            """ generated source for method getName """
            return self.name

        def getArity(self):
            """ generated source for method getArity """
            return self.arity

        def hashCode(self):
            """ generated source for method hashCode """
            prime = 31
            result = 1
            result = prime * result + self.arity
            result = prime * result + (0 if (self.name == None) else self.name.hashCode())
            return result

        def equals(self, obj):
            """ generated source for method equals """
            if self == obj:
                return True
            if obj == None:
                return False
            if getClass() != obj.__class__:
                return False
            other = obj
            if self.arity != other.arity:
                return False
            if self.name == None:
                if other.name != None:
                    return False
            elif not self.name == other.name:
                return False
            return True

        def __str__(self):
            """ generated source for method toString """
            return "NameAndArity [name=" + self.name + ", arity=" + self.arity + "]"

    @classmethod
    def deepCopyOf(cls, original):
        """ generated source for method deepCopyOf """
        copy = Lists.newArrayListWithCapacity(len(original))
        for originalTermModel in original:
            copy.add(cls.TermModel.copyOf(originalTermModel))
        return copy

