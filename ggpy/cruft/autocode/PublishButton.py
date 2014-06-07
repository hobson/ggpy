#!/usr/bin/env python
""" generated source for module PublishButton """
# package: org.ggp.base.util.ui
import java.awt.event.ActionEvent

import java.awt.event.ActionListener

import javax.swing.JButton

import javax.swing.JOptionPane

import org.ggp.base.server.GameServer

@SuppressWarnings("serial")
class PublishButton(JButton, ActionListener):
    """ generated source for class PublishButton """
    theServer = GameServer()

    def __init__(self, theName):
        """ generated source for method __init__ """
        super(PublishButton, self).__init__(theName)
        self.addActionListener(self)
        self.setEnabled(False)

    def setServer(self, theServer):
        """ generated source for method setServer """
        self.theServer = theServer
        self.setEnabled(True)

    def actionPerformed(self, e):
        """ generated source for method actionPerformed """
        if e.getSource() == self:
            if self.theServer != None:
                if not self.theServer.getMatch().getGame().getRepositoryURL().contains("127.0.0.1"):
                    if theMatchKey != None:
                        print "Publishing to: " + theURL
                        if nChoice == JOptionPane.YES_OPTION:
                            try:
                                java.awt.Desktop.getDesktop().browse(java.net.URI.create(theURL))
                            except Exception as ee:
                                ee.printStackTrace()
                    else:
                        JOptionPane.showMessageDialog(self, "Unknown problem when publishing match.", "Publishing Match Online", JOptionPane.ERROR_MESSAGE)
                else:
                    JOptionPane.showMessageDialog(self, "Could not publish a game that is only stored locally.", "Publishing Match Online", JOptionPane.ERROR_MESSAGE)
                setEnabled(False)

