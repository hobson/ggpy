#!/usr/bin/env python
""" generated source for module TtlCache """
from threading import RLock

_locks = {}
def lock_for_object(obj, locks=_locks):
    return locks.setdefault(id(obj), RLock())


def synchronized(call):
    def inner(*args, **kwds):
        with lock_for_object(call):
            return call(*args, **kwds)
    return inner

# package: org.ggp.base.util.statemachine.cache
import java.util.ArrayList

import java.util.Collection

import java.util.HashMap

import java.util.HashSet

import java.util.List

import java.util.Map

import java.util.Set

# 
#  * This is a generic implementation of a Time-To-Live cache
#  * that maps keys of type K to values of type V. It's backed
#  * by a hashmap, and whenever a pair (K,V) is accessed, their
#  * TTL is reset to the starting TTL (which is the parameter
#  * passed to the constructor). On the other hand, when the
#  * method prune() is called, the TTL of all of the pairs in the
#  * map is decremented, and pairs whose TTL has reached zero are
#  * removed.
#  *
#  * While this class implements the Map interface, keep in mind
#  * that it only decrements the TTL of an entry when that entry
#  * is accessed directly.
#  *
#  * @param <K> Key type
#  * @param <V> Value type
#  
class TtlCache(Map, K, V):
    """ generated source for class TtlCache """
    class Entry(object):
        """ generated source for class Entry """
        ttl = int()
        value = V()

        def __init__(self, value, ttl):
            """ generated source for method __init__ """
            self.value = value
            self.ttl = ttl

        @SuppressWarnings("unchecked")
        def equals(self, o):
            """ generated source for method equals """
            if isinstance(o, (self.Entry, )):
                return (o).value == self.value
            return False

    contents = Map()
    ttl = int()

    def __init__(self, ttl):
        """ generated source for method __init__ """
        super(TtlCache, self).__init__()
        self.contents = HashMap()
        self.ttl = ttl

    @synchronized
    def containsKey(self, key):
        """ generated source for method containsKey """
        return self.contents.containsKey(key)

    @synchronized
    def get(self, key):
        """ generated source for method get """
        entry = self.contents.get(key)
        if entry == None:
            return None
        #  Reset the TTL when a value is accessed directly.
        entry.ttl = self.ttl
        return entry.value

    @synchronized
    def prune(self):
        """ generated source for method prune """
        toPrune = ArrayList()
        for key in contents.keySet():
            if entry.ttl == 0:
                toPrune.add(key)
            entry.ttl -= 1
        for key in toPrune:
            self.contents.remove(key)

    @synchronized
    def put(self, key, value):
        """ generated source for method put """
        x = self.contents.put(key, self.Entry(value, self.ttl))
        if x == None:
            return None
        return x.value

    @synchronized
    def size(self):
        """ generated source for method size """
        return len(self.contents)

    @synchronized
    def clear(self):
        """ generated source for method clear """
        self.contents.clear()

    @synchronized
    def containsValue(self, value):
        """ generated source for method containsValue """
        return self.contents.containsValue(value)

    @synchronized
    def isEmpty(self):
        """ generated source for method isEmpty """
        return self.contents.isEmpty()

    @synchronized
    def keySet(self):
        """ generated source for method keySet """
        return self.contents.keySet()

    @synchronized
    def putAll(self, m):
        """ generated source for method putAll """
        for anEntry in m.entrySet():
            self.put(anEntry.getKey(), anEntry.getValue())

    @synchronized
    def remove(self, key):
        """ generated source for method remove """
        return self.contents.remove(key).value

    @synchronized
    def values(self):
        """ generated source for method values """
        theValues = HashSet()
        for e in contents.values():
            theValues.add(e.value)
        return theValues

    class entrySetMapEntry(Map, Entry, K, V):
        """ generated source for class entrySetMapEntry """
        key = K()
        value = V()

        def __init__(self, k, v):
            """ generated source for method __init__ """
            super(entrySetMapEntry, self).__init__()
            self.key = k
            self.value = v

        def getKey(self):
            """ generated source for method getKey """
            return self.key

        def getValue(self):
            """ generated source for method getValue """
            return self.value

        def setValue(self, value):
            """ generated source for method setValue """
            return (self.value = value)

    @synchronized
    def entrySet(self):
        """ generated source for method entrySet """
        theEntries = HashSet()
        for e in contents.entrySet():
            theEntries.add(self.entrySetMapEntry(e.getKey(), e.getValue().value))
        return theEntries

