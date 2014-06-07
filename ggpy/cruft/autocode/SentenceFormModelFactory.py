#!/usr/bin/env python
""" generated source for module SentenceFormModelFactory """
# package: org.ggp.base.util.gdl.model
import java.util.HashSet

import java.util.List

import java.util.Map.Entry

import java.util.Set

import org.ggp.base.util.gdl.GdlVisitor

import org.ggp.base.util.gdl.GdlVisitors

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.transforms.GdlCleaner

import org.ggp.base.util.gdl.transforms.VariableConstrainer

import com.google.common.base.Predicates

import com.google.common.collect.HashMultimap

import com.google.common.collect.ImmutableList

import com.google.common.collect.ImmutableSet

import com.google.common.collect.ImmutableSetMultimap

import com.google.common.collect.SetMultimap

import com.google.common.collect.Sets

class SentenceFormModelFactory(object):
    """ generated source for class SentenceFormModelFactory """
    # 
    # 	 * Creates a SentenceFormModel for the given game description.
    # 	 *
    # 	 * It is recommended to use the {@link GdlCleaner} on the game
    # 	 * description before constructing this model, to prevent some
    # 	 * common problems with slightly invalid game descriptions.
    # 	 *
    # 	 * It is also recommended to use the {@link VariableConstrainer}
    # 	 * on the description before using this. If the description allows
    # 	 * for function-valued variables, some aspects of the model,
    # 	 * including the dependency graph, may be incorrect.
    # 	 
    @classmethod
    def create(cls, description):
        """ generated source for method create """
        gameRules = ImmutableList.copyOf(description)
        sentenceForms = getSentenceForms(gameRules)
        rulesByForm = getRulesByForm(gameRules, sentenceForms)
        trueSentencesByForm = getTrueSentencesByForm(gameRules, sentenceForms)
        dependencyGraph = getDependencyGraph(sentenceForms, rulesByForm)
        constantSentenceForms = getConstantSentenceForms(sentenceForms, dependencyGraph)
        independentSentenceForms = getIndependentSentenceForms(sentenceForms, dependencyGraph)
        return ImmutableSentenceFormModel(gameRules, sentenceForms, constantSentenceForms, independentSentenceForms, dependencyGraph, rulesByForm, trueSentencesByForm)

    @classmethod
    def getIndependentSentenceForms(cls, sentenceForms, dependencyGraph):
        """ generated source for method getIndependentSentenceForms """
        augmentedGraph = augmentGraphWithLanguageRules(dependencyGraph, sentenceForms)
        moveDependentSentenceForms = DependencyGraphs.getMatchingAndDownstream(sentenceForms, augmentedGraph, SentenceForms.DOES_PRED)
        return ImmutableSet.copyOf(Sets.difference(sentenceForms, moveDependentSentenceForms))

    @classmethod
    def getConstantSentenceForms(cls, sentenceForms, dependencyGraph):
        """ generated source for method getConstantSentenceForms """
        augmentedGraph = augmentGraphWithLanguageRules(dependencyGraph, sentenceForms)
        changingSentenceForms = DependencyGraphs.getMatchingAndDownstream(sentenceForms, augmentedGraph, Predicates.or_(SentenceForms.TRUE_PRED, SentenceForms.DOES_PRED))
        return ImmutableSet.copyOf(Sets.difference(sentenceForms, changingSentenceForms))

    # 
    # 	 * Modifies the graph by adding dependencies corresponding to language rules
    # 	 * that apply in a looser sense: TRUE forms depend on NEXT forms and DOES
    # 	 * forms depend on LEGAL forms.
    # 	 
    @classmethod
    def augmentGraphWithLanguageRules(cls, dependencyGraph, sentenceForms):
        """ generated source for method augmentGraphWithLanguageRules """
        newGraph = HashMultimap.create()
        newGraph.putAll(dependencyGraph)
        for form in sentenceForms:
            if form.__name__ == GdlPool.TRUE:
                if sentenceForms.contains(nextForm):
                    newGraph.put(form, nextForm)
            elif form.__name__ == GdlPool.DOES:
                if sentenceForms.contains(legalForm):
                    newGraph.put(form, legalForm)
        return newGraph

    @classmethod
    def getDependencyGraph(cls, sentenceForms, rulesByForm):
        """ generated source for method getDependencyGraph """
        dependencyGraph = HashMultimap.create()
        for entry in rulesByForm.entries():
            for bodyLiteral in rule.getBody():
                dependencyGraph.putAll(head, getSentenceFormsInBody(bodyLiteral, sentenceForms))
        return ImmutableSetMultimap.copyOf(dependencyGraph)

    @classmethod
    def getSentenceFormsInBody(cls, bodyLiteral, sentenceForms):
        """ generated source for method getSentenceFormsInBody """
        forms = HashSet()
        GdlVisitors.visitAll(bodyLiteral, GdlVisitor())
        return forms

    @classmethod
    def getTrueSentencesByForm(cls, gameRules, sentenceForms):
        """ generated source for method getTrueSentencesByForm """
        builder = ImmutableSetMultimap.builder()
        for gdl in gameRules:
            if isinstance(gdl, (GdlSentence, )):
                for form in sentenceForms:
                    if form.matches(sentence):
                        builder.put(form, sentence)
                        break
        return builder.build()

    @classmethod
    def getRulesByForm(cls, gameRules, sentenceForms):
        """ generated source for method getRulesByForm """
        builder = ImmutableSetMultimap.builder()
        for gdl in gameRules:
            if isinstance(gdl, (GdlRule, )):
                for form in sentenceForms:
                    if form.matches(rule.getHead()):
                        builder.put(form, rule)
                        break
        return builder.build()

    @classmethod
    def getSentenceForms(cls, gameRules):
        """ generated source for method getSentenceForms """
        return SentenceFormsFinder(gameRules).findSentenceForms()

