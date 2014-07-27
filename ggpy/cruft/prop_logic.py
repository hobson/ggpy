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
    def __init__(self,t):
        self.keyword = Keyword(self.symbol)
        for lit in self.literals:
            self.keyword |= Keyword(lit)
        self.args = t[0][0:]
    def evaluate(self, a):
        if a == 'and':
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
    ("not" , 1, opAssoc.RIGHT, Not),
    ("and", 2, opAssoc.LEFT, And),
    ("or",  2, opAssoc.LEFT, Or),
    ("",    2, opAssoc.LEFT, And),
#     ("implies",  3, opAssoc.RIGHT, Implies),  # ValueError: if numterms=3, opExpr must be a tuple or list of two expressions
    ])
test = ["p and not q",
        "not not p",
        "not(p and q)",
        "q or not p and r",
        "q or not p or not r",
        "q or not (p and r)",
        "p or q or r",
        "p or q or r and False",
        "(p or q or r) and False",
        "p q", # ignores the implied AND and only reports value of p
        "(p q)", # ignores the implied AND and only reports value of p
        "(p) (q)", # ignores the implied AND and only reports value of p
        "(q or (p and q))",  # implied AND doesn't work, expects closing parenthesis
        "p r", # ignores the implied AND and only reports value of p
        "(p r)", # ignores the implied AND and only reports value of p
        "(p) (r)", # ignores the implied AND and only reports value of p
        "(q or (p and r))",  # implied AND doesn't work, expects closing parenthesis
        ]

p = True
q = False
r = True
print "p =", p
print "q =", q
print "r =", r
print
for t in test:
    res = expression.parseString(t)[0]
    print t,'\n', res, '=', bool(res),'\n'