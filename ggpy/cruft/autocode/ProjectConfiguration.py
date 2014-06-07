#!/usr/bin/env python
""" generated source for module ProjectConfiguration """
# 
#  * ProjectConfiguration handles the project-specific directory settings.
#  * This class stores the paths of the game directory so it can quickly be changed and overridden.
#  *
#  * @author Sam Schreiber
#  
# package: org.ggp.base.util.configuration
import java.io.File

class ProjectConfiguration(object):
    """ generated source for class ProjectConfiguration """
    #  Game rulesheet repository information 
    gamesRootDirectoryPath = "games"
    gameImagesDirectory = File(File(gamesRootDirectoryPath, "resources"), "images")

