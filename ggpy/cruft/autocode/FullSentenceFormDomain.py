#!/usr/bin/env python
""" generated source for module FullSentenceFormDomain """
# package: org.ggp.base.util.gdl.model
import java.util.Collection

import java.util.Iterator

import java.util.List

import java.util.Set

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlSentence

import com.google.common.base.Preconditions

import com.google.common.collect.ImmutableList

import com.google.common.collect.ImmutableSet

import com.google.common.collect.Lists

# 
#  * A {@link SentenceFormDomain} implementation that stores every possible
#  * version of the sentence.
#  
class FullSentenceFormDomain(SentenceFormDomain):
    """ generated source for class FullSentenceFormDomain """
    form = SentenceForm()
    domain = ImmutableList()
    domainsForSlots = ImmutableList()

    def __init__(self, form, domain, domainsForSlots):
        """ generated source for method __init__ """
        super(FullSentenceFormDomain, self).__init__()
        self.form = form
        self.domain = domain
        self.domainsForSlots = domainsForSlots

    @classmethod
    def create(cls, form, domain):
        """ generated source for method create """
        domainsForSlotsBuilder = Lists.newArrayList()
        i = 0
        while i < form.getTupleSize():
            domainsForSlotsBuilder.add(ImmutableSet.builder())
            i += 1
        for sentence in domain:
            assert form.matches(sentence)
            if len(tuple_) != form.getTupleSize():
                raise IllegalArgumentException()
            while i < len(tuple_):
                domainsForSlotsBuilder.get(i).add(constant)
                i += 1
        domainsForSlots = ImmutableList.builder()
        for builder in domainsForSlotsBuilder:
            domainsForSlots.add(builder.build())
        return FullSentenceFormDomain(form, ImmutableList.copyOf(domain), domainsForSlots.build())

    def iterator(self):
        """ generated source for method iterator """
        return self.domain.iterator()

    def getForm(self):
        """ generated source for method getForm """
        return self.form

    def getDomainForSlot(self, slotIndex):
        """ generated source for method getDomainForSlot """
        Preconditions.checkElementIndex(slotIndex, self.form.getTupleSize())
        return self.domainsForSlots.get(slotIndex)

