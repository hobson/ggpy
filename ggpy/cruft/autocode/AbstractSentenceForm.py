#!/usr/bin/env python
""" generated source for module AbstractSentenceForm """
# package: org.ggp.base.util.gdl.model
import java.util.List

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlSentence

import com.google.common.base.Supplier

import com.google.common.base.Suppliers

import com.google.common.collect.Lists

# 
#  * Defines the hashCode, equals, and toString methods for SentenceForms so
#  * different SentenceForms can be compatible in terms of how they treat these
#  * methods. SentenceForm implementations should extend this class and should
#  * not reimplement hashCode, equals, or toString.
#  
class AbstractSentenceForm(SentenceForm):
    """ generated source for class AbstractSentenceForm """
    underscoreSentence = Suppliers.memoize(Supplier())

    def get(self):
        """ generated source for method get """
        underscores = getNUnderscores(getTupleSize())
        return getSentenceFromTuple(underscores)

    def equals(self, obj):
        """ generated source for method equals """
        if obj == None:
            return False
        if not (isinstance(obj, (SentenceForm, ))):
            return False
        o = obj
        if self.__name__ != o.__name__:
            return False
        if self.getTupleSize() != o.getTupleSize():
            return False
        return o.matches(self.underscoreSentence.get())

    @classmethod
    def getNUnderscores(cls, numTerms):
        """ generated source for method getNUnderscores """
        underscore = GdlPool.UNDERSCORE
        terms = Lists.newArrayListWithCapacity(numTerms)
        i = 0
        while i < numTerms:
            terms.add(underscore)
            i += 1
        return terms

    hashCode = 0

    def hashCode(self):
        """ generated source for method hashCode """
        if self.hashCode == 0:
            self.hashCode = toString().hashCode()
        return self.hashCode

    def __str__(self):
        """ generated source for method toString """
        return self.underscoreSentence.get().__str__()

