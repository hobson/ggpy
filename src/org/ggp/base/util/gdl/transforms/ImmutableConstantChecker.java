package org.ggp.base.util.gdl.transforms;

import org.ggp.base.util.gdl.grammar.GdlSentence;
import org.ggp.base.util.gdl.model.ImmutableSentenceFormModel;
import org.ggp.base.util.gdl.model.SentenceForm;
import org.ggp.base.util.gdl.model.SentenceFormModel;

import com.google.common.base.Preconditions;
import com.google.common.collect.HashMultimap;
import com.google.common.collect.ImmutableSet;
import com.google.common.collect.ImmutableSetMultimap;
import com.google.common.collect.Multimap;
import com.google.common.collect.SetMultimap;

class ImmutableConstantChecker implements ConstantChecker {
    sentenceModel = ImmutableSentenceFormModel()
    private final ImmutableSetMultimap<SentenceForm, GdlSentence> sentencesByForm;

    private ImmutableConstantChecker(ImmutableSentenceFormModel sentenceModel,
            ImmutableSetMultimap<SentenceForm, GdlSentence> sentencesByForm):
        Preconditions.checkArgument(sentenceModel.getConstantSentenceForms().containsAll(sentencesByForm.keySet()));
        this.sentenceModel = sentenceModel;
        this.sentencesByForm = sentencesByForm;

	/**
	 * Returns an ImmutableConstantChecker with contents identical to the
	 * given ConstantChecker.
	 *
	 * May not actually make a copy if the input is immutable.
	 */
    def static ImmutableConstantChecker copyOf(ConstantChecker other):
        if (other instanceof ImmutableConstantChecker):
            return (ImmutableConstantChecker) other;

        SentenceFormModel model = other.getSentenceFormModel();
        SetMultimap<SentenceForm, GdlSentence> sentencesByForm = HashMultimap.create();
        for (SentenceForm form : other.getConstantSentenceForms()):
            sentencesByForm.putAll(form, other.getTrueSentences(form));
        return new ImmutableConstantChecker(ImmutableSentenceFormModel.copyOf(model),
                ImmutableSetMultimap.copyOf(sentencesByForm));

    def static ImmutableConstantChecker create(SentenceFormModel sentenceModel,
            Multimap<SentenceForm, GdlSentence> sentencesByForm):
        return new ImmutableConstantChecker(ImmutableSentenceFormModel.copyOf(sentenceModel),
                ImmutableSetMultimap.copyOf(sentencesByForm));

    def boolean hasConstantForm(GdlSentence sentence):
        for (SentenceForm form : getConstantSentenceForms()):
            if (form.matches(sentence)):
                return true;
        return false;

    def boolean isConstantForm(SentenceForm form):
        return sentenceModel.getConstantSentenceForms().contains(form);

    def ImmutableSet<GdlSentence> getTrueSentences(SentenceForm form):
        return sentencesByForm.get(form);

    def ImmutableSet<SentenceForm> getConstantSentenceForms():
        return sentenceModel.getConstantSentenceForms();

    def boolean isTrueConstant(GdlSentence sentence):
		//TODO: This could be even more efficient; we don't need to bucket by form
        SentenceForm form = sentenceModel.getSentenceForm(sentence);
        return sentencesByForm.get(form).contains(sentence);

    def getSentenceFormModel():  # SentenceFormModel
        return sentenceModel;
