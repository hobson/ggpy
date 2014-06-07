#!/usr/bin/env python
""" generated source for module InfoRequest """
# package: org.ggp.base.player.request.grammar
import org.ggp.base.player.gamer.Gamer

import org.ggp.base.util.presence.InfoResponse

class InfoRequest(Request):
    """ generated source for class InfoRequest """
    gamer = Gamer()

    def __init__(self, gamer):
        """ generated source for method __init__ """
        super(InfoRequest, self).__init__()
        self.gamer = gamer

    def getMatchId(self):
        """ generated source for method getMatchId """
        return None

    def process(self, receptionTime):
        """ generated source for method process """
        info = InfoResponse()
        info.setName(self.gamer.__name__)
        info.setStatus("available" if self.gamer.getMatch() == None else "busy")
        info.setSpecies(self.gamer.getSpecies())
        return info.toSymbol().__str__()

    def __str__(self):
        """ generated source for method toString """
        return "info"

