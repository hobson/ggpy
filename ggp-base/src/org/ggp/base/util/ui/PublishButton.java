package org.ggp.base.util.ui

import java.awt.event.ActionEvent
import java.awt.event.ActionListener

import javax.swing.JButton
import javax.swing.JOptionPane

import org.ggp.base.server.GameServer


class PublishButton(JButton implements ActionListener):
    theServer = GameServer()

    def PublishButton(String theName):
        super(theName)
        self.addActionListener(this)
        self.setEnabled(false)

    def void setServer(GameServer theServer):
        self.theServer = theServer
        self.setEnabled(true)

    def void actionPerformed(ActionEvent e):
        if (e.getSource() == this):
            if (theServer != null):
                if (!theServer.getMatch().getGame().getRepositoryURL().contains("127.0.0.1")):
                    String theMatchKey = theServer.startPublishingToSpectatorServer("http://matches.ggp.org/")
                    if (theMatchKey != null):
                        String theURL = "http://www.ggp.org/view/all/matches/" + theMatchKey + "/"
                        System.out.println("Publishing to: " + theURL)
                        int nChoice = JOptionPane.showConfirmDialog(this,
                                "Publishing successfully. Would you like to open the spectator view in a browser?",
                                "Publishing Match Online",
                                JOptionPane.YES_NO_OPTION)
                        if (nChoice == JOptionPane.YES_OPTION):
                            try 
                                java.awt.Desktop.getDesktop().browse(java.net.URI.create(theURL))
                            except Exception ee):
                                ee.printStackTrace()


                    else:
                        JOptionPane.showMessageDialog(this,
                                "Unknown problem when publishing match.",
                                "Publishing Match Online",
                                JOptionPane.ERROR_MESSAGE)

                else:
                    JOptionPane.showMessageDialog(this,
                        "Could not publish a game that is only stored locally.",
                        "Publishing Match Online",
                        JOptionPane.ERROR_MESSAGE)

                setEnabled(false)



