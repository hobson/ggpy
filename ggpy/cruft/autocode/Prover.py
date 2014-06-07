#!/usr/bin/env python
""" generated source for module Prover """
# package: org.ggp.base.util.prover
import java.util.Set

import org.ggp.base.util.gdl.grammar.GdlSentence

class Prover(object):
    """ generated source for interface Prover """
    __metaclass__ = ABCMeta
    @abstractmethod
    def askAll(self, query, context):
        """ generated source for method askAll """

    @abstractmethod
    def askOne(self, query, context):
        """ generated source for method askOne """

    @abstractmethod
    def prove(self, query, context):
        """ generated source for method prove """

