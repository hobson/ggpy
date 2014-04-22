#!/usr/bin/env python
""" generated source for module GdlValidator """
# package: org.ggp.base.util.gdl
import org.ggp.base.util.symbol.grammar.Symbol

import org.ggp.base.util.symbol.grammar.SymbolAtom

import org.ggp.base.util.symbol.grammar.SymbolList

# 
#  * The GdlValidator class implements Gdl validation for the GdlFactory class.
#  * Its purpose is to validate whether or not a Symbol can be transformed into a
#  * Gdl expression without error.
#  
class GdlValidator(object):
    """ generated source for class GdlValidator """
    # 
    # 	 * Validates whether a Symbol can be transformed into a Gdl expression
    # 	 * without error using the following process:
    # 	 * <ol>
    # 	 * <li>Returns true if the Symbol is a SymbolAtom. Otherwise, treats the
    # 	 * Symbol as a SymbolList.</li>
    # 	 * <li>Checks that the SymbolList contains no sub-elements that are
    # 	 * SymbolLists which do not begin with a SymbolAtom.</li>
    # 	 * <li>Checks that neither the SymbolList nor its sub-elements contain the
    # 	 * deprecated 'or' keyword.</li>
    # 	 * </ol>
    # 	 * Note that as implemented, this method is incomplete: it only verifies a
    # 	 * subset of the correctness properties of well-formed Gdl. A more thorough
    # 	 * implementation is advisable.
    # 	 *
    # 	 * @param symbol
    # 	 *            The Symbol to validate.
    # 	 * @return True if the Symbol passes validation; false otherwise.
    # 	 
    def validate(self, symbol):
        """ generated source for method validate """
        if isinstance(symbol, (SymbolAtom, )):
            return True
        elif containsAnonymousList(symbol):
            return False
        elif containsOr(symbol):
            return False
        else:
            return True

    # 
    # 	 * A recursive method that checks whether a Symbol contains SymbolList that
    # 	 * does not begin with a SymbolAtom.
    # 	 *
    # 	 * @param symbol
    # 	 *            The Symbol to validate.
    # 	 * @return True if the Symbol passes validation; false otherwise.
    # 	 
    def containsAnonymousList(self, symbol):
        """ generated source for method containsAnonymousList """
        if isinstance(symbol, (SymbolAtom, )):
            return False
        else:
            if isinstance(symbol, (SymbolList, )):
                return True
            else:
                while i < (symbol).size():
                    if self.containsAnonymousList((symbol).get(i)):
                        return True
                    i += 1
                return False

    # 
    # 	 * A recursive method that checks whether a Symbol contains the deprecated
    # 	 * 'or' keyword.
    # 	 *
    # 	 * @param symbol
    # 	 *            The Symbol to validate.
    # 	 * @return True if the Symbol passes validation; false otherwise.
    # 	 
    def containsOr(self, symbol):
        """ generated source for method containsOr """
        if isinstance(symbol, (SymbolAtom, )):
            return False
        else:
            if symbol.__str__().lower() == "or":
                return True
            elif isinstance(symbol, (SymbolList, )):
                while i < (symbol).size():
                    if self.containsOr((symbol).get(i)):
                        return True
                    i += 1
        return False

