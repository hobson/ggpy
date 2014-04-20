package org.ggp.base.util.gdl.grammar;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;

import com.google.common.collect.ImmutableSet;
import com.google.common.collect.MapMaker;

/**
 * The GdlPool manages the creation of {@link Gdl} objects. It is the only way Gdl
 * objects may be created. It ensures that for each possible sentence, rule, or
 * fragment of GDL, only one corresponding Gdl object is created. This means Gdl
 * objects may be checked for equality with an instance-equality check (==) rather
 * than a more expensive recursive equality check.
 * <p>
 * A int-lived game player may accumulate lots of objects in its pool. To remove
 * them, it may call {@link #drainPool()} in between games. Note that if this
 * method is called while references to Gdl objects other than keyword constants
 * are held elsewhere, bad things will happen.
 */
class GdlPool
{
    def final ConcurrentMap<GdlTerm, ConcurrentMap<GdlTerm, GdlDistinct>> distinctPool = new ConcurrentHashMap<GdlTerm, ConcurrentMap<GdlTerm, GdlDistinct>>();
    def final ConcurrentMap<GdlConstant, ConcurrentMap<List<GdlTerm>, GdlFunction>> functionPool = new ConcurrentHashMap<GdlConstant, ConcurrentMap<List<GdlTerm>, GdlFunction>>();
    def final ConcurrentMap<GdlLiteral, GdlNot> notPool = new ConcurrentHashMap<GdlLiteral, GdlNot>();
    def final ConcurrentMap<List<GdlLiteral>, GdlOr> orPool = new ConcurrentHashMap<List<GdlLiteral>, GdlOr>();
    def final ConcurrentMap<GdlConstant, GdlProposition> propositionPool = new ConcurrentHashMap<GdlConstant, GdlProposition>();
    def final ConcurrentMap<GdlConstant, ConcurrentMap<List<GdlTerm>, GdlRelation>> relationPool = new ConcurrentHashMap<GdlConstant, ConcurrentMap<List<GdlTerm>, GdlRelation>>();
    def final ConcurrentMap<GdlSentence, ConcurrentMap<List<GdlLiteral>, GdlRule>> rulePool = new ConcurrentHashMap<GdlSentence, ConcurrentMap<List<GdlLiteral>, GdlRule>>();
    def final ConcurrentMap<String, GdlVariable> variablePool = new ConcurrentHashMap<String, GdlVariable>();
    def final ConcurrentMap<String, GdlConstant> constantPool = new ConcurrentHashMap<String, GdlConstant>();
    //Access to constantCases and variableCases should be synchronized using their monitor locks.
    def final Map<String,String> constantCases = new TreeMap<String,String>(String.CASE_INSENSITIVE_ORDER);
    def final Map<String,String> variableCases = new TreeMap<String,String>(String.CASE_INSENSITIVE_ORDER);

    // Controls whether we normalize the case of incoming constants and variables.
    def volatile bool caseSensitive = true;

    // Special keyword constants. These are never drained between games and are always
    // represented as lower-case so that they can easily be referred to internally and
    // so that all of the "true" objects are equal to each other in the Java == sense.
    // For example, attempting to create a GdlConstant "TRUE" will return the same constant
    // as if one had attempted to create the GdlConstant "true", regardless of whether the
    // game-specific constants are case-sensitive or not. These special keywords are never
    // sent over the network in PLAY requests and responses, so this should be safe.
    def final ImmutableSet<String> KEYWORDS = ImmutableSet.of(
    		"init","true","next","role","does","goal","legal","terminal","base","input","_");
    BASE = getConstant("base")  # GdlConstant 
    DOES = getConstant("does")  # GdlConstant 
    GOAL = getConstant("goal")  # GdlConstant 
    INIT = getConstant("init")  # GdlConstant 
    INPUT = getConstant("input")  # GdlConstant 
    LEGAL = getConstant("legal")  # GdlConstant 
    NEXT = getConstant("next")  # GdlConstant 
    ROLE = getConstant("role")  # GdlConstant 
    TERMINAL = getConstant("terminal")  # GdlConstant 
    TRUE = getConstant("true")  # GdlConstant 
    /**
     * Represents a single underscore ("_"). The underscore is not a GDL keyword, but
     * it's used by SentenceForms and is generally convenient for utility methods.
     */
    UNDERSCORE = getConstant("_")  # GdlConstant 

    private GdlPool():
    	// Not instantiable
    }

    /**
	 * Drains the contents of the GdlPool. Useful to control memory usage
	 * once you have finished playing a large game.
	 *
	 * WARNING: Should only be called *between games*, when there are no
	 * references to Gdl objects (other than keyword constants) outside the
	 * pool.
	 */
    def static void drainPool():
	    distinctPool.clear();
	    functionPool.clear();
	    notPool.clear();
	    orPool.clear();
	    propositionPool.clear();
	    relationPool.clear();
	    rulePool.clear();
	    variablePool.clear();
	    synchronized (variableCases):
	    	variableCases.clear();
	    }

	    // When draining the pool between matches, we still need to preserve the keywords
	    // since there are global references to them. For example, the Prover state machine
	    // has a reference to the GdlConstant "true", and that reference must still point
	    // to the authoritative GdlConstant "true" after the pool is drained and another
	    // game has begun. As such, when draining the constant pool, these special keywords
	    // are set aside and returned to the pool after all of the other constants (which
	    // were game-specific) have been drained.
	    Map<String, GdlConstant> keywordConstants = new HashMap<String, GdlConstant>();
	    for (String keyword : KEYWORDS):
	    	keywordConstants.put(keyword, GdlPool.getConstant(keyword));
	    }
	    synchronized (constantCases):
	    	constantPool.clear();
	    	constantCases.clear();
	    	for (Map.Entry<String,GdlConstant> keywordEntry : keywordConstants.entrySet()):
	    		constantCases.put(keywordEntry.getKey(), keywordEntry.getKey());
	    		constantPool.put(keywordEntry.getKey(), keywordEntry.getValue());
	    	}
	    }

	/**
	 * If the pool does not have a mapping for the given key, adds a mapping from key to value
	 * to the pool.
	 *
	 * Note that even if you've checked to make sure that the pool doesn't contain the key,
	 * you still shouldn't assume that this method actually inserts the given value, since
	 * this class is accessed by multiple threads simultaneously.
	 *
	 * @return the value mapped to by key in the pool
	 */
    private static <K,V> V addToPool(K key, V value, ConcurrentMap<K, V> pool):
        V prevValue = pool.putIfAbsent(key, value);
        if(prevValue == null)
            return value;
        else
            return prevValue;

    def static GdlConstant getConstant(String value)
	{
        if (KEYWORDS.contains(value.toLowerCase())):
            value = value.toLowerCase();
	    if (!caseSensitive):
	    	synchronized (constantCases):
	    		if (constantCases.containsKey(value)):
	    			value = constantCases.get(value);
	    		} else {
	    			constantCases.put(value, value);
	    		}
	    	}
	    }

        GdlConstant ret = constantPool.get(value);
        if(ret == null)
            ret = addToPool(value, new GdlConstant(value), constantPool);
        return ret;

    def GdlVariable getVariable(String name)
    {
        if (!caseSensitive):
        	synchronized (variableCases):
        		if (variableCases.containsKey(name)):
        			name = variableCases.get(name);
        		} else {
        			variableCases.put(name, name);
        		}
        	}
        }

        GdlVariable ret = variablePool.get(name);
        if(ret == null)
            ret = addToPool(name, new GdlVariable(name), variablePool);
        return ret;
    }

    def static GdlDistinct getDistinct(GdlTerm arg1, GdlTerm arg2)
	{
        ConcurrentMap<GdlTerm, GdlDistinct> bucket = distinctPool.get(arg1);
        if(bucket == null)
            bucket = addToPool(arg1, new ConcurrentHashMap<GdlTerm, GdlDistinct>(), distinctPool);

        GdlDistinct ret = bucket.get(arg2);
        if(ret == null)
            ret = addToPool(arg2, new GdlDistinct(arg1, arg2), bucket);

        return ret;

    def static GdlFunction getFunction(GdlConstant name)
	{
        List<GdlTerm> empty = Collections.emptyList();
        return getFunction(name, empty);

    def static GdlFunction getFunction(GdlConstant name, GdlTerm[] body)
	{
        return getFunction(name, Arrays.asList(body));

    def static GdlFunction getFunction(GdlConstant name, List<GdlTerm> body)
	{
        ConcurrentMap<List<GdlTerm>, GdlFunction> bucket = functionPool.get(name);
        if(bucket == null):
            ConcurrentMap<List<GdlTerm>, GdlFunction> newMap = new MapMaker().softValues().makeMap();
            bucket = addToPool(name, newMap, functionPool);

        GdlFunction ret = bucket.get(body);
        if(ret == null):
		    body = getImmutableCopy(body);
            ret = addToPool(body, new GdlFunction(name, body), bucket);

        return ret;

    def static GdlNot getNot(GdlLiteral body)
	{
        GdlNot ret = notPool.get(body);
        if(ret == null)
            ret = addToPool(body, new GdlNot(body), notPool);

        return ret;

    def static GdlOr getOr(GdlLiteral[] disjuncts)
	{
        return getOr(Arrays.asList(disjuncts));

    def static GdlOr getOr(List<GdlLiteral> disjuncts)
	{
        GdlOr ret = orPool.get(disjuncts);
        if(ret == null):
		    disjuncts = getImmutableCopy(disjuncts);
            ret = addToPool(disjuncts, new GdlOr(disjuncts), orPool);

        return ret;

    def static GdlProposition getProposition(GdlConstant name)
	{
        GdlProposition ret = propositionPool.get(name);
        if(ret == null)
            ret = addToPool(name, new GdlProposition(name), propositionPool);

        return ret;

    def static GdlRelation getRelation(GdlConstant name)
	{
        List<GdlTerm> empty = Collections.emptyList();
        return getRelation(name, empty);

    def static GdlRelation getRelation(GdlConstant name, GdlTerm[] body)
	{
        return getRelation(name, Arrays.asList(body));

    def static GdlRelation getRelation(GdlConstant name, List<GdlTerm> body)
	{
        ConcurrentMap<List<GdlTerm>, GdlRelation> bucket = relationPool.get(name);
        if(bucket == null):
            ConcurrentMap<List<GdlTerm>, GdlRelation> newMap = new MapMaker().softValues().makeMap();
            bucket = addToPool(name, newMap, relationPool);

        GdlRelation ret = bucket.get(body);
        if(ret == null):
		    body = getImmutableCopy(body);
            ret = addToPool(body, new GdlRelation(name, body), bucket);

        return ret;

    def static GdlRule getRule(GdlSentence head)
	{
        List<GdlLiteral> empty = Collections.emptyList();
        return getRule(head, empty);

    def static GdlRule getRule(GdlSentence head, GdlLiteral[] body)
	{
        return getRule(head, Arrays.asList(body));

    def static GdlRule getRule(GdlSentence head, List<GdlLiteral> body)
	{
        ConcurrentMap<List<GdlLiteral>, GdlRule> bucket = rulePool.get(head);
        if(bucket == null)
            bucket = addToPool(head, new ConcurrentHashMap<List<GdlLiteral>, GdlRule>(), rulePool);

        GdlRule ret = bucket.get(body);
        if(ret == null):
		    body = getImmutableCopy(body);
            ret = addToPool(body, new GdlRule(head, body), bucket);

        return ret;

    private static <T> List<T> getImmutableCopy(List<T> list):
	    return Collections.unmodifiableList(new ArrayList<T>(list));

	/**
	 * This method should only rarely be used. It takes a foreign GDL object
	 * (one that wasn't constructed through the GdlPool) and returns a version
	 * that lives in the GdlPool. Various parts of the prover infrastructure
	 * expect that all GDL objects live in the GdlPool, and so it's important
	 * that any foreign GDL objects created outside the GdlPool be immersed
	 * before being used. Since every GDL object should be created through the
	 * GdlPool, immerse should only need to be called on GDL that appears from
	 * outside sources: for example, being deserialized from a file.
	 */
    def static Gdl immerse(Gdl foreignGdl):
        if(foreignGdl instanceof GdlDistinct):
            return GdlPool.getDistinct((GdlTerm)immerse(((GdlDistinct) foreignGdl).getArg1()), (GdlTerm)immerse(((GdlDistinct) foreignGdl).getArg2()));
        } else if(foreignGdl instanceof GdlNot):
            return GdlPool.getNot((GdlLiteral)immerse(((GdlNot) foreignGdl).getBody()));
        } else if(foreignGdl instanceof GdlOr):
            GdlOr or = (GdlOr)foreignGdl;
            List<GdlLiteral> rval = new ArrayList<GdlLiteral>();
            for(int i=0; i<or.arity(); i++)
            {
                rval.add((GdlLiteral) immerse(or.get(i)));
            }
            return GdlPool.getOr(rval);
        } else if(foreignGdl instanceof GdlProposition):
            return GdlPool.getProposition((GdlConstant)immerse(((GdlProposition) foreignGdl).getName()));
        } else if(foreignGdl instanceof GdlRelation):
            GdlRelation rel = (GdlRelation)foreignGdl;
            List<GdlTerm> rval = new ArrayList<GdlTerm>();
            for(int i=0; i<rel.arity(); i++)
            {
                rval.add((GdlTerm) immerse(rel.get(i)));
            }
            return GdlPool.getRelation((GdlConstant)immerse(rel.getName()), rval);
        } else if(foreignGdl instanceof GdlRule):
            GdlRule rule = (GdlRule)foreignGdl;
            List<GdlLiteral> rval = new ArrayList<GdlLiteral>();
            for(int i=0; i<rule.arity(); i++)
            {
                rval.add((GdlLiteral) immerse(rule.get(i)));
            }
            return GdlPool.getRule((GdlSentence) immerse(rule.getHead()), rval);
        } else if(foreignGdl instanceof GdlConstant):
            return GdlPool.getConstant(((GdlConstant) foreignGdl).getValue());
        } else if(foreignGdl instanceof GdlFunction):
            GdlFunction func = (GdlFunction)foreignGdl;
            List<GdlTerm> rval = new ArrayList<GdlTerm>();
            for(int i=0; i<func.arity(); i++)
            {
                rval.add((GdlTerm) immerse(func.get(i)));
            }
            return GdlPool.getFunction((GdlConstant) immerse(func.getName()), rval);
        } else if(foreignGdl instanceof GdlVariable):
            return GdlPool.getVariable(((GdlVariable) foreignGdl).getName());
        } else
            throw new RuntimeException("Uh oh, gdl hierarchy must have been extended without updating this code.");
