#!/usr/bin/env python
""" generated source for module AbstractSentenceDomainModel """
# package: org.ggp.base.util.gdl.model
import java.util.List

import java.util.Set

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import com.google.common.collect.Multimap

# 
#  * Allows SentenceDomainModels to delegate their SentenceFormModel aspects
#  * to an existing SentenceFormModel.
#  
class AbstractSentenceDomainModel(SentenceDomainModel):
    """ generated source for class AbstractSentenceDomainModel """
    formModel = SentenceFormModel()

    def __init__(self, formModel):
        """ generated source for method __init__ """
        super(AbstractSentenceDomainModel, self).__init__()
        self.formModel = formModel

    # package-private
    def getFormModel(self):
        """ generated source for method getFormModel """
        return self.formModel

    def getIndependentSentenceForms(self):
        """ generated source for method getIndependentSentenceForms """
        return self.formModel.getIndependentSentenceForms()

    def getConstantSentenceForms(self):
        """ generated source for method getConstantSentenceForms """
        return self.formModel.getConstantSentenceForms()

    def getDependencyGraph(self):
        """ generated source for method getDependencyGraph """
        return self.formModel.getDependencyGraph()

    def getSentencesListedAsTrue(self, form):
        """ generated source for method getSentencesListedAsTrue """
        return self.formModel.getSentencesListedAsTrue(form)

    def getRules(self, form):
        """ generated source for method getRules """
        return self.formModel.getRules(form)

    def getSentenceForms(self):
        """ generated source for method getSentenceForms """
        return self.formModel.getSentenceForms()

    def getDescription(self):
        """ generated source for method getDescription """
        return self.formModel.getDescription()

    def getSentenceForm(self, sentence):
        """ generated source for method getSentenceForm """
        return self.formModel.getSentenceForm(sentence)

