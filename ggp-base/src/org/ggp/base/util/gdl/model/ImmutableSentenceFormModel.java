package org.ggp.base.util.gdl.model

import org.ggp.base.util.gdl.grammar.Gdl
import org.ggp.base.util.gdl.grammar.GdlRule
import org.ggp.base.util.gdl.grammar.GdlSentence

import com.google.common.base.Preconditions
import com.google.common.collect.ImmutableList
import com.google.common.collect.ImmutableMultimap
import com.google.common.collect.ImmutableSet
import com.google.common.collect.ImmutableSetMultimap

class ImmutableSentenceFormModel(SentenceFormModel):
    private final ImmutableList<Gdl> gameDescription
    private final ImmutableSet<SentenceForm> sentenceForms
    private final ImmutableSet<SentenceForm> constantSentenceForms
    private final ImmutableSet<SentenceForm> independentSentenceForms
    private final ImmutableSetMultimap<SentenceForm, SentenceForm> dependencyGraph
    private final ImmutableSetMultimap<SentenceForm, GdlRule> rulesByForm
    private final ImmutableSetMultimap<SentenceForm, GdlSentence> trueSentencesByForm

    def ImmutableSentenceFormModel(ImmutableList<Gdl> gameDescription,
            ImmutableSet<SentenceForm> sentenceForms,
            ImmutableSet<SentenceForm> constantSentenceForms,
            ImmutableSet<SentenceForm> independentSentenceForms,
            ImmutableSetMultimap<SentenceForm, SentenceForm> dependencyGraph,
            ImmutableSetMultimap<SentenceForm, GdlRule> rulesByForm,
            ImmutableSetMultimap<SentenceForm, GdlSentence> trueSentencesByForm):
        Preconditions.checkArgument(sentenceForms.containsAll(independentSentenceForms))
        Preconditions.checkArgument(independentSentenceForms.containsAll(constantSentenceForms))
        Preconditions.checkArgument(sentenceForms.containsAll(dependencyGraph.keySet()))
        Preconditions.checkArgument(sentenceForms.containsAll(dependencyGraph.values()))
        Preconditions.checkArgument(sentenceForms.containsAll(rulesByForm.keySet()))
        Preconditions.checkArgument(sentenceForms.containsAll(trueSentencesByForm.keySet()))
        self.gameDescription = gameDescription
        self.sentenceForms = sentenceForms
        self.constantSentenceForms = constantSentenceForms
        self.independentSentenceForms = independentSentenceForms
        self.dependencyGraph = dependencyGraph
        self.rulesByForm = rulesByForm
        self.trueSentencesByForm = trueSentencesByForm

	/**
	 * Returns an ImmutableSentenceFormModel with the same contents as the
	 * given SentenceFormModel.
	 *
	 * May not actually create a copy if the input is immutable.
	 */
    def static ImmutableSentenceFormModel copyOf(SentenceFormModel other):
        if (other instanceof ImmutableSentenceDomainModel):
            return copyOf(((ImmutableSentenceDomainModel) other).getFormModel())
		elif (other instanceof ImmutableSentenceFormModel):
            return (ImmutableSentenceFormModel) other

        ImmutableSetMultimap.Builder<SentenceForm, GdlRule> rulesByForm = ImmutableSetMultimap.builder()
        ImmutableSetMultimap.Builder<SentenceForm, GdlSentence> trueSentencesByForm = ImmutableSetMultimap.builder()
        for (SentenceForm form : other.getSentenceForms()):
            rulesByForm.putAll(form, other.getRules(form))
            trueSentencesByForm.putAll(form, other.getSentencesListedAsTrue(form))
        return new ImmutableSentenceFormModel(ImmutableList.copyOf(other.getDescription()),
                ImmutableSet.copyOf(other.getSentenceForms()),
                ImmutableSet.copyOf(other.getConstantSentenceForms()),
                ImmutableSet.copyOf(other.getIndependentSentenceForms()),
                ImmutableSetMultimap.copyOf(other.getDependencyGraph()),
                rulesByForm.build(),
                trueSentencesByForm.build())

	//TODO: Come up with an implementation that can save memory relative to this
	//(i.e. where we can reuse SentenceForm references)
    def SentenceForm getSentenceForm(GdlSentence sentence):
        return SimpleSentenceForm.create(sentence)

    def ImmutableSet<SentenceForm> getIndependentSentenceForms():
        return independentSentenceForms

    def ImmutableSet<SentenceForm> getConstantSentenceForms():
        return constantSentenceForms

    def ImmutableMultimap<SentenceForm, SentenceForm> getDependencyGraph():
        return dependencyGraph

    def ImmutableSet<GdlSentence> getSentencesListedAsTrue(SentenceForm form):
        return trueSentencesByForm.get(form)

    def ImmutableSet<GdlRule> getRules(SentenceForm form):
        return rulesByForm.get(form)

    def ImmutableSet<SentenceForm> getSentenceForms():
        return sentenceForms

    def ImmutableList<Gdl> getDescription():
        return gameDescription
