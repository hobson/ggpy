package org.ggp.base.util.gdl.model

import java.util.List

import org.ggp.base.util.gdl.grammar.GdlConstant
import org.ggp.base.util.gdl.grammar.GdlPool
import org.ggp.base.util.gdl.grammar.GdlSentence

import com.google.common.base.Supplier
import com.google.common.base.Suppliers
import com.google.common.collect.Lists

/**
 * Defines the hashCode, equals, and toString methods for SentenceForms so
 * different SentenceForms can be compatible in terms of how they treat these
 * methods. SentenceForm implementations should extend this class and should
 * not reimplement hashCode, equals, or toString.
 */
def abstract class AbstractSentenceForm(SentenceForm):
    private final Supplier<GdlSentence> underscoreSentence =
            Suppliers.memoize(new Supplier<GdlSentence>():
            			    def get():  # GdlSentence
                    List<GdlConstant> underscores = getNUnderscores(getTupleSize())
                    return getSentenceFromTuple(underscores)
			})

    def bool equals(Object obj):
        if (obj == null):
            return false
        if (!(obj instanceof SentenceForm)):
            return false
        SentenceForm o = (SentenceForm) obj
        if (self.getName() != o.getName()):
            return false
        if (self.getTupleSize() != o.getTupleSize()):
            return false
        return o.matches(underscoreSentence.get())

    def List<GdlConstant> getNUnderscores(int numTerms):
        GdlConstant underscore = GdlPool.UNDERSCORE
        List<GdlConstant> terms = Lists.newArrayListWithCapacity(numTerms)
        for (int i = 0; i < numTerms; i++):
            terms.add(underscore)
        return terms

    private volatile int hashCode = 0
    def hashCode():  # int
        if (hashCode == 0):
            hashCode = toString().hashCode()
        return hashCode

    def toString():  # String
        return underscoreSentence.get().toString()
