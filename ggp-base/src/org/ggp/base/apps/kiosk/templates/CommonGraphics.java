package org.ggp.base.apps.kiosk.templates

import java.awt.Color
import java.awt.Font
import java.awt.FontMetrics
import java.awt.Graphics
import java.awt.Image
import java.io.File
import java.io.IOException
import java.util.Random

import javax.imageio.ImageIO

import org.ggp.base.util.configuration.ProjectConfiguration


class CommonGraphics(object):
    def Image getImage(String imageName):
        return getImage("", imageName)

    def Image getImage(String dirName, String imageName):
        try 
            return ImageIO.read(new File(new File(ProjectConfiguration.gameImagesDirectory, dirName), imageName))
        except IOException e):
            e.printStackTrace()
            return null


    def void fillWithString(Graphics g, String theText, float sizeFactor):
        int theHeight = g.getClipBounds().height
        int theWidth = g.getClipBounds().width

        Font theFont = g.getFont().deriveFont((float) (theHeight / sizeFactor)).deriveFont(Font.BOLD)
        g.setFont(theFont)

        FontMetrics theMetric = g.getFontMetrics()
        g.drawString(theText, (theWidth - theMetric.stringWidth(theText)) / 2, theMetric.getAscent() + (theHeight - (theMetric.getDescent() + theMetric.getAscent())) / 2)

    def void drawSelectionBox(Graphics g):
        int width = g.getClipBounds().width
        int height = g.getClipBounds().height

        g.setColor(Color.GREEN)
        g.drawRect(3, 3, width-6, height-6)

    def void drawCellBorder(Graphics g):
        int width = g.getClipBounds().width
        int height = g.getClipBounds().height

        g.setColor(Color.BLACK)
        g.drawRect(1, 1, width-2, height-2)

    def void drawBubbles(Graphics g, int nCode):
        int width = g.getClipBounds().width
        int height = g.getClipBounds().height

        g.setColor(Color.BLUE)
        g.fillRect(1, 1, width-2, height-2)

        Random r = new Random(nCode)
        int nBubbles = r.nextInt(3)+2
        for(int i = 0; i < nBubbles; i++):
            int xB = (int)(r.nextDouble() * width)
            int yB = (int)(r.nextDouble() * height)
            int rB = (int)(r.nextDouble() * Math.min(width, height)/5.0)
            g.setColor(Color.CYAN)
            g.drawOval(xB-rB, yB-rB, rB*2, rB*2)


    def void drawDisc(Graphics g):
        int width = g.getClipBounds().width
        int height = g.getClipBounds().height

        Color theColor = g.getColor()
        g.setColor(Color.DARK_GRAY)
        g.fillOval(4, 4, width-8, height-8)
        g.setColor(theColor)
        g.fillOval(6, 6, width-12, height-12)

    def void drawCheckersPiece(Graphics g, String checkersPiece):
        int width = g.getClipBounds().width
        int height = g.getClipBounds().height

        if(checkersPiece.length() != 2)
            return

        Color theColor = ((checkersPiece.charAt(0) == 'b') ? Color.BLACK : Color.RED)
        bool isKing = (checkersPiece.charAt(1) == 'k')

        g.setColor(Color.DARK_GRAY)
        g.fillOval(4, 4, width-8, height-8)
        g.setColor(theColor)
        g.fillOval(6, 6, width-12, height-12)
        if(isKing):
            if(theCrownImage == null)
                theCrownImage = getImage("checkers", "crown.png")

            g.setColor(Color.YELLOW)
            g.drawImage(theCrownImage, width/5, 2*height/7, 3*width/5, 3*height/7, null)


    def void drawChessPiece(Graphics g, String chessPiece):
        int width = g.getClipBounds().width
        int height = g.getClipBounds().height

        if (blackPawnImage == null)
            lazyLoadChessPieces()

        Image toDraw = null
        if(chessPiece.charAt(0) == 'w'):
            if(chessPiece.equals("wp")) toDraw = whitePawnImage
            else if(chessPiece.equals("wn")) toDraw = whiteKnightImage
            else if(chessPiece.equals("wb")) toDraw = whiteBishopImage
            else if(chessPiece.equals("wq")) toDraw = whiteQueenImage
            else if(chessPiece.equals("wr")) toDraw = whiteRookImage
            else if(chessPiece.equals("wk")) toDraw = whiteKingImage
        elif(chessPiece.charAt(0) == 'b'):
            if(chessPiece.equals("bp")) toDraw = blackPawnImage
            else if(chessPiece.equals("bn")) toDraw = blackKnightImage
            else if(chessPiece.equals("bb")) toDraw = blackBishopImage
            else if(chessPiece.equals("bq")) toDraw = blackQueenImage
            else if(chessPiece.equals("br")) toDraw = blackRookImage
            else if(chessPiece.equals("bk")) toDraw = blackKingImage

        if(toDraw != null):
            g.drawImage(toDraw, 5, 5, width-10, height-10, null)
        else:
            System.err.println("Could not process chess piece [" + chessPiece + "].")


    def void lazyLoadChessPieces():
        blackPawnImage   = getImage("chess", "Black_Pawn.png")
        blackRookImage   = getImage("chess", "Black_Rook.png")
        blackBishopImage = getImage("chess", "Black_Bishop.png")
        blackKnightImage = getImage("chess", "Black_Knight.png")
        blackKingImage   = getImage("chess", "Black_King.png")
        blackQueenImage  = getImage("chess", "Black_Queen.png")
        whitePawnImage   = getImage("chess", "White_Pawn.png")
        whiteRookImage   = getImage("chess", "White_Rook.png")
        whiteBishopImage = getImage("chess", "White_Bishop.png")
        whiteKnightImage = getImage("chess", "White_Knight.png")
        whiteKingImage   = getImage("chess", "White_King.png")
        whiteQueenImage  = getImage("chess", "White_Queen.png")

    // Checkers images
    def Image theCrownImage

    // Chess images
    def Image blackPawnImage
    def Image blackRookImage
    def Image blackBishopImage
    def Image blackKnightImage
    def Image blackKingImage
    def Image blackQueenImage
    def Image whitePawnImage
    def Image whiteRookImage
    def Image whiteBishopImage
    def Image whiteKnightImage
    def Image whiteKingImage
    def Image whiteQueenImage
