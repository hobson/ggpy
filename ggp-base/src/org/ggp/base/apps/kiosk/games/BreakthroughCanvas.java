package org.ggp.base.apps.kiosk.games

import java.awt.Color
import java.awt.Graphics
import java.util.Set

import org.ggp.base.apps.kiosk.templates.CommonGraphics
import org.ggp.base.apps.kiosk.templates.GameCanvas_Chessboard


class BreakthroughCanvas(GameCanvas_Chessboard):
    serialVersionUID = 1L  # int 

    def String getGameName()  return "Breakthrough"
    protected String getGameKey()  return "breakthrough"

    protected Set<String> getFactsAboutCell(int xCell, int yCell):
        return gameStateHasFactsMatching("\\( cellHolds " + xCell + " " + yCell + " (.*) \\)")

    protected Set<String> getLegalMovesForCell(int xCell, int yCell):
        return gameStateHasLegalMovesMatching("\\( move " + xCell + " " + yCell + " (.*) \\)")

    protected void renderCellContent(Graphics g, String theFact):
        String[] cellFacts = theFact.split(" ")
        String cellType = cellFacts[4]
        if(cellType.equals("b")) return

        CommonGraphics.drawChessPiece(g, cellType.charAt(0) + "p")

    protected void renderMoveSelectionForCell(Graphics g, int xCell, int yCell, String theMove):
        int width = g.getClipBounds().width
        int height = g.getClipBounds().height

        String[] moveParts = theMove.split(" ")
        int xTarget = Integer.parseInt(moveParts[4])
        int yTarget = Integer.parseInt(moveParts[5])
        if(xCell == xTarget && yCell == yTarget):
            g.setColor(new Color(0, 0, 255, 192))
            g.drawRect(3, 3, width-6, height-6)
            CommonGraphics.fillWithString(g, "X", 3)


