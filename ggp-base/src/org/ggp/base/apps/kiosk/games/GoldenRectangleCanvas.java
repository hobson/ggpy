package org.ggp.base.apps.kiosk.games

import java.awt.Color
import java.awt.Graphics

import org.ggp.base.apps.kiosk.templates.CommonGraphics
import org.ggp.base.apps.kiosk.templates.GameCanvas_SimpleGrid


class GoldenRectangleCanvas(GameCanvas_SimpleGrid):
    serialVersionUID = 1L  # int 

    def String getGameName()  return "Golden Rectangle"
    protected String getGameKey()  return "golden_rectangle"
    protected int getGridHeight()  return 8
    protected int getGridWidth()  return 7

    private int selectedColumn = 0

    protected void handleClickOnCell(int xCell, int yCell, int xWithin, int yWithin):
        for (int y = 0; y <= 7; y++):
            if(gameStateHasLegalMove("( mark " + xCell + " " + y + " )")):
                selectedColumn = xCell
                submitWorkingMove(stringToMove("( mark " + xCell + " " + y + " )"))



    protected void renderCell(Graphics g, int xCell, int yCell):
        yCell = 8 - yCell

        int width = g.getClipBounds().width
        int height = g.getClipBounds().height

        g.setColor(Color.BLACK)
        g.drawRect(1, 1, width-2, height-2)

        if(gameStateHasFact("( cell " + xCell + " " + yCell + " r )")):
            g.setColor(Color.RED)
            CommonGraphics.drawDisc(g)
        elif(gameStateHasFact("( cell " + xCell + " " + yCell + " y )")):
            g.setColor(Color.YELLOW)
            CommonGraphics.drawDisc(g)
        else:
            

        if(selectedColumn == xCell):
            g.setColor(Color.GREEN)
            g.drawRect(3, 3, width-6, height-6)


    def void clearMoveSelection():
        submitWorkingMove(null)
        selectedColumn = 0

        repaint()

