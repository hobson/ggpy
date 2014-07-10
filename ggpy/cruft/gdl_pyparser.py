import pyparsing as pp

# capital letter followed by any number of alphanum or underscore chars
function_constant = pp.Word(pp.srange("[A-Za-z]"), pp.srange("[a-zA-Z0-9_]"))
identifier = pp.Word(pp.srange("[A-Za-z]"), pp.srange("[a-zA-Z0-9_]"))
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

variable = pp.Word('?', pp.alphas)


# GDL-II Relation Constants
sees = pp.Keyword('sees')  # The predicate sees(?r,?p) means that role ?r perceives ?p in the next game state.
random = pp.Keyword('random')  # A predefined player that choses legal moves randomly

# GDL-I Relation Constants
relation_constant = role | inpt | base | init | next | does | legal | goal | terminal | distinct | true

# Numerical contant
# FIXME: too permissive -- accepts 10 numbers, "00", "01", ... "09"
number = (pp.Keyword('100') | pp.Word(pp.nums, min=1, max=2))

# the only operator/relationship constant
implies = pp.Keyword('<=')

token = (implies | variable | relation_constant | number | pp.Word(pp.alphas + pp.nums))

# Define the simple recursive grammar
grammar = pp.Forward()
nested_parentheses = pp.nestedExpr('(', ')', content=grammar) 
grammar << (implies | variable | relation_constant | number | pp.Word(pp.alphas + pp.nums) | nested_parentheses)