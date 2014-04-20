package org.ggp.base.apps.kiosk.games

import java.awt.Color
import java.awt.Graphics
import java.util.Set

import org.ggp.base.apps.kiosk.templates.CommonGraphics
import org.ggp.base.apps.kiosk.templates.GameCanvas_FancyGrid


// NOTE: I still don't fully understand how this game actually works. -Sam
class ChickenTicTacToeCanvas(GameCanvas_FancyGrid):
    serialVersionUID = 0x1  # int 

    def String getGameName()  return "Tic-Tac-Toe (Chicken)"
    protected String getGameKey()  return "chickentictactoe"
    protected int getGridHeight()  return 3
    protected int getGridWidth()  return 3

    protected Set<String> getFactsAboutCell(int xCell, int yCell):
        return gameStateHasFactsMatching("\\( cell " + xCell + " " + yCell + " (.*) \\)")

    protected Set<String> getLegalMovesForCell(int xCell, int yCell):
        return gameStateHasLegalMovesMatching("\\( mark " + xCell + " " + yCell + " \\)")

    protected void renderCellContent(Graphics g, String theFact):
        String[] cellFacts = theFact.split(" ")

        if(!cellFacts[4].equals("b")):
            g.setColor(Color.BLACK)
            CommonGraphics.fillWithString(g, cellFacts[4], 1.2)


