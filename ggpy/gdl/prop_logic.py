#
# proplogic.py
#
# Based on SimpleBool by Paul McGuire (pyparsing)
# 
# Parses GDL propositional logic (boolean expressions of fact or implication)
# Assumes expression in prefix (polish) notation, where the 
# operator comes first and all operands follow

from pyparsing import *
import pyparsing as pp
import sys

class Atom(object):
    # default atom (even empty string) is treated as an AND operation
    symbol = '&'
    literals = ('and', 'AND', ' ', 'And', '&&')

    @classmethod
    def get_parser(cls):
        cls.parser = pp.Keyword(cls.symbol)
        for lit in cls.literals:
            cls.parser |= pp.Keyword(lit)
        return cls.parser

    def __init__(self, t):
        self.args = t[0][0:]

    def evaluate(self, a):
        if a in self.literals:
            return True
        if isinstance(a, basestring):
            return eval(a)
        else:
            return bool(a)

    def __str__(self):
        sep = " %s " % self.symbol
        return "(" + sep.join(map(str, [a for a in self.args if a not in self.literals])) + ")"


class And(Atom):

    def __nonzero__(self):
        for a in self.args:
            if not self.evaluate(a):
                return False
        return True


class Or(Atom):
    symbol = '|'
    literals = ('or', 'OR', 'Or', '||')

    def __nonzero__(self):
        for a in self.args[0::2]:
            if self.evaluate(a):
                return True
        return False


class Not(Atom):
    symbol = '~'
    literals = ('not', 'Not', 'NOT', '!')

    def __str__(self):
        """Override the Atom stringifier because it assumes binary operators and Not is unary"""
        return self.symbol + str(self.args[1])

    def __nonzero__(self):
        return not self.evaluate(self.arg)


class Implies(Atom):
    symbol = '='
    implied_operator = Atom.symbol
    literals = ('<=', '-:', '<-', 'implies', 'Implies', 'IMPLIES')

    def __init__(self):
        super(Implies, self).__init__()
        self.variable = self.args[0]

    def __str__(self):
        """
        Implies (assignment?) is not really an operator so not sure if it should be derived from Atom
        Implies is variable arity in GDL, with an implied And between arguments.
        """
        return self.variable + self.symbol + str(self.implied_operator.join(self.args[1:]))

    def __nonzero__(self):
        return all(self.evaluate(a) for a in self.args)


def create_variable(token_tree):
    """Create a global variable within this module to hold a new identifier (variable)
       whenever a new one is mentioned in a propositional logic universe (set of expressions/facts).

    FIXME: seems highly unsafe to allow a logic expression to alter the global namespace,
           even though existing variables, names, objects, functions are protected. 
    """
    this_module = sys.modules[__name__]
    variable_name = token_tree[0]
    if hasattr(this_module, variable_name):
        return
    return setattr(sys.modules[__name__], variable_name, create_variable.default_value)
    # globals()[token_tree[0]] = default_value
create_variable.default_value = None


atom = oneOf("True False") | pp.Word(pp.alphas, pp.alphas + '_' + '0123456789').setParseAction(create_variable)
expression = pp.operatorPrecedence(atom,
    [
    (Not.get_parser(), 1, opAssoc.RIGHT, Not),
    (And.get_parser(), 2, opAssoc.LEFT, And),
    (Or.get_parser(),  2, opAssoc.LEFT, Or),
    ("", 2, opAssoc.LEFT, And),
#     ("implies",  3, opAssoc.RIGHT, Implies),  # ValueError: if numterms=3, opExpr must be a tuple or list of two expressions
    ])


from gdl.parser import comment


fact = expression + (comment | pp.lineEnd.suppress() | pp.stringEnd.suppress())
fact_or_comment = comment | fact
fact_set = pp.OneOrMore(fact_or_comment)


def test():
    import time
    # FIXME: define assignment operator for non-global assignment of value to variables in subsequent expressions
    global p, q, r, this, that, theother, theother2
    p, q, r = True, False, True
    # don't declare "that" and let it take on the value None which will evaluate to False
    this, theother, theother2 = p, r, r
    tests = [
                ("p and not q  ; True and not False => True", True),
                ("not not p ; double-negative: not not True => True", True),
                ("not(p and q)", True),
                ("q or not p and r", False),
                ("q or (not p and r)", False),  # FIXME: doesn't check the not precedence priority properly
                ("not (p and r) or q", False),  # FIXME: this takes unusually long to process (1.5 seconds!)
                ("(q or (not (p and r)))", False),
                ("(q or not p) or not r", False),
                ("q or not (p and r)", False),
                ("p or q or r", True),
                ("p or q or r and False", True),
                ("(p or q or r) and False", False),
                ("p q", False),
                ("(p q)", False),
                ("(p) (q)", False),
                ("(q or (p and q))", False),
                ("p r", True),
                ("(p r)", True),
                ("(p) (r)", True),
                ("(q or (p and r))", True),
                ("; comments are strings instead of bools",  " comments are strings instead of bools"),
                ("(this or (that and theother2))", True),
                ("__new_hidden_variable | theother2   ; raise an exception so that system hidden globals that begin are protected", pp.ParseException("Expected W:(;)")),
                ("(<= (x) (True))", getattr(sys.modules[__name__], 'x')),
            ]


    print "p, q, r = %r, %r, %r" % (p, q, r)
    print
    passed, failed = 0, 0
    for s, expected in tests:
        t0 = time.time()
        try:
            result = fact_or_comment.parseString(s)[0]
        except Exception as e:
            result = e
        # the "mark" for an expression or node (propnet terminology) is 
        # either the boolean evaluation of the expression, or the contents of the comment (a string)
        # TODO: allow numerical value (int/float) expressions/formulas instead of just boolean binary logic?
        mark = (result if isinstance(result, (basestring, Exception, float, int)) else bool(result))
        dt = time.time() - t0
        print '      test string: %s' % s 
        print 'python expression: %r == %r     (%3f ms)' % (str(result), mark, dt * 1000)
        if str(mark) == str(expected) and type(mark) == type(expected):
            passed += 1
            print 'Passed'
            print
        else:
            failed += 1
            print 'TEST FAILED! Expected: %r' % expected
            print '        Expected type: %s' % type(expected) 
            print '                  Got: %r' % mark
            print '             Got type: %s' % type(mark)
            print
    print "Passed %d out of %d, Failed %d" % (passed, passed + failed, failed)
    return failed


if __name__ == '__main__':
    test()