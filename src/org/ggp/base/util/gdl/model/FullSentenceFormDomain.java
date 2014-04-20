package org.ggp.base.util.gdl.model

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

/**
 * A @link SentenceFormDomain} implementation that stores every possible
 * version of the sentence.
 */
class FullSentenceFormDomain(SentenceFormDomain):
    form = SentenceForm()
    private final ImmutableList<GdlSentence> domain
    private final ImmutableList<ImmutableSet<GdlConstant>> domainsForSlots

    def FullSentenceFormDomain(
            SentenceForm form,
            ImmutableList<GdlSentence> domain,
            ImmutableList<ImmutableSet<GdlConstant>> domainsForSlots):
        self.form = form
        self.domain = domain
        self.domainsForSlots = domainsForSlots

    def static FullSentenceFormDomain create(SentenceForm form, Collection<GdlSentence> domain):
        List<ImmutableSet.Builder<GdlConstant>> domainsForSlotsBuilder = Lists.newArrayList()
        for (int i = 0; i < form.getTupleSize(); i++):
            domainsForSlotsBuilder.add(ImmutableSet.<GdlConstant>builder())
        for (GdlSentence sentence : domain):
            assert form.matches(sentence)
            List<GdlConstant> tuple = GdlUtils.getTupleFromGroundSentence(sentence)
            if (tuple.size() != form.getTupleSize()):
                throw new IllegalArgumentException()
            for (int i = 0; i < tuple.size(); i++):
                GdlConstant constant = tuple.get(i)
                domainsForSlotsBuilder.get(i).add(constant)
        ImmutableList.Builder<ImmutableSet<GdlConstant>> domainsForSlots = ImmutableList.builder()
        for (ImmutableSet.Builder<GdlConstant> builder : domainsForSlotsBuilder):
            domainsForSlots.add(builder.build())
        return new FullSentenceFormDomain(form, ImmutableList.copyOf(domain),
                domainsForSlots.build())

    def Iterator<GdlSentence> iterator():
        return domain.iterator()

    def getForm():  # SentenceForm
        return form

    def Set<GdlConstant> getDomainForSlot(int slotIndex):
        Preconditions.checkElementIndex(slotIndex, form.getTupleSize())
        return domainsForSlots.get(slotIndex)
