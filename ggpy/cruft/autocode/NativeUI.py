#!/usr/bin/env python
""" generated source for module NativeUI """
# package: org.ggp.base.util.ui
import javax.swing.UIManager

# 
#  * NativeUI is a simple user-interface wrapper around the snippet of code
#  * that configures the Java UI to adopt the look-and-feel of the operating
#  * system that it's running on. This is wrapped into its own separate class
#  * because it's used in a number of different places (all of the graphical
#  * applications) and it's useful to edit it centrally.
#  *
#  * @author Sam Schreiber
#  
class NativeUI(object):
    """ generated source for class NativeUI """
    @classmethod
    def setNativeUI(cls):
        """ generated source for method setNativeUI """
        try:
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName())
        except Exception as e:
            System.err.println("Unable to set native look and feel.")
            #  e.printStackTrace();

