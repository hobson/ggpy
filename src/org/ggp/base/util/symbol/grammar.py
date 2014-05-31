#!/usr/bin/env python
# package: org.ggp.base.util.symbol.grammar

import threading

class SymbolFormatException(Exception):
    source = ''

    def __init__(self, message, source):
        super(SymbolFormatException, self).__init__(message)
        self.source = source

    def getSource(self):
        return self.source

    def __str__(self):
        return "Improperly formatted symbolic expression: " + self.source



class Symbol(object):
    def __str__(self):
        pass

class SymbolAtom(Symbol):
    def __init__(self, value=None):
        super(SymbolAtom, self).__init__()
        self.value = value.intern() if not value is None else ''

    def getValue(self):
        return self.value

    def __str__(self):
        return self.value


class SymbolList(Symbol):  # odd that this is a derived class and not a container for Symbol objects
    '''List container for Symbol objects (self.contents = [Symbol(), Symbol(), ...])
    
    Java     -> Python
    size     -> __len__
    toString -> __str__
    '''
    def __init__(self, contents):
        super(SymbolList, self).__init__()
        self.contents = contents

    def get(self, index):
        """ generated source for method get """
        return self.contents.get(index)

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        if self.contents:
            return '( ' + ' '.join([str(sym) for sym in self.contents]) + ' )'
        else:
            return '( )'


class SymbolPool(object):
    '''A pair of dicts/pools with a thread-safe add_key_value_if_absent() operations
    
    Python dicts and lists are already single-operation (atomic) thread-safe
    nonatomic operations for lists (L) and dicts (D) include:

        i = i+1
        L.append(L[-1])
        L[i] = L[j]
        D[x] = D[x] + 1
    
    SymbolPool uses a lock (GIL?) to perform multiple operations on a dict/list thread-safely
    Here's how you'd do the same for the D[x] operation above:

        import threading
        lock = threading.Lock()
        lock.acquire() 
        D[x] = D[x] + 1
        lock.release()
    '''

    # WARNING: mutable class attributes will be shared across instances!
    atomPool = {} 
    listPool = {} 
   
    # `classmethod`s can be overridden by any classes that inherit SymbolPool
    # and are shared among instances. otherwise they are the same as instance
    # methods. `staticmethod`s are just non-global functions and don't need to access
    # the class
    @staticmethod  
    def addToPool(key, value, pool):
        """ Add key-value to `dict` `pool` if `pool` does not yet have one for that key

        value :: a list of Symbol objects (SymbolList)
        pool  :: a dictionary of atoms or symbol lists stored in this SymbolPool class

        Sam says, "Even if you've checked to make sure that the pool doesn't contain the key,
        you still shouldn't assume that this method actually inserts the given value, since
        this class is accessed by multiple threads simultaneously."

        @return the value associated with the key in the pool
        """
        # added by HL to avoid the unthreadsafe behavior described by Sam above
        lock = threading.Lock()
        lock.aquire()
        prev_value = pool.get(key)
        if prev_value is None:
            pool[key] = value
            lock.release()
            return value
        lock.release()
        return prev_value

    @classmethod
    def getAtom(cls, value):
        '''Add an atom to the atomPool if it isn't already there, return the value if there'''
        ret = cls.atomPool.get(value)
        if ret is None:
            ret = cls.addToPool(value, SymbolAtom(value), cls.atomPool)
        return ret

    @classmethod
    def getList(cls, contents):
        """contents is a SymbolList or list of symbols"""
        ret = cls.listPool.get(contents)
        if ret == None:
            ret = cls.addToPool(contents, SymbolList(contents), cls.listPool)
        return ret

    # no need to overload in python just treat the Array like a List and it should just work!
    # @classmethod
    # @getList.register(object, Symbol)
    # def getList_0(cls, contents):
    #     """ generated source for method getList_0 """
    #     return cls.getList(Arrays.asList(contents))

    @classmethod
    def drainPool(cls):
        '''Drains the contents of the SymbolPool. Useful to control memory usage.

        Sam says, "Once you've finished playing a large game, this should be safe to call
        any time during gameplay. But my experiments indicate that SymbolPool
        has a 97% cache hit rate during a game, so you likely only want to call
        this between games, because symbols from previous game are unlikely to
        reappear in subsequent, unrelated games.""
        '''
        cls.atomPool = dict()
        cls.listPool = dict()


class SymbolFactory(object):
    @classmethod
    def create(cls, string):
        try:
            return cls.convert(LinkedList(tokens))
        except Exception as e:
            raise SymbolFormatException(string)

    #  Private, implementation-specific methods below here 
    @classmethod
    def convert(cls, tokens):
        """ generated source for method convert """
        if tokens.getFirst() == "(":
            return convertList(tokens)
        else:
            return convertAtom(tokens)

    @classmethod
    def convertAtom(cls, tokens):
        """ generated source for method convertAtom """
        return SymbolPool.getAtom(tokens.removeFirst())

    @classmethod
    def convertList(cls, tokens):
        """ generated source for method convertList """
        contents = ArrayList()
        tokens.removeFirst()
        while not tokens.getFirst() == "":  # java2python added an extra close-paren
            contents.add(cls.convert(tokens))
        tokens.removeFirst()
        return SymbolPool.getList(contents)

    @classmethod
    def lex(cls, string):
        """ generated source for method lex """
        tokens = ArrayList()
        for token in string.split(" "):
            tokens.add(token)
        return tokens

    @classmethod
    def preprocess(cls, string):
        """ generated source for method preprocess """
        string = string.replaceAll("\\(", " ( ")
        string = string.replaceAll("\\)", " ) ")
        string = string.replaceAll("\\s+", " ")
        string = string.trim()
        return string

