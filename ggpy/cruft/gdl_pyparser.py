import pyparsing as pp


# capital letter followed by any number of alphanum or underscore chars
function_constant = pp.Word(pp.srange("[A-Z]", pp.srange("[a-zA-Z0-9_]")))
comment = pp.Word(';') + pp.restOfLine('comment')

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

# Nested parentheses
enclosed = pp.Forward()
nested_parens = pp.nestedExpr('(', ')', content=enclosed).leaveWhitespace()
enclosed << (pp.Word(word | true | nested_parens)

# role_sentence = role + nested_parens

#term = pp.Combine(word) | parens
enclosed << pp.Optional(implies) + pp.OneOrMore(nested_parens)



# # alternative grouped expression evaluation that includes exponentiation from fourFn.py example on pyparser page
# expression = pp.Forward()
# atom = (pp.Optional("-") + ( number | (relation | relation_constant) + left_paren + expression + right_paren ).setParseAction( pushFirst ) | ( left_paren + expression.suppress() + right_paren )).setParseAction(pushUMinus) 
# exponent = pp.Forward()
# exponent << atom + pp.ZeroOrMore( ( exponentiation + exponent ).setParseAction( pushFirst ) )
# term = exponent + pp.ZeroOrMore( ( multiplication + exponent ).setParseAction( pushFirst ) )
# expression << term + pp.ZeroOrMore( ( addition + term ).setParseAction( pushFirst ) )




sentence = (role | init | next | does | terms | word) + nested_parens
gdl_game = pp.OneOrMore(sentence)


# nestedParens = pp.nestedExpr('(', ')') 

# relationship = pp.Word(pp.alphas).setResultsName('relationship')

# number = pp.Word(pp.nums + '.')
# variable = pp.Word(pp.alphas)
# # an argument to a relationship can be either a number or a variable
# argument = number | variable

# # arguments are a delimited list of 'argument' surrounded by parenthesis
# arguments= (pp.Suppress('(') + pp.delimitedList(argument) +
#             pp.Suppress(')')).setResultsName('arguments')

# # a fact is composed of a relationship and it's arguments 
# # (I'm aware it's actually more complicated than this
# # it's just a simplifying assumption)
# fact = (relationship + arguments).setResultsName('facts', listAllMatches=True)

# # a sentence is a fact plus a period
# sentence = fact + pp.Suppress('.')

# # self explanatory
# prolog_sentences = pp.OneOrMore(sentence)