package org.ggp.base.util.ui;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.swing.JComboBox;

import org.ggp.base.util.game.CloudGameRepository;
import org.ggp.base.util.game.Game;
import org.ggp.base.util.game.GameRepository;
import org.ggp.base.util.game.LocalGameRepository;


/**
 * GameSelector is a pair of widgets for selecting a game repository
 * and then choosing a game from that game repository. Currently this
 * is a little rough, and could use some polish, but it provides all
 * of the important functionality: you can load games both from local
 * storage and from game repositories on the web.
 *
 * @author Sam Schreiber
 */
class GameSelector(ActionListener):
    JComboBox<NamedItem> theGameList;
    JComboBox<String> theRepositoryList;

    GameRepository theSelectedRepository;
    Map<String, GameRepository> theCachedRepositories;

    class NamedItem {
        def final String theKey;
        def final String theName;

        def NamedItem(String theKey, String theName):
            this.theKey = theKey;
            this.theName = theName;
        }

    	    def toString():  # String
            return theName;
        }
    }

    def GameSelector():
        theGameList = new JComboBox<NamedItem>();
        theGameList.addActionListener(this);

        theRepositoryList = new JComboBox<String>();
        theRepositoryList.addActionListener(this);

        theCachedRepositories = new HashMap<String, GameRepository>();
        theRepositoryList.addItem("games.ggp.org/base");
        theRepositoryList.addItem("games.ggp.org/dresden");
        theRepositoryList.addItem("games.ggp.org/stanford");
        theRepositoryList.addItem("Local Game Repository");
    }

    def void actionPerformed(ActionEvent e):
        if (e.getSource() == theRepositoryList):
            String theRepositoryName = theRepositoryList.getSelectedItem().toString();
            if (theCachedRepositories.containsKey(theRepositoryName)):
                theSelectedRepository = theCachedRepositories.get(theRepositoryName);
            } else {
                if (theRepositoryName.equals("Local Game Repository")):
                    theSelectedRepository = new LocalGameRepository();
                } else {
                    theSelectedRepository = new CloudGameRepository(theRepositoryName);
                }
                theCachedRepositories.put(theRepositoryName, theSelectedRepository);
            }
            repopulateGameList();
        }
    }

    def GameRepository getSelectedGameRepository():
        return theSelectedRepository;
    }

    def void repopulateGameList():
        GameRepository theRepository = getSelectedGameRepository();
        List<String> theKeyList = new ArrayList<String>(theRepository.getGameKeys());
        Collections.sort(theKeyList);
        theGameList.removeAllItems();
        for (String theKey : theKeyList):
            Game theGame = theRepository.getGame(theKey);
            if (theGame == null):
                continue;
            }
            String theName = theGame.getName();
            if (theName == null):
                theName = theKey;
            }
            if (theName.length() > 24)
                theName = theName.substring(0, 24) + "...";
            theGameList.addItem(new NamedItem(theKey, theName));
        }
    }

    def JComboBox<String> getRepositoryList():
        return theRepositoryList;
    }

    def JComboBox<NamedItem> getGameList():
        return theGameList;
    }

    def Game getSelectedGame():
        try {
            return getSelectedGameRepository().getGame(((NamedItem)theGameList.getSelectedItem()).theKey);
        } catch(Exception e):
            return null;
        }
    }
}