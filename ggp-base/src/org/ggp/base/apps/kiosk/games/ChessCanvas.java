package org.ggp.base.apps.kiosk.games

import java.awt.Color
import java.awt.Graphics
import java.util.Set

import org.ggp.base.apps.kiosk.templates.CommonGraphics
import org.ggp.base.apps.kiosk.templates.GameCanvas_Chessboard


class ChessCanvas(GameCanvas_Chessboard):
    serialVersionUID = 1L  # int 

    def String getGameName()  return "Chess"
    protected String getGameKey()  return "chess"

    protected Set<String> getLegalMovesForCell(int xCell, int yCell):
        String xLetter = coordinateToLetter(xCell)
        return gameStateHasLegalMovesMatching("\\( move .. " + xLetter + " " + yCell + " (.*) \\)")

    protected Set<String> getFactsAboutCell(int xCell, int yCell):
        String xLetter = coordinateToLetter(xCell)
        return gameStateHasFactsMatching("\\( cell " + xLetter + " " + yCell + " (.*) \\)")

    protected void renderCellContent(Graphics g, String theFact):
        String[] cellFacts = theFact.split(" ")
        String cellType = cellFacts[4]
        if(!cellType.equals("b")):
            CommonGraphics.drawChessPiece(g, cellType)


    protected void renderMoveSelectionForCell(Graphics g, int xCell, int yCell, String theMove):
        int width = g.getClipBounds().width
        int height = g.getClipBounds().height

        String xLetter = coordinateToLetter(xCell)

        String[] moveParts = theMove.split(" ")
        String xTarget = moveParts[5]
        int yTarget = Integer.parseInt(moveParts[6])
        if(xLetter.equals(xTarget) && yCell == yTarget):
            g.setColor(new Color(0, 0, 255, 192))
            g.drawRect(3, 3, width-6, height-6)
            CommonGraphics.fillWithString(g, "X", 3)


