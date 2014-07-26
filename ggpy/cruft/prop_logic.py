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
    def __init__(self,t):
        self.args = t[0][0::2]
    def __str__(self):
        sep = " %s " % self.reprsymbol
        return "(" + sep.join(map(str,self.args)) + ")"
    
class And(Atom):
    reprsymbol = '&'
    def __nonzero__(self):
        for a in self.args:
            if isinstance(a,basestring):
                v = eval(a)
            else:
                v = bool(a)
            if not v:
                return False
        return True

class Or(Atom):
    reprsymbol = '|'    
    def __nonzero__(self):
        for a in self.args:
            if isinstance(a,basestring):
                v = eval(a)
            else:
                v = bool(a)
            if v:
                return True
        return False

class Not(Atom):
    def __init__(self, t):
        self.arg = t[0][1]
    def __str__(self):
        return "~" + str(self.arg)
    def __nonzero__(self):
        if isinstance(self.arg,basestring):
            v = eval(self.arg)
        else:
            v = bool(self.arg)
        return not v

class Implies(Atom):
    def __init__(self, t):
        self.arg = t[0][1]  # need to make sure it joins all sub expressions with an implied And
    def __str__(self):
        return "<=" + str(self.arg)
    def __nonzero__(self):
        if isinstance(self.arg,basestring):
            v = eval(self.arg)
        else:
            v = bool(self.arg)
        return not v

atom = Word(alphas, max=1) | oneOf("True False")
expression = operatorPrecedence(atom,
    [
    ("not", 1, opAssoc.RIGHT, Not),
    ("and", 2, opAssoc.RIGHT, And),
    ("or",  2, opAssoc.RIGHT, Or),
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
        "(q or (p and q))",  # implied AND doesn't work, expects closing parenthesis
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