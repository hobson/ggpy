#!/usr/bin/env python
""" generated source for module CartesianSentenceFormDomain """
# package: org.ggp.base.util.gdl.model
import java.util.Iterator

import java.util.List

import java.util.Set

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlSentence

import com.google.common.base.Function

import com.google.common.base.Preconditions

import com.google.common.collect.ImmutableList

import com.google.common.collect.ImmutableSet

import com.google.common.collect.Iterators

import com.google.common.collect.Lists

import com.google.common.collect.SetMultimap

import com.google.common.collect.Sets

# 
#  * A {@link SentenceFormDomain} implementation that stores which
#  * constant values are possible for each slot of a sentence form.
#  *
#  * This is a more compact representation than a {@link FullSentenceFormDomain},
#  * but has less expressive power.
#  
class CartesianSentenceFormDomain(SentenceFormDomain):
    """ generated source for class CartesianSentenceFormDomain """
    form = SentenceForm()
    domainsForSlots = ImmutableList()

    def __init__(self, form, domainsForSlots):
        """ generated source for method __init__ """
        super(CartesianSentenceFormDomain, self).__init__()
        self.form = form
        self.domainsForSlots = domainsForSlots

    @classmethod
    @overloaded
    def create(cls, form, domainsForSlots):
        """ generated source for method create """
        return CartesianSentenceFormDomain(form, ImmutableList.copyOf(Lists.transform(domainsForSlots, Function())))

    @classmethod
    @create.register(object, SentenceForm, SetMultimap)
    def create_0(cls, form, setMultimap):
        """ generated source for method create_0 """
        Preconditions.checkNotNull(setMultimap)
        domainsForSlots = Lists.newArrayList()
        i = 0
        while i < form.getTupleSize():
            domainsForSlots.add(setMultimap.get(i))
            i += 1
        return cls.create(form, domainsForSlots)

    def iterator(self):
        """ generated source for method iterator """
        return Iterators.transform(Sets.cartesianProduct(self.domainsForSlots).iterator(), Function())

    def getForm(self):
        """ generated source for method getForm """
        return self.form

    def getDomainForSlot(self, slotIndex):
        """ generated source for method getDomainForSlot """
        Preconditions.checkElementIndex(slotIndex, self.form.getTupleSize())
        return self.domainsForSlots.get(slotIndex)

