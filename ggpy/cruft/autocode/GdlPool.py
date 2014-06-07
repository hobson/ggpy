#!/usr/bin/env python
""" generated source for module GdlPool """
from threading import RLock

_locks = {}
def lock_for_object(obj, locks=_locks):
    return locks.setdefault(id(obj), RLock())


def synchronized(call):
    def inner(*args, **kwds):
        with lock_for_object(call):
            return call(*args, **kwds)
    return inner

# package: org.ggp.base.util.gdl.grammar
import java.util.ArrayList

import java.util.Arrays

import java.util.Collections

import java.util.HashMap

import java.util.List

import java.util.Map

import java.util.TreeMap

import java.util.concurrent.ConcurrentHashMap

import java.util.concurrent.ConcurrentMap

import com.google.common.collect.ImmutableSet

import com.google.common.collect.MapMaker

# 
#  * The GdlPool manages the creation of {@link Gdl} objects. It is the only way Gdl
#  * objects may be created. It ensures that for each possible sentence, rule, or
#  * fragment of GDL, only one corresponding Gdl object is created. This means Gdl
#  * objects may be checked for equality with an instance-equality check (==) rather
#  * than a more expensive recursive equality check.
#  * <p>
#  * A long-lived game player may accumulate lots of objects in its pool. To remove
#  * them, it may call {@link #drainPool()} in between games. Note that if this
#  * method is called while references to Gdl objects other than keyword constants
#  * are held elsewhere, bad things will happen.
#  
class GdlPool(object):
    """ generated source for class GdlPool """
    distinctPool = ConcurrentHashMap()
    functionPool = ConcurrentHashMap()
    notPool = ConcurrentHashMap()
    orPool = ConcurrentHashMap()
    propositionPool = ConcurrentHashMap()
    relationPool = ConcurrentHashMap()
    rulePool = ConcurrentHashMap()
    variablePool = ConcurrentHashMap()
    constantPool = ConcurrentHashMap()

    # Access to constantCases and variableCases should be synchronized using their monitor locks.
    constantCases = TreeMap(String.CASE_INSENSITIVE_ORDER)
    variableCases = TreeMap(String.CASE_INSENSITIVE_ORDER)

    #  Controls whether we normalize the case of incoming constants and variables.
    caseSensitive = True

    #  Special keyword constants. These are never drained between games and are always
    #  represented as lower-case so that they can easily be referred to internally and
    #  so that all of the "true" objects are equal to each other in the Java == sense.
    #  For example, attempting to create a GdlConstant "TRUE" will return the same constant
    #  as if one had attempted to create the GdlConstant "true", regardless of whether the
    #  game-specific constants are case-sensitive or not. These special keywords are never
    #  sent over the network in PLAY requests and responses, so this should be safe.
    KEYWORDS = ImmutableSet.of("init", "true", "next", "role", "does", "goal", "legal", "terminal", "base", "input", "_")
    BASE = getConstant("base")
    DOES = getConstant("does")
    GOAL = getConstant("goal")
    INIT = getConstant("init")
    INPUT = getConstant("input")
    LEGAL = getConstant("legal")
    NEXT = getConstant("next")
    ROLE = getConstant("role")
    TERMINAL = getConstant("terminal")
    TRUE = getConstant("true")

    # 
    #      * Represents a single underscore ("_"). The underscore is not a GDL keyword, but
    #      * it's used by SentenceForms and is generally convenient for utility methods.
    #      
    UNDERSCORE = getConstant("_")

    def __init__(self):
        """ generated source for method __init__ """
        #  Not instantiable

    # 
    # 	 * once you have finished playing a large game.
    # 	 *
    # 	 * WARNING: Should only be called *between games*, when there are no
    # 	 * references to Gdl objects (other than keyword constants) outside the
    # 	 * pool.
    # 	 
    @classmethod
    def drainPool(cls):
        """ generated source for method drainPool """
        cls.distinctPool.clear()
        cls.functionPool.clear()
        cls.notPool.clear()
        cls.orPool.clear()
        cls.propositionPool.clear()
        cls.relationPool.clear()
        cls.rulePool.clear()
        cls.variablePool.clear()
        with lock_for_object(cls.variableCases):
            cls.variableCases.clear()
        #  When draining the pool between matches, we still need to preserve the keywords
        #  since there are global references to them. For example, the Prover state machine
        #  has a reference to the GdlConstant "true", and that reference must still point
        #  to the authoritative GdlConstant "true" after the pool is drained and another
        #  game has begun. As such, when draining the constant pool, these special keywords
        #  are set aside and returned to the pool after all of the other constants (which
        #  were game-specific) have been drained.
        keywordConstants = HashMap()
        for keyword in KEYWORDS:
            keywordConstants.put(keyword, GdlPool.getConstant(keyword))
        with lock_for_object(cls.constantCases):
            cls.constantPool.clear()
            cls.constantCases.clear()
            for keywordEntry in keywordConstants.entrySet():
                cls.constantCases.put(keywordEntry.getKey(), keywordEntry.getKey())
                cls.constantPool.put(keywordEntry.getKey(), keywordEntry.getValue())

    # 
    # 	 * If the pool does not have a mapping for the given key, adds a mapping from key to value
    # 	 * to the pool.
    # 	 *
    # 	 * Note that even if you've checked to make sure that the pool doesn't contain the key,
    # 	 * you still shouldn't assume that this method actually inserts the given value, since
    # 	 * this class is accessed by multiple threads simultaneously.
    # 	 *
    # 	 * @return the value mapped to by key in the pool
    # 	 
    @classmethod
    def addToPool(cls, key, value, pool):
        """ generated source for method addToPool """
        prevValue = pool.putIfAbsent(key, value)
        if prevValue == None:
            return value
        else:
            return prevValue

    @classmethod
    def getConstant(cls, value):
        """ generated source for method getConstant """
        if cls.KEYWORDS.contains(value.lower()):
            value = value.lower()
        if not cls.caseSensitive:
            with lock_for_object(cls.constantCases):
                if cls.constantCases.containsKey(value):
                    value = cls.constantCases.get(value)
                else:
                    cls.constantCases.put(value, value)
        ret = cls.constantPool.get(value)
        if ret == None:
            ret = cls.addToPool(value, GdlConstant(value), cls.constantPool)
        return ret

    @classmethod
    def getVariable(cls, name):
        """ generated source for method getVariable """
        if not cls.caseSensitive:
            with lock_for_object(cls.variableCases):
                if cls.variableCases.containsKey(name):
                    name = cls.variableCases.get(name)
                else:
                    cls.variableCases.put(name, name)
        ret = cls.variablePool.get(name)
        if ret == None:
            ret = cls.addToPool(name, GdlVariable(name), cls.variablePool)
        return ret

    @classmethod
    def getDistinct(cls, arg1, arg2):
        """ generated source for method getDistinct """
        bucket = cls.distinctPool.get(arg1)
        if bucket == None:
            bucket = cls.addToPool(arg1, ConcurrentHashMap(), cls.distinctPool)
        ret = bucket.get(arg2)
        if ret == None:
            ret = cls.addToPool(arg2, GdlDistinct(arg1, arg2), bucket)
        return ret

    @classmethod
    @overloaded
    def getFunction(cls, name):
        """ generated source for method getFunction """
        empty = Collections.emptyList()
        return cls.getFunction(name, empty)

    @classmethod
    @getFunction.register(object, GdlConstant, GdlTerm)
    def getFunction_0(cls, name, body):
        """ generated source for method getFunction_0 """
        return cls.getFunction(name, Arrays.asList(body))

    @classmethod
    @getFunction.register(object, GdlConstant, List)
    def getFunction_1(cls, name, body):
        """ generated source for method getFunction_1 """
        bucket = cls.functionPool.get(name)
        if bucket == None:
            bucket = cls.addToPool(name, newMap, cls.functionPool)
        ret = bucket.get(body)
        if ret == None:
            body = getImmutableCopy(body)
            ret = cls.addToPool(body, GdlFunction(name, body), bucket)
        return ret

    @classmethod
    def getNot(cls, body):
        """ generated source for method getNot """
        ret = cls.notPool.get(body)
        if ret == None:
            ret = cls.addToPool(body, GdlNot(body), cls.notPool)
        return ret

    @classmethod
    @overloaded
    def getOr(cls, disjuncts):
        """ generated source for method getOr """
        return cls.getOr(Arrays.asList(disjuncts))

    @classmethod
    @getOr.register(object, List)
    def getOr_0(cls, disjuncts):
        """ generated source for method getOr_0 """
        ret = cls.orPool.get(disjuncts)
        if ret == None:
            disjuncts = getImmutableCopy(disjuncts)
            ret = cls.addToPool(disjuncts, GdlOr(disjuncts), cls.orPool)
        return ret

    @classmethod
    def getProposition(cls, name):
        """ generated source for method getProposition """
        ret = cls.propositionPool.get(name)
        if ret == None:
            ret = cls.addToPool(name, GdlProposition(name), cls.propositionPool)
        return ret

    @classmethod
    @overloaded
    def getRelation(cls, name):
        """ generated source for method getRelation """
        empty = Collections.emptyList()
        return cls.getRelation(name, empty)

    @classmethod
    @getRelation.register(object, GdlConstant, GdlTerm)
    def getRelation_0(cls, name, body):
        """ generated source for method getRelation_0 """
        return cls.getRelation(name, Arrays.asList(body))

    @classmethod
    @getRelation.register(object, GdlConstant, List)
    def getRelation_1(cls, name, body):
        """ generated source for method getRelation_1 """
        bucket = cls.relationPool.get(name)
        if bucket == None:
            bucket = cls.addToPool(name, newMap, cls.relationPool)
        ret = bucket.get(body)
        if ret == None:
            body = getImmutableCopy(body)
            ret = cls.addToPool(body, GdlRelation(name, body), bucket)
        return ret

    @classmethod
    @overloaded
    def getRule(cls, head):
        """ generated source for method getRule """
        empty = Collections.emptyList()
        return cls.getRule(head, empty)

    @classmethod
    @getRule.register(object, GdlSentence, GdlLiteral)
    def getRule_0(cls, head, body):
        """ generated source for method getRule_0 """
        return cls.getRule(head, Arrays.asList(body))

    @classmethod
    @getRule.register(object, GdlSentence, List)
    def getRule_1(cls, head, body):
        """ generated source for method getRule_1 """
        bucket = cls.rulePool.get(head)
        if bucket == None:
            bucket = cls.addToPool(head, ConcurrentHashMap(), cls.rulePool)
        ret = bucket.get(body)
        if ret == None:
            body = getImmutableCopy(body)
            ret = cls.addToPool(body, GdlRule(head, body), bucket)
        return ret

    @classmethod
    def getImmutableCopy(cls, list_):
        """ generated source for method getImmutableCopy """
        return Collections.unmodifiableList(ArrayList(list_))

    # 
    # 	 * This method should only rarely be used. It takes a foreign GDL object
    # 	 * (one that wasn't constructed through the GdlPool) and returns a version
    # 	 * expect that all GDL objects live in the GdlPool, and so it's important
    # 	 * that any foreign GDL objects created outside the GdlPool be immersed
    # 	 * before being used. Since every GDL object should be created through the
    # 	 * GdlPool, immerse should only need to be called on GDL that appears from
    # 	 * outside sources: for example, being deserialized from a file.
    # 	 
    @classmethod
    def immerse(cls, foreignGdl):
        """ generated source for method immerse """
        if isinstance(foreignGdl, (GdlDistinct, )):
            return GdlPool.getDistinct(cls.immerse((foreignGdl).getArg1()), cls.immerse((foreignGdl).getArg2()))
        elif isinstance(foreignGdl, (GdlNot, )):
            return GdlPool.getNot(cls.immerse((foreignGdl).getBody()))
        elif isinstance(foreignGdl, (GdlOr, )):
            while i < or_.arity():
                rval.add(cls.immerse(or_.get(i)))
                i += 1
            return GdlPool.getOr(rval)
        elif isinstance(foreignGdl, (GdlProposition, )):
            return GdlPool.getProposition(cls.immerse((foreignGdl).__name__))
        elif isinstance(foreignGdl, (GdlRelation, )):
            while i < rel.arity():
                rval.add(cls.immerse(rel.get(i)))
                i += 1
            return GdlPool.getRelation(cls.immerse(rel.__name__), rval)
        elif isinstance(foreignGdl, (GdlRule, )):
            while i < rule.arity():
                rval.add(cls.immerse(rule.get(i)))
                i += 1
            return GdlPool.getRule(cls.immerse(rule.getHead()), rval)
        elif isinstance(foreignGdl, (GdlConstant, )):
            return GdlPool.getConstant((foreignGdl).getValue())
        elif isinstance(foreignGdl, (GdlFunction, )):
            while i < func.arity():
                rval.add(cls.immerse(func.get(i)))
                i += 1
            return GdlPool.getFunction(cls.immerse(func.__name__), rval)
        elif isinstance(foreignGdl, (GdlVariable, )):
            return GdlPool.getVariable((foreignGdl).__name__)
        else:
            raise RuntimeException("Uh oh, gdl hierarchy must have been extended without updating this code.")

GdlPool.# 	 * Drains the contents of the GdlPool. Useful to control memory usage

GdlPool.# 	 * that lives in the GdlPool. Various parts of the prover infrastructure

