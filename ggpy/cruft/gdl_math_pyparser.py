# Adapted from fourFn.py by Paul McGuire and Andrea Griffini at 
# http://pyparsing.wikispaces.com/file/detail/fourFn.py 
#
# Support + - / * ^ math operations.
#
# Copyright 2003-2006 by Paul McGuire
#
import pyparsing as pp
import math
import operator

class Stack(object):
    _stack = None

    def __init__(self):
        _stack = []

    def pushFirst( strg, loc, toks ):
        exprStack.append( toks[0] )

    def pushUMinus( strg, loc, toks ):
        if toks and toks[0]=='-': 
            exprStack.append( 'unary -' )
            #~ exprStack.append( '-1' )
            #~ exprStack.append( '*' )

def expression_grammar()
    # GDL keywords ("Relation Constants")
    role = pp.Keyword('role')  # role(a) means that a is a player name/side in the game.
    inpt = pp.Keyword('input') # input(t) means that t is a base proposition in the game.
    base = pp.Keyword('base')  # base(a) means that a is an action in the game.
    init = pp.Keyword('init')  # init(p) means that the datum p is true in the initial state.
    next = pp.Keyword('next')  # next(p) means that the datum p is true in the next state.
    does = pp.Keyword('does')  # does(r,a) means that player r performs action a in the current state.
    legal = pp.Keyword('legal')  # legal(r,a) means it is legal for r to play a in the current state.
    goal = pp.Keyword('goal')  # goal(r,n) means that player the current state has utility n for player r. n must be an integer from 0 through 100.
    terminal = pp.Keyword('terminal')  # terminal means that the current state is a terminal state.
    distinct = pp.Keyword('distinct')  # distinct(x,y) means that the values of x and y are different.
    true = pp.Keyword('true')  # true(p) means that the datum p is true in the current state.

    # GDL-II Relation Constants
    sees = pp.Keyword('sees')  # The predicate sees(?r,?p) means that role ?r perceives ?p in the next game state.
    random = pp.Keyword('random')  # A predefined player that choses legal moves randomly

    # GDL-I Relation Constants
    relation_constant = role | inpt | base | init | next | does | legal | goal | terminal | distinct | true

    # Numerical contant
    # FIXME: too permissive -- accepts 10 numbers, "00", "01", ... "09"
    number = pp.Keyword('100') | pp.Word(pp.nums, min=1, max=2)

    # the only operator/relationship constant
    implies = pp.Keyword('<=')

    point = pp.Literal( "." )
    relation = pp.Word(pp.alphas, pp.alphas+pp.nums+"_$")
 
    add  = pp.Literal( "+" )
    subtract = pp.Literal( "-" )
    multiply  = pp.Literal( "*" )
    divide   = pp.Literal( "/" )
    left_paren  = pp.Literal( "(" ).suppress()
    right_paren  = pp.Literal( ")" ).suppress()
    addition  = add | subtract
    multiplication = multiply | divide
    exponentiation = pp.Literal( "^" )
    
    expression = pp.Forward()
    atom = (pp.Optional("-") + ( number | (relation | relation_constant) + left_paren + expression + right_paren ).setParseAction( pushFirst ) | ( left_paren + expression.suppress() + right_paren )).setParseAction(pushUMinus) 
    
    # "atom [ ^ exponent ]..." gives right-to-left order precedence
    # "atom [ ^ atom ]...", gives left-to-right precendence
    # right-to-left: 2^3^2 = 2^(3^2)
    # left-to-right:       = (2^3)^2
    exponent = pp.Forward()
    exponent << atom + pp.ZeroOrMore( ( exponentiation + exponent ).setParseAction( pushFirst ) )
    
    term = exponent + pp.ZeroOrMore( ( multiplication + exponent ).setParseAction( pushFirst ) )
    expression << term + pp.ZeroOrMore( ( addition + term ).setParseAction( pushFirst ) )
    return expression


# map operator symbols to corresponding arithmetic operations
epsilon = 1e-12

operation = { 
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
    }

fun = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "abs": abs,
    "trunc": lambda a: int(a),
    "round": round,
    "sgn": lambda a: abs(a) > epsilon and cmp(a, 0) or 0,
    }

def evaluate_expression(atom_list):
    operator = atom_list.pop()
    if operator == 'unary -':
        return -evaluate_expression( atom_list )
    if operator in "+-*/^":
        op2 = evaluate_expression( atom_list )
        op1 = evaluate_expression( atom_list )
        return operation[operator]( op1, op2 )
    elif operator in fun:
        return fun[operator]( evaluate_expression( atom_list ) )
    elif operator[0].isalpha():
        return 0
    else:
        return float( operator )

def test( s, expression_value ):
    stack = Stack()
    results = expression_grammar().parseString( s )
    value = evaluate_expression( stack._stack[:] )
    if val == expression_value:
        print s + " = ", value, results, "=>",  stack._stack
    else:
        print s + " ERROR: ", value, "!=", expression_value, results, "=>", stack._stack

if __name__ == "__main__":

    # nested parentheses seem to work too
    test( "1 / (2 * (5 + 1))", 1. / (2 * (5 + 1) ) )
    test( "1 / ((5 + 1) / 2)", 1. / ((5 + 1.) / 2) )

    # but not if you forget to close the outer parentheses!
    test( "1 / ((5 + 1) / 2",  1. / ((5 + 1.) / 2) )

    test( "9", 9 )
    test( "-9", -9 )
    test( "--9", 9 )
    test( "9 + 3 + 6", 9 + 3 + 6 )
    test( "9 + 3 / 11", 9 + 3. / 11 )
    test( "(9 + 3)", (9 + 3) )
    test( "(9+3) / 11", (9 + 3.) / 11 )
    test( "9 - 12 - 6", 9 - 12 - 6 )
    test( "2*3.14159", 2 * 3.14159 )
    test( "3.1415926535*3.1415926535 / 10", 3.1415926535*3.1415926535 / 10 )
    test( "e / 3", math.e / 3 )
    test( "2^3^2", 2**3**2 )
    test( "2^3+2", 2**3+2 )
    test( "2^9", 2**9 )
    test( "sgn(-2)", -1 )
    test( "sgn(0)", 0 )
    test( "sgn(0.1)", 1 )


"""
Test output:
>pythonw -u fourFn.py
9 = 9.0 ['9'] => ['9']
9 + 3 + 6 = 18.0 ['9', '+', '3', '+', '6'] => ['9', '3', '+', '6', '+']
9 + 3 / 11 = 9.27272727273 ['9', '+', '3', '/', '11'] => ['9', '3', '11', '/', '+']
(9 + 3) = 12.0 [] => ['9', '3', '+']
(9+3) / 11 = 1.09090909091 ['/', '11'] => ['9', '3', '+', '11', '/']
9 - 12 - 6 = -9.0 ['9', '-', '12', '-', '6'] => ['9', '12', '-', '6', '-']
9 - (12 - 6) = 3.0 ['9', '-'] => ['9', '12', '6', '-', '-']
2*3.14159 = 6.28318 ['2', '*', '3.14159'] => ['2', '3.14159', '*']
3.1415926535*3.1415926535 / 10 = 0.986960440053 ['3.1415926535', '*', '3.1415926535', '/', '10'] => ['3.1415926535', '3.1415926535', '*', '10', '/']
PI * PI / 10 = 0.986960440109 ['PI', '*', 'PI', '/', '10'] => ['PI', 'PI', '*', '10', '/']
PI*PI/10 = 0.986960440109 ['PI', '*', 'PI', '/', '10'] => ['PI', 'PI', '*', '10', '/']
PI^2 = 9.86960440109 ['PI', '^', '2'] => ['PI', '2', '^']
6.02E23 * 8.048 = 4.844896e+024 ['6.02E23', '*', '8.048'] => ['6.02E23', '8.048', '*']
e / 3 = 0.90609394282 ['E', '/', '3'] => ['E', '3', '/']
sin(PI/2) = 1.0 ['sin', 'PI', '/', '2'] => ['PI', '2', '/', 'sin']
trunc(E) = 2 ['trunc', 'E'] => ['E', 'trunc']
E^PI = 23.1406926328 ['E', '^', 'PI'] => ['E', 'PI', '^']
2^3^2 = 512.0 ['2', '^', '3', '^', '2'] => ['2', '3', '2', '^', '^']
2^3+2 = 10.0 ['2', '^', '3', '+', '2'] => ['2', '3', '^', '2', '+']
2^9 = 512.0 ['2', '^', '9'] => ['2', '9', '^']
sgn(-2) = -1 ['sgn', '-2'] => ['-2', 'sgn']
sgn(0) = 0 ['sgn', '0'] => ['0', 'sgn']
sgn(0.1) = 1 ['sgn', '0.1'] => ['0.1', 'sgn']
>Exit code: 0
"""