#!/usr/bin/env python
""" generated source for module AbortingException """
# package: org.ggp.base.player.gamer.exception
@SuppressWarnings("serial")
class AbortingException(Exception):
    """ generated source for class AbortingException """
    def __init__(self, cause):
        """ generated source for method __init__ """
        super(AbortingException, self).__init__(cause)

    def __str__(self):
        """ generated source for method toString """
        return "An unhandled exception ocurred during aborting: " + super(AbortingException, self).__str__()

