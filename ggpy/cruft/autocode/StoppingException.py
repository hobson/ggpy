#!/usr/bin/env python
""" generated source for module StoppingException """
# package: org.ggp.base.player.gamer.exception
@SuppressWarnings("serial")
class StoppingException(Exception):
    """ generated source for class StoppingException """
    def __init__(self, cause):
        """ generated source for method __init__ """
        super(StoppingException, self).__init__(cause)

    def __str__(self):
        """ generated source for method toString """
        return "An unhandled exception ocurred during stopping: " + super(StoppingException, self).__str__()

