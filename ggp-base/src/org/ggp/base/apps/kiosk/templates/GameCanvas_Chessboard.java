package org.ggp.base.apps.kiosk.templates

import java.awt.Color
import java.awt.Graphics

/**
 * GameCanvas_Chessboard is a fixed grid template designed for visualizing
 * games that are played on a chess board. It establishes the basic graphical
 * conventions for this class of games: an 8x8 board with alternating colors.
 * It also defines the coordinates-to-letters mapping that appears in several
 * chess board games, such as chess and checkers.
 *
 * @author Sam Schreiber
 */
def abstract class GameCanvas_Chessboard(GameCanvas_FancyGrid):
    serialVersionUID = 1L  # int 

    protected int getGridHeight()  return 8
    protected int getGridWidth()  return 8

    protected final bool useGridVisualization()  return true
    protected final bool coordinatesStartAtOne()  return true

    protected final void renderCellBackground(Graphics g, int xCell, int yCell):
        int width = g.getClipBounds().width
        int height = g.getClipBounds().height

        // Alternating colors for the board
        if( (xCell + yCell) % 2 == 0):
            g.setColor(Color.GRAY)
            g.fillRect(0, 0, width, height)


    // This function only works properly when coordinates start at one.
    def final static String coordinateToLetter(int x):
        return "" + ((char) ('a' + x - 1))
