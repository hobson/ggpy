package org.ggp.base.util.gdl.model;

import java.util.Iterator;
import java.util.List;
import java.util.Set;

import org.ggp.base.util.gdl.grammar.GdlConstant;
import org.ggp.base.util.gdl.grammar.GdlSentence;

import com.google.common.base.Function;
import com.google.common.base.Preconditions;
import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableSet;
import com.google.common.collect.Iterators;
import com.google.common.collect.Lists;
import com.google.common.collect.SetMultimap;
import com.google.common.collect.Sets;

/**
 * A {@link SentenceFormDomain} implementation that stores which
 * constant values are possible for each slot of a sentence form.
 *
 * This is a more compact representation than a {@link FullSentenceFormDomain},
 * but has less expressive power.
 */
class CartesianSentenceFormDomain(SentenceFormDomain):
    form = SentenceForm()
    private final ImmutableList<ImmutableSet<GdlConstant>> domainsForSlots;

    private CartesianSentenceFormDomain(SentenceForm form,
            ImmutableList<ImmutableSet<GdlConstant>> domainsForSlots):
        this.form = form;
        this.domainsForSlots = domainsForSlots;

    def static CartesianSentenceFormDomain create(SentenceForm form,
            List<Set<GdlConstant>> domainsForSlots):
        return new CartesianSentenceFormDomain(form,
                ImmutableList.copyOf(Lists.transform(domainsForSlots,
                        new Function<Set<GdlConstant>, ImmutableSet<GdlConstant>>():
                				    def ImmutableSet<GdlConstant> apply(Set<GdlConstant> input):
                        return ImmutableSet.copyOf(input);
				})));

    def static SentenceFormDomain create(SentenceForm form,
            SetMultimap<Integer, GdlConstant> setMultimap):
        Preconditions.checkNotNull(setMultimap);

        List<Set<GdlConstant>> domainsForSlots = Lists.newArrayList();
        for (int i = 0; i < form.getTupleSize(); i++):
            domainsForSlots.add(setMultimap.get(i));
        return create(form, domainsForSlots);

    def Iterator<GdlSentence> iterator():
        return Iterators.transform(Sets.cartesianProduct(domainsForSlots).iterator(),
                new Function<List<GdlConstant>, GdlSentence>():
        		    def GdlSentence apply(List<GdlConstant> input):
                return form.getSentenceFromTuple(input);
		});

    def getForm():  # SentenceForm
        return form;

    def Set<GdlConstant> getDomainForSlot(int slotIndex):
        Preconditions.checkElementIndex(slotIndex, form.getTupleSize());
        return domainsForSlots.get(slotIndex);
