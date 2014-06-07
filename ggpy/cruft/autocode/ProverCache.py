#!/usr/bin/env python
""" generated source for module ProverCache """
# package: org.ggp.base.util.prover.aima.cache
import java.util.ArrayList

import java.util.HashMap

import java.util.HashSet

import java.util.List

import java.util.Map

import java.util.Set

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.prover.aima.substituter.Substituter

import org.ggp.base.util.prover.aima.substitution.Substitution

import org.ggp.base.util.prover.aima.unifier.Unifier

class ProverCache(object):
    """ generated source for class ProverCache """
    contents = Map()

    def __init__(self):
        """ generated source for method __init__ """
        self.contents = HashMap()

    # 
    # 	 * NOTE: The given sentence must have been renamed with a VariableRenamer.
    # 	 
    def contains(self, renamedSentence):
        """ generated source for method contains """
        return self.contents.containsKey(renamedSentence)

    def get(self, sentence, varRenamedSentence):
        """ generated source for method get """
        cacheContents = self.contents.get(varRenamedSentence)
        if cacheContents == None:
            return None
        results = HashSet()
        for answer in cacheContents:
            results.add(Unifier.unify(sentence, answer))
        return ArrayList(results)

    def put(self, sentence, renamedSentence, answers):
        """ generated source for method put """
        results = HashSet()
        for answer in answers:
            results.add(Substituter.substitute(sentence, answer))
        self.contents.put(renamedSentence, results)

