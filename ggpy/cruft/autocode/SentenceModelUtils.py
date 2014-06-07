#!/usr/bin/env python
""" generated source for module SentenceModelUtils """
# package: org.ggp.base.util.gdl.model
import java.util.Set

import org.ggp.base.util.gdl.grammar.GdlSentence

class SentenceModelUtils(object):
    """ generated source for class SentenceModelUtils """
    @classmethod
    def inSentenceFormGroup(cls, sentence, forms):
        """ generated source for method inSentenceFormGroup """
        for form in forms:
            if form.matches(sentence):
                return True
        return False

