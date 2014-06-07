#!/usr/bin/env python
""" generated source for module SentenceForms """
# package: org.ggp.base.util.gdl.model
import java.util.Collection

import java.util.Set

import org.ggp.base.util.gdl.grammar.GdlPool

import com.google.common.base.Predicate

import com.google.common.collect.Sets

class SentenceForms(object):
    """ generated source for class SentenceForms """
    def __init__(self):
        """ generated source for method __init__ """

    TRUE_PRED = Predicate()

    @overloaded
    def apply(self, input):
        """ generated source for method apply """
        return input.__name__ == GdlPool.TRUE

    DOES_PRED = Predicate()

    @apply.register(object, SentenceForm)
    def apply_0(self, input):
        """ generated source for method apply_0 """
        return input.__name__ == GdlPool.DOES

    @classmethod
    def getNames(cls, forms):
        """ generated source for method getNames """
        names = Sets.newHashSet()
        for form in forms:
            names.add(form.__name__.getValue())
        return names

