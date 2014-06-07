#!/usr/bin/env python
""" generated source for module ImmutableSentenceDomainModel """
# package: org.ggp.base.util.gdl.model
import java.util.List

import java.util.Map

import java.util.Set

import org.ggp.base.util.gdl.grammar.GdlConstant

import com.google.common.collect.ImmutableMap

import com.google.common.collect.Lists

class ImmutableSentenceDomainModel(AbstractSentenceDomainModel):
    """ generated source for class ImmutableSentenceDomainModel """
    domains = ImmutableMap()

    def __init__(self, formModel, domains):
        """ generated source for method __init__ """
        super(ImmutableSentenceDomainModel, self).__init__(formModel)
        if not formModel.getSentenceForms() == domains.keySet():
            raise IllegalArgumentException()
        self.domains = domains

    @classmethod
    def create(cls, formModel, domains):
        """ generated source for method create """
        return ImmutableSentenceDomainModel(ImmutableSentenceFormModel.copyOf(formModel), ImmutableMap.copyOf(domains))

    @classmethod
    def copyUsingCartesianDomains(cls, otherModel):
        """ generated source for method copyUsingCartesianDomains """
        if isinstance(otherModel, (ImmutableSentenceDomainModel, )):
            return otherModel
        domains = ImmutableMap.builder()
        for form in otherModel.getSentenceForms():
            while i < form.getTupleSize():
                domainsForSlots.add(otherDomain.getDomainForSlot(i))
                i += 1
            domains.put(form, CartesianSentenceFormDomain.create(form, domainsForSlots))
        return ImmutableSentenceDomainModel(ImmutableSentenceFormModel.copyOf(otherModel), domains.build())

    def getDomain(self, form):
        """ generated source for method getDomain """
        return self.domains.get(form)

