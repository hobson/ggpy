package org.ggp.base.util.gdl.model

import java.util.List
import java.util.Set

import org.ggp.base.util.gdl.grammar.Gdl
import org.ggp.base.util.gdl.grammar.GdlRule
import org.ggp.base.util.gdl.grammar.GdlSentence

import com.google.common.collect.Multimap

/**
 * Allows SentenceDomainModels to delegate their SentenceFormModel aspects
 * to an existing SentenceFormModel.
 */
def abstract class AbstractSentenceDomainModel(SentenceDomainModel):
    formModel = SentenceFormModel()

    protected AbstractSentenceDomainModel(SentenceFormModel formModel):
        self.formModel = formModel

	/*package-private*/ SentenceFormModel getFormModel():
        return formModel

    def Set<SentenceForm> getIndependentSentenceForms():
        return formModel.getIndependentSentenceForms()

    def Set<SentenceForm> getConstantSentenceForms():
        return formModel.getConstantSentenceForms()

    def Multimap<SentenceForm, SentenceForm> getDependencyGraph():
        return formModel.getDependencyGraph()

    def Set<GdlSentence> getSentencesListedAsTrue(SentenceForm form):
        return formModel.getSentencesListedAsTrue(form)

    def Set<GdlRule> getRules(SentenceForm form):
        return formModel.getRules(form)

    def Set<SentenceForm> getSentenceForms():
        return formModel.getSentenceForms()

    def List<Gdl> getDescription():
        return formModel.getDescription()

    def SentenceForm getSentenceForm(GdlSentence sentence):
        return formModel.getSentenceForm(sentence)
