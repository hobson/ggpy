# logic_pyparsing.py
from __future__ import print_function
from pyparsing import infixNotation, opAssoc, Keyword, Word, alphas

symbols = {
    'p': None,
    'q': None,
    'r': None,
    }

class Operand(object):
    def __init__(self, token):
        self.label = token[0]
        self.value = eval(symbols.get(token[0], None))
    def __bool__(self):
        return self.value
    def __str__(self):
        return self.label
    __repr__ = __str__
    __nonzero__ = __bool__


class BinaryOperator(object):

    def __init__(self,t):
        self.args = t[0][0::2]
    def __str__(self):
        sep = " %s " % self.ascii_symbol
        return "(" + sep.join(map(str,self.args)) + ")"
    def __bool__(self):
        return self.evaluate(bool(a) for a in self.args)
    __repr__ = __str__
    __nonzero__ = __bool__


class And(BinaryOperator):
    ascii_symbol = '&'
    evaluate = all


class Or(BinaryOperator):
    ascii_symbol = '|'
    evaluate = any


class Not(object):
    def __init__(self,t):
        self.arg = t[0][1]
    def __bool__(self):
        v = bool(self.arg)
        return not v
    def __str__(self):
        return "~" + str(self.arg)
    __repr__ = __str__
    __nonzero__ = __bool__


T = Keyword("True") | Keyword("true") | Keyword("T") | Keyword("1")
F = Keyword("False") | Keyword("false")| Keyword("F")| Keyword("0")

operand = T | F | Word(alphas, max=1)
operand.setParseAction(Operand)

# define expression, based on expression operand and
# list of operations in precedence order
expression = infixNotation( operand,
    [
    ("not", 1, opAssoc.RIGHT, Not),
    ("and", 2, opAssoc.LEFT,  And),
    ("or",  2, opAssoc.LEFT,  Or),
    ])


def test():
    symbols['p'] = True
    symbols['q'] = False
    symbols['r'] = True
    tests = [("p", True),
             ("q", False),
             ("p and q", False),
             ("p and not q", True),
             ("not not p", True),
             ("not(p and q)", True),
             ("q or not p and r", False),
             ("q or not p or not r", False),
             ("q or not (p and r)", False),
             ("p or q or r", True),
             ("p or q or r and False", True),
             ("(p or q or r) and False", False),
            ]

    print("p =", symbols.get('p'))
    print("q =", symbols.get('q'))
    print("r =", symbols.get('r'))
    print()
    passes, failures = 0, 0
    for test_string, expected_result in tests:
        print(test_string)
        ans = expression.parseString(test_string)[0]
        success = "PASS" if bool(ans) == expected_result else "FAIL"
        if success == "PASS":
            passes += 1
        else:
            failures += 1
        print(test_string,'\n', expected_result, '=', bool(ans),'\n', success, '\n')
    print('tests passed: ' + passes)
    print('tests failed: ' + failures)
    return passes, failures
