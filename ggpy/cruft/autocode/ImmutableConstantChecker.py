#!/usr/bin/env python
""" generated source for module ImmutableConstantChecker """
# package: org.ggp.base.util.gdl.transforms
import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.model.ImmutableSentenceFormModel

import org.ggp.base.util.gdl.model.SentenceForm

import org.ggp.base.util.gdl.model.SentenceFormModel

import com.google.common.base.Preconditions

import com.google.common.collect.HashMultimap

import com.google.common.collect.ImmutableSet

import com.google.common.collect.ImmutableSetMultimap

import com.google.common.collect.Multimap

import com.google.common.collect.SetMultimap

class ImmutableConstantChecker(ConstantChecker):
    """ generated source for class ImmutableConstantChecker """
    sentenceModel = ImmutableSentenceFormModel()
    sentencesByForm = ImmutableSetMultimap()

    def __init__(self, sentenceModel, sentencesByForm):
        """ generated source for method __init__ """
        super(ImmutableConstantChecker, self).__init__()
        Preconditions.checkArgument(sentenceModel.getConstantSentenceForms().containsAll(sentencesByForm.keySet()))
        self.sentenceModel = sentenceModel
        self.sentencesByForm = sentencesByForm

    # 
    # 	 * Returns an ImmutableConstantChecker with contents identical to the
    # 	 * given ConstantChecker.
    # 	 *
    # 	 * May not actually make a copy if the input is immutable.
    # 	 
    @classmethod
    def copyOf(cls, other):
        """ generated source for method copyOf """
        if isinstance(other, (ImmutableConstantChecker, )):
            return other
        model = other.getSentenceFormModel()
        sentencesByForm = HashMultimap.create()
        for form in other.getConstantSentenceForms():
            sentencesByForm.putAll(form, other.getTrueSentences(form))
        return ImmutableConstantChecker(ImmutableSentenceFormModel.copyOf(model), ImmutableSetMultimap.copyOf(sentencesByForm))

    @classmethod
    def create(cls, sentenceModel, sentencesByForm):
        """ generated source for method create """
        return ImmutableConstantChecker(ImmutableSentenceFormModel.copyOf(sentenceModel), ImmutableSetMultimap.copyOf(sentencesByForm))

    def hasConstantForm(self, sentence):
        """ generated source for method hasConstantForm """
        for form in getConstantSentenceForms():
            if form.matches(sentence):
                return True
        return False

    def isConstantForm(self, form):
        """ generated source for method isConstantForm """
        return self.sentenceModel.getConstantSentenceForms().contains(form)

    def getTrueSentences(self, form):
        """ generated source for method getTrueSentences """
        return self.sentencesByForm.get(form)

    def getConstantSentenceForms(self):
        """ generated source for method getConstantSentenceForms """
        return self.sentenceModel.getConstantSentenceForms()

    def isTrueConstant(self, sentence):
        """ generated source for method isTrueConstant """
        # TODO: This could be even more efficient; we don't need to bucket by form
        form = self.sentenceModel.getSentenceForm(sentence)
        return self.sentencesByForm.get(form).contains(sentence)

    def getSentenceFormModel(self):
        """ generated source for method getSentenceFormModel """
        return self.sentenceModel

