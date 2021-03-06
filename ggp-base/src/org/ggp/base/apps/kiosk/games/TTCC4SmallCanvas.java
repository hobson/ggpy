package org.ggp.base.apps.kiosk.games

import java.awt.Color
import java.awt.Graphics
import java.util.Set

import org.ggp.base.apps.kiosk.templates.CommonGraphics
import org.ggp.base.apps.kiosk.templates.GameCanvas_FancyGrid


class TTCC4SmallCanvas(GameCanvas_FancyGrid):
    serialVersionUID = 1L  # int 

    def String getGameName()  return "TTCC4 (Small)"
    protected String getGameKey()  return "ttcc4_2player_small"
    protected int getGridHeight()  return 5
    protected int getGridWidth()  return 5

    protected final bool useGridVisualization()  return false
    protected final bool coordinatesStartAtOne()  return true

    protected final void renderCellBackground(Graphics g, int xCell, int yCell):
        int width = g.getClipBounds().width
        int height = g.getClipBounds().height

        yCell = 6 - yCell

        CommonGraphics.drawCellBorder(g)

        // Clear out the edges
        if(xCell == 1 || xCell == 5 || yCell == 1 || yCell == 5):
            g.setColor(Color.DARK_GRAY)
            g.fillRect(0, 0, width, height)


    protected Set<String> getLegalMovesForCell(int xCell, int yCell):
        yCell = 6 - yCell

        Set<String> theMoves = gameStateHasLegalMovesMatching("\\( pawnMove " + xCell + " " + yCell + " (.*) \\)")
        theMoves.addAll(gameStateHasLegalMovesMatching("\\( knightMove " + xCell + " " + yCell + " (.*) \\)"))
        theMoves.addAll(gameStateHasLegalMovesMatching("\\( checkerMove " + xCell + " " + yCell + " (.*) \\)"))
        theMoves.addAll(gameStateHasLegalMovesMatching("\\( jump " + xCell + " " + yCell + " (.*) \\)"))

        if(theMoves.size() == 0)
            theMoves.addAll(gameStateHasLegalMovesMatching("\\( drop " + xCell + " \\)"))

        if(theMoves.size() == 0)
            theMoves.add("noop")

        return theMoves

    protected Set<String> getFactsAboutCell(int xCell, int yCell):
        yCell = 6 - yCell
        return gameStateHasFactsMatching("\\( cell " + xCell + " " + yCell + " (.*) \\)")

    protected void renderCellContent(Graphics g, Set<String> theFacts):
        if(theFacts.size() == 0) return
        String theFact = theFacts.iterator().next()

        String[] cellFacts = theFact.split(" ")
        String cellType = cellFacts[4]
        if(!cellType.equals("b")):
            Color myColor = null
            if(cellType.startsWith("red")) myColor = Color.red
            if(cellType.startsWith("blue")) myColor = Color.blue
            if(myColor == null):
                System.err.println("Got weird piece: " + cellType)
                return

            int width = g.getClipBounds().width
            int height = g.getClipBounds().height

            g.setColor(myColor)
            g.fillOval(2, 2, width-4, height-4)

            if(cellType.contains("Pawn")):
                CommonGraphics.drawChessPiece(g, "bp")
            elif(cellType.contains("Knight")):
                CommonGraphics.drawChessPiece(g, "bn")
            elif(cellType.contains("Checker")):
                CommonGraphics.drawCheckersPiece(g, "bk")
            elif(cellType.contains("Disc")):
                



    protected void renderMoveSelectionForCell(Graphics g, int xCell, int yCell, String theMove):
        int width = g.getClipBounds().width
        int height = g.getClipBounds().height

        yCell = 6 - yCell

        String[] moveParts = theMove.split(" ")

        if(moveParts.length == 4):
            int xDrop = Integer.parseInt(moveParts[2])
            if(xCell == xDrop):
                g.setColor(Color.GREEN)
                g.drawRect(3, 3, width-6, height-6)
                g.drawRect(4, 4, width-8, height-8)

        elif(moveParts.length == 7):
            int xTarget = Integer.parseInt(moveParts[4])
            int yTarget = Integer.parseInt(moveParts[5])
            if(xTarget == xCell && yCell == yTarget):
                g.setColor(Color.GREEN)
                g.drawRect(3, 3, width-6, height-6)
                g.drawRect(4, 4, width-8, height-8)
                CommonGraphics.fillWithString(g, "X", 3)

        elif(moveParts.length == 9):
            int xTarget = Integer.parseInt(moveParts[6])
            int yTarget = Integer.parseInt(moveParts[7])
            if(xTarget == xCell && yCell == yTarget):
                g.setColor(Color.GREEN)
                g.drawRect(3, 3, width-6, height-6)
                g.drawRect(4, 4, width-8, height-8)
                CommonGraphics.fillWithString(g, "X", 3)



