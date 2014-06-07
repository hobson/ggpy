#!/usr/bin/env python
""" generated source for module SentenceDomainModelFactory """
# package: org.ggp.base.util.gdl.model
import java.util.List

import java.util.Map

import org.ggp.base.util.gdl.grammar.Gdl

class SentenceDomainModelFactory(object):
    """ generated source for class SentenceDomainModelFactory """
    @classmethod
    def createWithCartesianDomains(cls, description):
        """ generated source for method createWithCartesianDomains """
        formModel = SentenceFormModelFactory.create(description)
        sentenceFormsFinder = SentenceFormsFinder(formModel.getDescription())
        domains = sentenceFormsFinder.findCartesianDomains()
        return ImmutableSentenceDomainModel.create(formModel, domains)

