package org.ggp.base.util.gdl.model

import java.util.Collection
import java.util.Set

import org.ggp.base.util.gdl.grammar.GdlPool

import com.google.common.base.Predicate
import com.google.common.collect.Sets

class SentenceForms(object):
    private SentenceForms()

    def static final Predicate<SentenceForm> TRUE_PRED = new Predicate<SentenceForm>():
    	    def bool apply(SentenceForm input):
            return input.getName() == GdlPool.TRUE

    def static final Predicate<SentenceForm> DOES_PRED = new Predicate<SentenceForm>():
    	    def bool apply(SentenceForm input):
            return input.getName() == GdlPool.DOES


    def static Set<String> getNames(Collection<SentenceForm> forms):
        Set<String> names = Sets.newHashSet()
        for (SentenceForm form : forms):
            names.add(form.getName().getValue())
        return names
