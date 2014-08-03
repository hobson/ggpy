#
# proplogic.py
#
# Based on SimpleBool by Paul McGuire (pyparsing)
# 
# Parses GDL propositional logic (boolean expressions of fact or implication)
# Assumes expression in prefix (polish) notation, where the 
# operator comes first and all operands follow

from pyparsing import *

class Atom(object):
    # default atom (even empty string) is treated as an AND operation
    symbol = '&'
    literals = ('and', 'AND', ' ', 'And', '&&')

    @classmethod
    def get_parser(cls):
        cls.parser = Keyword(cls.symbol)
        for lit in cls.literals:
            cls.parser |= Keyword(lit)
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
    def __init__(self, t):
        self.arg = t[0][1]
    # override the Atom stringifier because it assumes binary operators and Not is a unary operator
    def __str__(self):
        return self.symbol + str(self.arg)
    def __nonzero__(self):
        return not self.evaluate(self.arg)


class Implies(Atom):
    symbol = '<='
    literals = ('-:', 'implies', 'Implies', 'IMPLIES')
    # override the Atom stringifier because it assumes binary operators and Implies is a unary (infinite arity?) operator
    def __str__(self):
        return self.symbol + str(self.arg)
    def __nonzero__(self):
        return all(self.evaluate(a) for a in self.args)


atom = Word(alphas, max=1) | oneOf("True False")
expression = operatorPrecedence(atom,
    [
    (Not.get_parser(), 1, opAssoc.RIGHT, Not),
    (And.get_parser(), 2, opAssoc.LEFT, And),
    (Or.get_parser(),  2, opAssoc.LEFT, Or),
    ("", 2, opAssoc.LEFT, And),
#     ("implies",  3, opAssoc.RIGHT, Implies),  # ValueError: if numterms=3, opExpr must be a tuple or list of two expressions
    ])


def test():
    import time
    # FIXME: define assignment operator for non-global assignment of value to variables in subsequent expressions
    global p, q, r
    p, q, r = True, False, True
    tests = [
                ("p and not q", True),
                ("not not p", True),
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
            ]


    print "p, q, r = %r, %r, %r" % (p, q, r)
    print
    passed, failed = 0, 0
    for s, expected in tests:
        t0 = time.time()
        result = expression.parseString(s)[0]
        dt = time.time() - t0
        print '      test string: %s' % s 
        print 'python expression: %s == %r     (%3f ms)' % (result, bool(result), dt * 1000)
        if bool(result) == expected:
            passed += 1
            print 'Passed'
            print
        else:
            failed += 1
            print 'TEST FAILED! Expected: %r' % expected
            print
    print "Passed %d out of %d, Failed %d" % (passed, passed + failed, failed)
    return failed


if __name__ == '__main__':
    test()