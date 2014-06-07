#!/usr/bin/env python
""" generated source for module AimaProver """
# package: org.ggp.base.util.prover.aima
import java.util.ArrayList

import java.util.HashSet

import java.util.LinkedList

import java.util.List

import java.util.Set

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlNot

import org.ggp.base.util.gdl.grammar.GdlOr

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.transforms.DistinctAndNotMover

import org.ggp.base.util.prover.Prover

import org.ggp.base.util.prover.aima.cache.ProverCache

import org.ggp.base.util.prover.aima.knowledge.KnowledgeBase

import org.ggp.base.util.prover.aima.renamer.VariableRenamer

import org.ggp.base.util.prover.aima.substituter.Substituter

import org.ggp.base.util.prover.aima.substitution.Substitution

import org.ggp.base.util.prover.aima.unifier.Unifier

import com.google.common.collect.Sets

class AimaProver(Prover):
    """ generated source for class AimaProver """
    knowledgeBase = KnowledgeBase()
    fixedAnswerCache = ProverCache()

    def __init__(self, description):
        """ generated source for method __init__ """
        super(AimaProver, self).__init__()
        description = DistinctAndNotMover.run(description)
        self.knowledgeBase = KnowledgeBase(Sets.newHashSet(description))

    @overloaded
    def ask(self, query, context, askOne):
        """ generated source for method ask """
        goals = LinkedList()
        goals.add(query)
        answers = HashSet()
        alreadyAsking = HashSet()
        self.ask(goals, KnowledgeBase(context), Substitution(), ProverCache(), VariableRenamer(), askOne, answers, alreadyAsking)
        results = HashSet()
        for theta in answers:
            results.add(Substituter.substitute(query, theta))
        return results

    #  Returns true iff the result is constant across all possible states of the game.
    @ask.register(object, LinkedList, KnowledgeBase, Substitution, ProverCache, VariableRenamer, bool, Set, Set)
    def ask_0(self, goals, context, theta, cache, renamer, askOne, results, alreadyAsking):
        """ generated source for method ask_0 """
        if len(goals) == 0:
            results.add(theta)
            return True
        else:
            if isinstance(qPrime, (GdlDistinct, )):
                isConstant = askDistinct(distinct, goals, context, theta, cache, renamer, askOne, results, alreadyAsking)
            elif isinstance(qPrime, (GdlNot, )):
                isConstant = askNot(not_, goals, context, theta, cache, renamer, askOne, results, alreadyAsking)
            elif isinstance(qPrime, (GdlOr, )):
                isConstant = askOr(or_, goals, context, theta, cache, renamer, askOne, results, alreadyAsking)
            else:
                isConstant = askSentence(sentence, goals, context, theta, cache, renamer, askOne, results, alreadyAsking)
            goals.addFirst(literal)
            return isConstant

    def askAll(self, query, context):
        """ generated source for method askAll """
        return self.ask(query, context, False)

    #  Returns true iff the result is constant across all possible states of the game.
    def askDistinct(self, distinct, goals, context, theta, cache, renamer, askOne, results, alreadyAsking):
        """ generated source for method askDistinct """
        if not distinct.getArg1() == distinct.getArg2():
            return self.ask(goals, context, theta, cache, renamer, askOne, results, alreadyAsking)
        return True

    #  Returns true iff the result is constant across all possible states of the game.
    def askNot(self, not_, goals, context, theta, cache, renamer, askOne, results, alreadyAsking):
        """ generated source for method askNot """
        notGoals = LinkedList()
        notGoals.add(not_.getBody())
        notResults = HashSet()
        isConstant = True
        isConstant &= self.ask(notGoals, context, theta, cache, renamer, True, notResults, alreadyAsking)
        if len(notResults) == 0:
            isConstant &= self.ask(goals, context, theta, cache, renamer, askOne, results, alreadyAsking)
        return isConstant

    def askOne(self, query, context):
        """ generated source for method askOne """
        results = self.ask(query, context, True)
        return results.iterator().next() if (len(results) > 0) else None

    #  Returns true iff the result is constant across all possible states of the game.
    def askOr(self, or_, goals, context, theta, cache, renamer, askOne, results, alreadyAsking):
        """ generated source for method askOr """
        isConstant = True
        i = 0
        while i < or_.arity():
            goals.addFirst(or_.get(i))
            isConstant &= self.ask(goals, context, theta, cache, renamer, askOne, results, alreadyAsking)
            goals.removeFirst()
            if askOne and (len(results) > 0):
                break
            i += 1
        return isConstant

    #  Returns true iff the result is constant across all possible states of the game.
    def askSentence(self, sentence, goals, context, theta, cache, renamer, askOne, results, alreadyAsking):
        """ generated source for method askSentence """
        varRenamedSentence = VariableRenamer().rename(sentence)
        if not self.fixedAnswerCache.contains(varRenamedSentence) and not cache.contains(varRenamedSentence):
            # Prevent infinite loops on certain recursive queries.
            if alreadyAsking.contains(sentence):
                return False
            alreadyAsking.add(sentence)
            candidates.addAll(self.knowledgeBase.fetch(sentence))
            candidates.addAll(context.fetch(sentence))
            for rule in candidates:
                if thetaPrime != None:
                    while i < r.arity():
                        sentenceGoals.add(r.get(i))
                        i += 1
                    isConstant &= self.ask(sentenceGoals, context, theta.compose(thetaPrime), cache, renamer, False, sentenceResults, alreadyAsking)
            if isConstant:
                self.fixedAnswerCache.put(sentence, varRenamedSentence, sentenceResults)
            else:
                cache.put(sentence, varRenamedSentence, sentenceResults)
            alreadyAsking.remove(sentence)
        cachedResults = self.fixedAnswerCache.get(sentence, varRenamedSentence)
        isConstant = (cachedResults != None)
        if cachedResults == None:
            cachedResults = cache.get(sentence, varRenamedSentence)
        for thetaPrime in cachedResults:
            isConstant &= self.ask(goals, context, theta.compose(thetaPrime), cache, renamer, askOne, results, alreadyAsking)
            if askOne and (len(results) > 0):
                break
        return isConstant

    def isTrueOrDoesSentence(self, sentence):
        """ generated source for method isTrueOrDoesSentence """
        name = sentence.__name__
        return name == GdlPool.TRUE or name == GdlPool.DOES

    def prove(self, query, context):
        """ generated source for method prove """
        return self.askOne(query, context) != None

