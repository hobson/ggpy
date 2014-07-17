#!/usr/bin/python
"""ggpy.gdl.propnet
 
Hobson Lane <hobson@totalgood.com>
(c) 2014 Hobson Lane
Open-source under MIT-license: [LICENSE.txt](github.com/hobson/ggpy/LICENSE.txt)
"""

import networkx as nx
# import pyparsing as pp
import operator

import parser 
import os

from pyparsing import ParseResults

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


def denest(list_or_obj):
    """Simplify excess nesting parenthesese if necessary, e.g. "((base b))"->"(base b)"

    Only denests the first branch in the nested tree

    >>> denest([[['base', 'b']]])
    ['base', 'b']
    >>> denest(['base', 'b'])
    ['base', 'b']
    >>> denest([['input', [['white', 'place', 1]]]])
    ['input', [['white', 'place', 1]]]
    """
    while is_parse_result(list_or_obj) and len(list_or_obj) == 1 and is_parse_result(list_or_obj[0]):
        return denest(list_or_obj[0])
    return list_or_obj


def nest(list_or_obj):
    """Add outermost parenthesese if none present, e.g. "base b"->"(base b)"

    >>> nest('base')
    ['base']
    """
    if (hasattr(list_or_obj, 'append') and hasattr(list_or_obj, '__iter__')) or isinstance(list_or_obj, (list, ParseResults)):
        return list_or_obj
    return [list_or_obj]


def nest_args(list_or_obj):
    """Add parenthesese aroung function arguments, e.g. "(base b)"->"(base(b))"

    >>> nest_args(['base', 'b'])
    ['base', ['b']]
    >>> nest_args(['input', 'white', 1])
    ['input', ['white', 1]]
    >>> nest_args(['input', [['white', 1]]])
    ['input', ['white', 1]]
    """
    # 
    if len(list_or_obj) > 1:
        list_or_obj[1] = denest(list_or_obj[1:])
        if len(list_or_obj[1:]) > 1:
            del(list_or_obj[2:])
    return list_or_obj


def normalize_ands(list_or_obj):
    """
    >>> normalize_ands(['<=', 'p', 'does', ['white', 'a'], '&', 'true', ['s']])
    ['<=', ['p'] ['does', ['white', 'a']], ['true', ['s']]'
    """

# keyword_meta =  { 
#                 'role': {'nargs': 1},
#                 'base': {'nargs': 1},
#                 'input': {'nargs': 2},
#                 'legal': {'nargs': 2},
#                 }


class LogicNetwork(nx.MultiDiGraph):

    def __init__(self, *args, **kwargs):
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
        print 'parse_action(s, loc, toks=%s)' % toks
        toks = denest(toks)
        print 'parse_action(s, loc, toks=%s)' % toks
        print len(toks)
        toks = nest_args(toks)
        name, type = None, toks[0]
        if type in ['role', 'base']:
            # print toks, toks[0][0], ' '.join(toks[0][1])
            name = '-'.join(toks[1])
            # print 'adding node named %s ...' % name
        elif type in ['legal', 'input']:
            # print toks, toks[0][0], ' '.join(toks[0][1])
            name = 'does(' + ','.join(toks[1]) + ')'
            # print 'adding node named %s ...' % name
        elif type == '<=':
            pass
        print name
        if name:
            self.add_node(type=type, name=name, mark=None, source=None)
        # print 'added node, now have %s' % self.nodes()


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

