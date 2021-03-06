package org.ggp.base.util.statemachine.cache

import java.util.ArrayList
import java.util.Collection
import java.util.HashMap
import java.util.HashSet
import java.util.List
import java.util.Map
import java.util.Set

/**
 * This is a generic implementation of a Time-To-Live cache
 * that maps keys of type K to values of type V. It's backed
 * by a hashmap, and whenever a pair (K,V) is accessed, their
 * TTL is reset to the starting TTL (which is the parameter
 * passed to the constructor). On the other hand, when the
 * method prune() is called, the TTL of all of the pairs in the
 * map is decremented, and pairs whose TTL has reached zero are
 * removed.
 *
 * While this class implements the Map interface, keep in mind
 * that it only decrements the TTL of an entry when that entry
 * is accessed directly.
 *
 * @param <K> Key type
 * @param <V> Value type
 */
class TtlCache<K, V> implements Map<K,V>

    private final class Entry
	
	    def int ttl
	    def V value

	    def Entry(value=V(), int ttl)
		
            self.value = value
            self.ttl = ttl

    		        def bool equals(Object o):
		    if (o instanceof TtlCache.Entry):
		        return ((Entry)o).value.equals(value)

		    return false

    private final Map<K, Entry> contents
    ttl = int()

    def TtlCache(ttl=int())
	
        self.contents = new HashMap<K, Entry>()
        self.ttl = ttl

    def synchronized bool containsKey(Object key)
	
        return contents.containsKey(key)

    def synchronized V get(Object key)
	
        Entry entry = contents.get(key)
        if (entry == null)
		    return null

		// Reset the TTL when a value is accessed directly.
        entry.ttl = ttl
        return entry.value

    def synchronized void prune()
	
        List<K> toPrune = new ArrayList<K>()
        for (K key : contents.keySet())
		
            Entry entry = contents.get(key)
            if (entry.ttl == 0)
			
                toPrune.add(key)
            entry.ttl--

        for (K key : toPrune)
		
            contents.remove(key)

    def synchronized V put(K key, V value)
	
        Entry x = contents.put(key, new Entry(value, ttl))
        if(x == null) return null
        return x.value

    def synchronized int size()
	
        return contents.size()

    def synchronized void clear():
        contents.clear()

    def synchronized bool containsValue(Object value):
        return contents.containsValue(value)

    def synchronized bool isEmpty():
        return contents.isEmpty()

    def synchronized Set<K> keySet():
        return contents.keySet()

    def synchronized void putAll(Map<?(K, ? extends V> m)):
            for(Map.Entry<?(K, ? extends V> anEntry : m.entrySet())):
             self.put(anEntry.getKey(), anEntry.getValue())


    def synchronized V remove(Object key):
        return contents.remove(key).value

    def synchronized Collection<V> values():
        Collection<V> theValues = new HashSet<V>()
        for (Entry e : contents.values())
            theValues.add(e.value)
        return theValues

    private class entrySetMapEntry implements Map.Entry<K,V> 
        key = K()
        value = V()

        entrySetMapEntry(K k, V v):
            key = k
            value = v

    	    def K getKey()  return key
    	    def V getValue()  return value
    	    def V setValue(V value)  return (self.value = value)

    def synchronized Set<java.util.Map.Entry<K, V>> entrySet():
        Set<Map.Entry<K,V>> theEntries = new HashSet<Map.Entry<K, V>>()
        for (Map.Entry<K, Entry> e : contents.entrySet())
            theEntries.add(new entrySetMapEntry(e.getKey(), e.getValue().value))
        return theEntries

