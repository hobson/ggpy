#!/usr/bin/python
"""ggpy.gdl.propnet
 
Hobson Lane <hobson@totalgood.com>
(c) 2014 Hobson Lane
Open-source under MIT-license: [LICENSE.txt](github.com/hobson/ggpy/LICENSE.txt)
"""

import os
import networkx as nx
import operator
# import pyparsing as pp

from pyparsing import ParseResults

from gdl import parser


class Node(object):
    def __init__(self, label=''):
        self.value = None
        if isinstance(label, basestring):
            self.label = label
        else:
            self.label = label[0]
    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self.label)
    __str__ = __repr__

class Connective(Node):
    def __init__(self, label):
        super(Connective, self).__init__(label)
        self.ary = 1
        self.operator = bool

class AndGate(Connective):
    def __init__(self, label=''):
        super(AndGate, self).__init__(label)
        self.ary = 2
        self.operator = operator.and_

class OrGate(Connective):
    def __init__(self, label=''):
        super(OrGate, self).__init__(label)
        self.ary = 2
        self.operator = operator.or_

class Inverter(Connective):
    def __init__(self, label=''):
        super(Inverter, self).__init__(label)
        self.operator = operator.not_

class Transition(Connective):
    """Point in a network cycle that represents a transition from one state (turn) to the next, a delay of one time-step or 1/z."""
    def __init__(self, label=''):
        super(Transition, self).__init__(label)
        self.operator = lambda x: None

class Proposition(Node):
    def __init__(self, label=''):
        super(Proposition, self).__init__(label)
        self.value = None

class Input(Node):
    """Proposition Node with only outgoing arcs (edges), no incoming arcs"""
    def __init__(self, label=''):
        super(Input, self).__init__(label)

class Base(Node):
    """Proposition Node with an incoming arcs only from a Transition Nodes"""
    def __init__(self, label=''):
        super(Base, self).__init__(label)

class Terminal(Node):
    """Terminal Node for a GGP game that halts the transitions (game steps/plays) when it becomes true"""
    def __init__(self, label=''):
        super(Terminal, self).__init__(label)
    def operator(self):
        if self.value:
            raise StopIteration


class Goal(Node):
    """A non-boolean valued node which indicates the rewuard for a player as an integer from 0 to 100"""
    def __init__(self, label=''):
        super(Terminal, self).__init__(label)


def is_parse_result(list_or_obj):
    return (hasattr(list_or_obj, 'append') and hasattr(list_or_obj, '__iter__')) or isinstance(list_or_obj, (list, ParseResults))


def denest(list_or_obj, verbosity=0):
    """Simplify excess nesting parenthesese if necessary, e.g. "((base b))"->"(base b)"

    Only denests the first branch in the nested tree

    >>> denest([[['base', 'b']]])
    ['base', 'b']
    >>> denest([['base', ['b']]])
    ['base', ['b']]
    >>> denest([[['base'], ['b']]])
    ['base', ['b']]
    >>> denest(['base', 'b'])
    ['base', 'b']
    >>> denest([['input', [['white', 'place', 1]]]])
    ['input', ['white', 'place', 1]]
    """
    if verbosity:
        print "denest(%r)" % list_or_obj
    # unwrap any nested 1-length lists 
    while is_parse_result(list_or_obj) and len(list_or_obj) == 1 and is_parse_result(list_or_obj[0]):
        return denest(list_or_obj[0])
    if verbosity:
        print "%r is not nested 1-length" % list_or_obj
    # unwrap any keywords
    if is_parse_result(list_or_obj):
        if len(list_or_obj) == 1 and not is_parse_result(list_or_obj[0]) and list_or_obj[0] in parser.RELATION_CONSTANTS:
            if verbosity:
                print "denesting 1-length list of keywords: %r" % list_or_obj
            return list_or_obj[0]
        else:
            return [denest(loo) for loo in list_or_obj]
    if verbosity:
        print "denested or non-keyword: %r" % list_or_obj
    return list_or_obj


def nest(list_or_obj, verbosity=0):
    """Add outermost parenthesese if none present, e.g. "base b"->"(base b)"

    >>> nest('base')
    'base'
    >>> nest([['base'], ['b']])
    ['base', ['b']]
    >>> nest('identifier')
    ['identifier']
    >>> nest(['<=', 'p', 'does', ['white', 'a'], '&', 'true', ['s']])
    ['<=', ['p'], 'does', [['white'], ['a']], '&', 'true', ['s']]
    """
    if verbosity:
        print "nest(%r)" % list_or_obj
    if is_parse_result(list_or_obj):
        if verbosity:
            print 'nest(loo) for loo in %r' % list_or_obj
        return denest([nest(loo) for loo in list_or_obj])
    # leave keyword identifiers unwrapped (no brackets)
    elif list_or_obj in parser.RELATION_CONSTANTS:
        if verbosity:
            print 'keyword left alone: %r' % list_or_obj
        return list_or_obj
    # wrap non-keyword identifiers and numbers with brackets
    if verbosity:
        print 'wrapping nonkeywords with brackets: denest([%r])' % list_or_obj
    return denest([list_or_obj])


def nest_args(list_or_obj, verbosity=0):
    """Add parenthesese aroung function arguments, e.g. "(base b)"->"(base(b))"

    >>> nest_args(['base', 'b'])
    ['base', ['b']]
    >>> nest_args(['s'])
    ['s']
    >>> nest_args('s')
    ['s']
    >>> nest_args(['input', 'white', 1])
    ['input', [['white'], [1]]]
    >>> nest_args(['input', [['white', 1]]])
    ['input', [['white'], [1]]]
    >>> nest_args(['<=', 'p', 'does', ['white', 'a'], '&', 'true', ['s']])  
    ['<=', [['p'], 'does', [['white'], ['a']], '&', 'true', ['s']]]
    """
    if verbosity:
        print "nest_args(%r)" % list_or_obj
    list_or_obj = nest(list_or_obj)
    if verbosity:
        print 'after nesting identifiers: %r' % list_or_obj
    # this is same as `nest(list_or_obj)` but leaves function names bare
    if isinstance(list_or_obj, basestring):
        return list_or_obj
    # for a list of strings, arenthesize the strings (arguments) after the first string (funciton name)
    elif len(list_or_obj) > 1 and isinstance(list_or_obj[0], basestring): #list_or_obj[0] in parser.RELATION_CONSTANTS:
        # make sure the args are wrapped in a single pair of brackets (the function names are NOT bracketed)  
        nargs = parser.RELATION_CONSTANTS.get(list_or_obj[0], 1)
        # ensure that there's only one pair of brackets around the args and it's the next item in the list
        list_or_obj[1] = denest(list_or_obj[1:nargs+1])
        # clean up the expressions that were processed already
        if len(list_or_obj[1:]) > 1:
            if verbosity:
                print 'deleting these expressions: %r' % list_or_obj[2:nargs+1]
            del(list_or_obj[2:nargs+1])
        if verbosity:
            print 'nesting the elements of this list: %r' % list_or_obj[1:]
        return [list_or_obj[0]] + [denest([nest_args(loo) for loo in list_or_obj[1:]])]
    if verbosity:
        print 'bracketing the expression %r' % list_or_obj
    return denest([list_or_obj])



def normalize_ands(list_or_obj):
    """Remove implied and operators

    >>> normalize_ands(['<=', 'p', 'does', ['white', 'a'], '&', 'true', ['s']])
    ['<=', [['p'], 'does', [['white'], ['a']], 'true', ['s']]]
    """
    if isinstance(list_or_obj, basestring):
        if list_or_obj.lower() in ['and', '&', '&&']:
            return None
        else:
            return list_or_obj
    else:
        toks = [normalize_ands(tok) for tok in nest_args(list_or_obj)]
        return [tok for tok in toks if tok]




class LogicNetwork(nx.DiGraph):
    """A networkx graph representation of a set of Propositional Logic facts/sentences

    Called a "propnet" in General Game Playing at coursera.

    To allow multiple edges to share the same source and destination
    change the LogicNetwork parent to nx.MultiDiGraph
    """

    def __init__(self, *args, **kwargs):
        self.sentences = []
        self.base_nodes = []
        self.redundant_edges = True  # whether to allow redundant edges (same source and destination) to be created
        self.verbosity = kwargs.get('verbosity', 1)
        return super(LogicNetwork, self).__init__(self, *args, **kwargs)

    def add_node(self, type=None, name=None, mark=None, source=None):
        print 'add_node'
        if name is None:
            name = self.number_of_nodes()
        if type is None:
            type = 'buffer'  # MIL-STD/ANSI/IEC term for "pass-through"/not-not/No-Op 
        attr = { 'type': type, 'name': name, 'mark': mark, 'source': source }
        print attr
        super(LogicNetwork, self).add_node(name, attr=attr)

    def get_nodes_by_attribute(self, **kwargs):
        return [n for n in self.nodes_iter() 
                if all(self.node[n]['attr'].get(k, None) == v for k, v in kwargs.iteritems())]

    def get_nodes_by_type(self, type):
        return [n for n in self.nodes_iter() 
                if self.node[n]['attr'].get('type', None) == type]

    def get_base_nodes(self):
        if self.verbosity:
            print 'looking for base nodes'
        self.base_nodes = [n for n in self.nodes_iter()
                if self.node[n]['attr'].get('type', None) == 'base']
        if self.verbosity:
            print 'found %d base nodes' % len(self.base_nodes)
        return self.base_nodes
        

    def parse_action(self, *args):
        '''Action to perform (add_node) when a new GDL token (word) is successfully parsed.
           A parse action must accept 0-3 arguments, and is called by pyparsing with
           C{fn(s,loc,toks)}, C{fn(loc,toks)}, C{fn(toks)}, or just C{fn()}, where:
            - s    = the original string parsed
            - loc  = the location of the matching substring within the origial string
            - toks = a list of the matched tokens, packaged as a C{L{ParseResults}} object
        '''
        if not args:
            return
        if len(args) == 3:
            s, loc, toks = args
        elif len(args) == 2:
            loc, toks = args
        elif len(args) == 1:
            toks = args
        if self.verbosity:
            print 'parse_action(s, loc, toks=%s)' % toks
        toks = denest(toks)
        if self.verbosity:
            print 'denest(toks): %r' % toks
        toks = nest_args(toks)    
        if self.verbosity:
            print 'nest_args(toks): %r' % toks
        toks = nest_args(toks)
        type = toks[0]
        name = None
        # if len(toks) > 1:
        #     if is_parse_result(toks[1]):
        #         if any(is_parse_result(toks[1][i]) for i in len(toks[1])):
        #             if not any(is_parse_result(toks[1][0][i]) for i in range(len(toks[1][0]))):
        #                 name = '-'.join('-'.join(tok) for tok in toks[1][0])
        #         else:
        #             name = '-'.join(toks[1])
        #     else:
        #         name = toks[1]
        if type == 'role':
            name = None  # no need to add a node for each new value of the role variable
        elif type == 'base':
            # print toks, toks[0][0], ' '.join(toks[0][1])
            name = '-'.join(toks[1])
            # print 'adding node named %s ...' % name
        elif type in ['legal', 'input']:
            # print toks, toks[0][0], ' '.join(toks[0][1])
            name = 'does(' + ','.join(tok[0] for tok in toks[1]) + ')'
            # print 'adding node named %s ...' % name
        elif type == '<=':
            if self.verbosity:
                print 'proposition (<=): %r' % toks
            if is_parse_result(toks[1][0]) or toks[1][0] not in parser.RELATION_CONSTANTS:
                self.add_node(type=type, name=toks[1][0][0], mark=None, source=None)
                # FIXME: add edges to/from transition
            if toks[1][0] == 'next':
                # next keyword defines a transition node and the arcs into it and from the transition to a base node
                for b in self.get_base_nodes():
                    if self.verbosity > 1:
                        print 'adding edge to base node found: %r' % b
                    edge = toks[1][1][1][0], toks[1][1][0][0]
                    # don't add redundant edges
                    if self.redundant_edges or edge not in self.edges():
                        self.add_edge(*edge)
                    # print toks, toks[0][0], ' '.join(toks[0][1])
                name = '-'.join(toks[2])
                # print 'adding node named %s ...' % name
                pass
        if name:
            if self.verbosity:
                print 'adding unconnected node for name: %r' % name
            self.add_node(type=type, name=name, mark=None, source=None)
        # print 'added node, now have %s' % self.nodes()
        self.sentences += [toks]


class View(Node):
    """Proposition Node with incoming arcs only from Base or Input Nodes, no arcs from Transition nodes"""
    def __init__(self, label=''):
        super(View, self).__init__(label)

def propnet_from_parsed_gdl(parsed_gdl):
    propnet = LogicNetwork()
    #parser.sentence.setParseAction(propnet.parse_action)
    for i, fact_tokens in enumerate(parsed_gdl):
        if (fact_tokens[0] in ['base', 'role', 'input']):
            name = ' '.join(fact_tokens[1])
            propnet.add_node(name=name, type=fact_tokens[0])
    return propnet

def noop(toks):
    print toks
    return toks

def propnet_from_gdl(gdl='chapter10', verbosity=None):
    propnet = LogicNetwork()
    parser.sentence.setParseAction(propnet.parse_action)
    parser.game_description.setParseAction(noop)
    for path in [gdl, os.path.join(os.path.dirname(__file__), '..', 'example_game_gdl', gdl + '.gdl')]:
        try:
            with open(path) as fpin:
                gdl = fpin.read()
            break
        except:
            pass
    parser.game_description.parseString(gdl)
    print propnet.nodes()
    return propnet

def propnet_from_example(game_name='chapter10'):
    from gdl import parser
    net = LogicNetwork()
    parser.sentence.setParseAction(net.parse_action)
    parser.game_description.parseFile(os.path.join('example_game_gdl', game_name + '.gdl'))
    return net

def test():
    net = nx.MultiDiGraph()
    # Example propnet from http://logic.stanford.edu/ggp/chapters/chapter_09.html
    s = Base('s')
    a = Input('a')
    b = Input('b')
    p, q, r = (View('p'), View('q'), View('r'))
    asp, pq, rs, qbr = (AndGate('asp'), Inverter('pq'), Transition('rs'), OrGate('qbr'))
    # propnet.add_node(s)
    # propnet.add_nodes_from((a, b))
    # propnet.add_nodes_from((p, q, r))
    # propnet.add_nodes_from((asp, pq, rs))

    net.add_edges_from([
                            (a, asp), (s, asp),
                            (asp, p),
                            (p, pq),
                            (pq, q),
                            (q, qbr),
                            (b, qbr), (qbr, r),
                            (r, rs),
                            (rs, s),
                           ])
    from matplotlib import pyplot as plt
    nx.draw(net, with_labels=True)
    plt.show()
    parser.base.parseAction(Base())
    # game description from http://logic.stanford.edu/ggp/chapters/chapter_09.html

    gdl_path = os.path.join(os.path.dirname(__file__), '..', 'example_game_gdl', 'chapter10.gdl')
    example = parser.game_description.parseFile(gdl_path)

    propnet_computed =  network_from_parsed_gdl(example)
    nx.draw(net, with_labels=True)
    plt.show()
    return net

