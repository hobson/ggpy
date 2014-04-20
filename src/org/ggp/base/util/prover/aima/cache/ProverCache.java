package org.ggp.base.util.prover.aima.cache

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


class ProverCache


    private final Map<GdlSentence, Set<GdlSentence>> contents

    def ProverCache()
	
        contents = new HashMap<GdlSentence, Set<GdlSentence>>()

	/**
	 * NOTE: The given sentence must have been renamed with a VariableRenamer.
	 */
    def bool contains(GdlSentence renamedSentence)
	
        return contents.containsKey(renamedSentence)

    def List<Substitution> get(GdlSentence sentence, GdlSentence varRenamedSentence)
	
        Set<GdlSentence> cacheContents = contents.get(varRenamedSentence)
        if (cacheContents == null):
            return null
        Set<Substitution> results = new HashSet<Substitution>()
        for (GdlSentence answer : cacheContents)
		
            results.add(Unifier.unify(sentence, answer))

        return new ArrayList<Substitution>(results)

    def void put(GdlSentence sentence, GdlSentence renamedSentence,
            Set<Substitution> answers)
	
        Set<GdlSentence> results = new HashSet<GdlSentence>()
        for (Substitution answer : answers)
		
            results.add(Substituter.substitute(sentence, answer))

        contents.put(renamedSentence, results)

