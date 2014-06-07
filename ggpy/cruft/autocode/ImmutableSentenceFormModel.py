#!/usr/bin/env python
""" generated source for module ImmutableSentenceFormModel """
# package: org.ggp.base.util.gdl.model
import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import com.google.common.base.Preconditions

import com.google.common.collect.ImmutableList

import com.google.common.collect.ImmutableMultimap

import com.google.common.collect.ImmutableSet

import com.google.common.collect.ImmutableSetMultimap

class ImmutableSentenceFormModel(SentenceFormModel):
    """ generated source for class ImmutableSentenceFormModel """
    gameDescription = ImmutableList()
    sentenceForms = ImmutableSet()
    constantSentenceForms = ImmutableSet()
    independentSentenceForms = ImmutableSet()
    dependencyGraph = ImmutableSetMultimap()
    rulesByForm = ImmutableSetMultimap()
    trueSentencesByForm = ImmutableSetMultimap()

    def __init__(self, gameDescription, sentenceForms, constantSentenceForms, independentSentenceForms, dependencyGraph, rulesByForm, trueSentencesByForm):
        """ generated source for method __init__ """
        super(ImmutableSentenceFormModel, self).__init__()
        Preconditions.checkArgument(sentenceForms.containsAll(independentSentenceForms))
        Preconditions.checkArgument(independentSentenceForms.containsAll(constantSentenceForms))
        Preconditions.checkArgument(sentenceForms.containsAll(dependencyGraph.keySet()))
        Preconditions.checkArgument(sentenceForms.containsAll(dependencyGraph.values()))
        Preconditions.checkArgument(sentenceForms.containsAll(rulesByForm.keySet()))
        Preconditions.checkArgument(sentenceForms.containsAll(trueSentencesByForm.keySet()))
        self.gameDescription = gameDescription
        self.sentenceForms = sentenceForms
        self.constantSentenceForms = constantSentenceForms
        self.independentSentenceForms = independentSentenceForms
        self.dependencyGraph = dependencyGraph
        self.rulesByForm = rulesByForm
        self.trueSentencesByForm = trueSentencesByForm

    # 
    # 	 * Returns an ImmutableSentenceFormModel with the same contents as the
    # 	 * given SentenceFormModel.
    # 	 *
    # 	 * May not actually create a copy if the input is immutable.
    # 	 
    @classmethod
    def copyOf(cls, other):
        """ generated source for method copyOf """
        if isinstance(other, (ImmutableSentenceDomainModel, )):
            return cls.copyOf((other).getFormModel())
        elif isinstance(other, (ImmutableSentenceFormModel, )):
            return other
        rulesByForm = ImmutableSetMultimap.builder()
        trueSentencesByForm = ImmutableSetMultimap.builder()
        for form in other.getSentenceForms():
            rulesByForm.putAll(form, other.getRules(form))
            trueSentencesByForm.putAll(form, other.getSentencesListedAsTrue(form))
        return ImmutableSentenceFormModel(ImmutableList.copyOf(other.getDescription()), ImmutableSet.copyOf(other.getSentenceForms()), ImmutableSet.copyOf(other.getConstantSentenceForms()), ImmutableSet.copyOf(other.getIndependentSentenceForms()), ImmutableSetMultimap.copyOf(other.getDependencyGraph()), rulesByForm.build(), trueSentencesByForm.build())

    # TODO: Come up with an implementation that can save memory relative to this
    # (i.e. where we can reuse SentenceForm references)
    def getSentenceForm(self, sentence):
        """ generated source for method getSentenceForm """
        return SimpleSentenceForm.create(sentence)

    def getIndependentSentenceForms(self):
        """ generated source for method getIndependentSentenceForms """
        return self.independentSentenceForms

    def getConstantSentenceForms(self):
        """ generated source for method getConstantSentenceForms """
        return self.constantSentenceForms

    def getDependencyGraph(self):
        """ generated source for method getDependencyGraph """
        return self.dependencyGraph

    def getSentencesListedAsTrue(self, form):
        """ generated source for method getSentencesListedAsTrue """
        return self.trueSentencesByForm.get(form)

    def getRules(self, form):
        """ generated source for method getRules """
        return self.rulesByForm.get(form)

    def getSentenceForms(self):
        """ generated source for method getSentenceForms """
        return self.sentenceForms

    def getDescription(self):
        """ generated source for method getDescription """
        return self.gameDescription

