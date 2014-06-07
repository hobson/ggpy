#!/usr/bin/env python
""" generated source for module MoveSelectionException """
# package: org.ggp.base.player.gamer.exception
@SuppressWarnings("serial")
class MoveSelectionException(Exception):
    """ generated source for class MoveSelectionException """
    def __init__(self, cause):
        """ generated source for method __init__ """
        super(MoveSelectionException, self).__init__(cause)

    def __str__(self):
        """ generated source for method toString """
        return "An unhandled exception ocurred during move selection: " + super(MoveSelectionException, self).__str__()

