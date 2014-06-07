#!/usr/bin/env python
""" generated source for module KnowledgeBase """
from threading import RLock

_locks = {}
def lock_for_object(obj, locks=_locks):
    return locks.setdefault(id(obj), RLock())


def synchronized(call):
    def inner(*args, **kwds):
        with lock_for_object(call):
            return call(*args, **kwds)
    return inner

# package: org.ggp.base.util.prover.aima.knowledge
import java.util.ArrayList

import java.util.HashMap

import java.util.List

import java.util.Map

import java.util.Set

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

class KnowledgeBase(object):
    """ generated source for class KnowledgeBase """
    contents = Map()

    def __init__(self, description):
        """ generated source for method __init__ """
        self.contents = HashMap()
        for gdl in description:
            if not self.contents.containsKey(key):
                self.contents.put(key, ArrayList())
            self.contents.get(key).add(rule)

    @synchronized
    def fetch(self, sentence):
        """ generated source for method fetch """
        key = sentence.__name__
        if self.contents.containsKey(key):
            return self.contents.get(key)
        else:
            return ArrayList()

