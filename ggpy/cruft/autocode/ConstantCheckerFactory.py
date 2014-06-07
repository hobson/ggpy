#!/usr/bin/env python
""" generated source for module ConstantCheckerFactory """
# package: org.ggp.base.util.gdl.transforms
import java.util.List

import java.util.Set

import org.ggp.base.util.concurrency.ConcurrencyUtils

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.gdl.model.DependencyGraphs

import org.ggp.base.util.gdl.model.SentenceDomainModel

import org.ggp.base.util.gdl.model.SentenceForm

import org.ggp.base.util.gdl.model.SentenceFormModel

import org.ggp.base.util.prover.aima.AimaProver

import org.ggp.base.util.reasoner.gdl.GdlChainingReasoner

import org.ggp.base.util.reasoner.gdl.GdlSentenceSet

import com.google.common.base.Predicates

import com.google.common.collect.HashMultimap

import com.google.common.collect.ImmutableMultimap

import com.google.common.collect.ImmutableSet

import com.google.common.collect.Lists

import com.google.common.collect.Multimap

import com.google.common.collect.Multimaps

class ConstantCheckerFactory(object):
    """ generated source for class ConstantCheckerFactory """
    # 
    # 	 * Precomputes the true sentences in every constant sentence form in the given
    # 	 * sentence model and returns the results in the form of a ConstantChecker.
    # 	 *
    # 	 * The implementation uses a forward-chaining reasoner.
    # 	 *
    # 	 * For accurate results, the rules used should have had the {@link NewVariableConstrainer}
    # 	 * transformation applied to them.
    # 	 *
    # 	 * On average, this approach is more efficient than {@link #createWithProver(SentenceFormModel)}.
    # 	 
    @classmethod
    def createWithForwardChaining(cls, model):
        """ generated source for method createWithForwardChaining """
        reasoner = GdlChainingReasoner.create(model)
        sentencesByForm = reasoner.getConstantSentences()
        addSentencesTrueByRulesDifferentially(sentencesByForm, model, reasoner)
        return ImmutableConstantChecker.create(model, Multimaps.filterKeys(sentencesByForm.getSentences(), Predicates.in_(model.getConstantSentenceForms())))

    @classmethod
    def addSentencesTrueByRulesDifferentially(cls, sentencesByForm, domainModel, reasoner):
        """ generated source for method addSentencesTrueByRulesDifferentially """
        model = domainModel
        constantForms = model.getConstantSentenceForms()
        # Find the part of the dependency graph dealing only with the constant forms.
        dependencySubgraph = Multimaps.filterKeys(model.getDependencyGraph(), Predicates.in_(constantForms))
        dependencySubgraph = Multimaps.filterValues(model.getDependencyGraph(), Predicates.in_(constantForms))
        dependencySubgraph = ImmutableMultimap.copyOf(dependencySubgraph)
        ordering = DependencyGraphs.toposortSafe(constantForms, dependencySubgraph)
        for stratum in ordering:
            #  One non-differential pass, collecting the changes
            for form in stratum:
                for rule in model.getRules(form):
                    if not reasoner.isSubsetOf(sentencesByForm, ruleResults):
                        sentencesByForm = reasoner.getUnion(sentencesByForm, ruleResults)
                        newlyTrueSentences = reasoner.getUnion(newlyTrueSentences, ruleResults)
            #  Now a lot of differential passes to deal with recursion efficiently
            while somethingChanged:
                somethingChanged = False
                for form in stratum:
                    for rule in model.getRules(form):
                        if not reasoner.isSubsetOf(sentencesByForm, ruleResults):
                            somethingChanged = True
                            newStuffInThisPass = reasoner.getUnion(newStuffInThisPass, ruleResults)
                sentencesByForm = reasoner.getUnion(sentencesByForm, newStuffInThisPass)
                newlyTrueSentences = newStuffInThisPass

    # 
    # 	 * Precomputes the true sentences in every constant sentence form in the given
    # 	 * sentence model and returns the results in the form of a ConstantChecker.
    # 	 *
    # 	 * The implementation uses a backwards-chaining theorem prover.
    # 	 *
    # 	 * In most (but not all) cases, {@link #createWithForwardChaining(SentenceDomainModel)}
    # 	 * is more efficient.
    # 	 
    @classmethod
    def createWithProver(cls, model):
        """ generated source for method createWithProver """
        sentencesByForm = HashMultimap.create()
        addSentencesTrueByRules(sentencesByForm, model)
        return ImmutableConstantChecker.create(model, sentencesByForm)

    @classmethod
    def addSentencesTrueByRules(cls, sentencesByForm, model):
        """ generated source for method addSentencesTrueByRules """
        prover = AimaProver(model.getDescription())
        for form in model.getConstantSentenceForms():
            for result in prover.askAll(query, ImmutableSet.of()):
                ConcurrencyUtils.checkForInterruption()
                # Variables may end up being replaced with functions, which is not
                # what we want here, so we have to double-check that the form is correct.
                if form.matches(result):
                    sentencesByForm.put(form, result)

    @classmethod
    def getVariablesTuple(cls, tupleSize):
        """ generated source for method getVariablesTuple """
        varsTuple = Lists.newArrayList()
        i = 0
        while i < tupleSize:
            varsTuple.add(GdlPool.getVariable("?" + i))
            i += 1
        return varsTuple

