#!/usr/bin/env python
""" generated source for module RequestFormatException """
# package: org.ggp.base.player.request.factory.exceptions
@SuppressWarnings("serial")
class RequestFormatException(Exception):
    """ generated source for class RequestFormatException """
    source = str()
    bad = Exception()

    def __init__(self, source, bad):
        """ generated source for method __init__ """
        super(RequestFormatException, self).__init__()
        self.source = source
        self.bad = bad

    def getSource(self):
        """ generated source for method getSource """
        return self.source

    def __str__(self):
        """ generated source for method toString """
        return "Improperly formatted request: " + self.source + ", resulting in exception: " + self.bad

