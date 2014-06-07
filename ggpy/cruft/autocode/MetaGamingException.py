#!/usr/bin/env python
""" generated source for module MetaGamingException """
# package: org.ggp.base.player.gamer.exception
@SuppressWarnings("serial")
class MetaGamingException(Exception):
    """ generated source for class MetaGamingException """
    def __init__(self, cause):
        """ generated source for method __init__ """
        super(MetaGamingException, self).__init__(cause)

    def __str__(self):
        """ generated source for method toString """
        return "An unhandled exception occurred during metagaming: " + super(MetaGamingException, self).__str__()

