#!/usr/bin/env python
""" generated source for module RequestFactory """
# package: org.ggp.base.player.request.factory
import java.util.ArrayList

import java.util.List

import org.ggp.base.player.gamer.Gamer

import org.ggp.base.player.request.factory.exceptions.RequestFormatException

import org.ggp.base.player.request.grammar.AbortRequest

import org.ggp.base.player.request.grammar.InfoRequest

import org.ggp.base.player.request.grammar.PlayRequest

import org.ggp.base.player.request.grammar.PreviewRequest

import org.ggp.base.player.request.grammar.Request

import org.ggp.base.player.request.grammar.StartRequest

import org.ggp.base.player.request.grammar.StopRequest

import org.ggp.base.util.game.Game

import org.ggp.base.util.gdl.factory.GdlFactory

import org.ggp.base.util.gdl.factory.exceptions.GdlFormatException

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.symbol.factory.SymbolFactory

import org.ggp.base.util.symbol.grammar.Symbol

import org.ggp.base.util.symbol.grammar.SymbolAtom

import org.ggp.base.util.symbol.grammar.SymbolList

class RequestFactory(object):
    """ generated source for class RequestFactory """
    def create(self, gamer, source):
        """ generated source for method create """
        try:
            if type_ == "play":
                return createPlay(gamer, list_)
            elif type_ == "start":
                return createStart(gamer, list_)
            elif type_ == "stop":
                return createStop(gamer, list_)
            elif type_ == "abort":
                return createAbort(gamer, list_)
            elif type_ == "info":
                return createInfo(gamer, list_)
            elif type_ == "preview":
                return createPreview(gamer, list_)
            else:
                raise IllegalArgumentException("Unrecognized request type!")
        except Exception as e:
            raise RequestFormatException(source, e)

    def createPlay(self, gamer, list_):
        """ generated source for method createPlay """
        if len(list_) != 3:
            raise IllegalArgumentException("Expected exactly 2 arguments!")
        arg1 = list_.get(1)
        arg2 = list_.get(2)
        matchId = arg1.getValue()
        moves = parseMoves(arg2)
        return PlayRequest(gamer, matchId, moves)

    def createStart(self, gamer, list_):
        """ generated source for method createStart """
        if len(list_) < 6:
            raise IllegalArgumentException("Expected at least 5 arguments!")
        arg1 = list_.get(1)
        arg2 = list_.get(2)
        arg3 = list_.get(3)
        arg4 = list_.get(4)
        arg5 = list_.get(5)
        matchId = arg1.getValue()
        roleName = GdlFactory.createTerm(arg2)
        theRulesheet = arg3.__str__()
        startClock = Integer.valueOf(arg4.getValue())
        playClock = Integer.valueOf(arg5.getValue())
        #  For now, there are only five standard arguments. If there are any
        #  new standard arguments added to START, they should be added here.
        theReceivedGame = Game.createEphemeralGame(theRulesheet)
        return StartRequest(gamer, matchId, roleName, theReceivedGame, startClock, playClock)

    def createStop(self, gamer, list_):
        """ generated source for method createStop """
        if len(list_) != 3:
            raise IllegalArgumentException("Expected exactly 2 arguments!")
        arg1 = list_.get(1)
        arg2 = list_.get(2)
        matchId = arg1.getValue()
        moves = parseMoves(arg2)
        return StopRequest(gamer, matchId, moves)

    def createAbort(self, gamer, list_):
        """ generated source for method createAbort """
        if len(list_) != 2:
            raise IllegalArgumentException("Expected exactly 1 argument!")
        arg1 = list_.get(1)
        matchId = arg1.getValue()
        return AbortRequest(gamer, matchId)

    def createInfo(self, gamer, list_):
        """ generated source for method createInfo """
        if len(list_) != 1:
            raise IllegalArgumentException("Expected no arguments!")
        return InfoRequest(gamer)

    def createPreview(self, gamer, list_):
        """ generated source for method createPreview """
        if len(list_) != 3:
            raise IllegalArgumentException("Expected exactly 2 arguments!")
        arg1 = list_.get(1)
        arg2 = list_.get(2)
        theRulesheet = arg1.__str__()
        previewClock = Integer.valueOf(arg2.getValue())
        theReceivedGame = Game.createEphemeralGame(theRulesheet)
        return PreviewRequest(gamer, theReceivedGame, previewClock)

    def parseMoves(self, symbol):
        """ generated source for method parseMoves """
        if isinstance(symbol, (SymbolAtom, )):
            return None
        else:
            while i < len(list_):
                moves.add(GdlFactory.createTerm(list_.get(i)))
                i += 1
            return moves

