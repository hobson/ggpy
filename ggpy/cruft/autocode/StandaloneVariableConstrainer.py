#!/usr/bin/env python
""" generated source for module StandaloneVariableConstrainer """
# package: org.ggp.base.util.gdl.transforms.standalone
import java.io.BufferedWriter

import java.io.File

import java.io.FileWriter

import java.io.IOException

import java.util.List

import org.ggp.base.util.files.FileUtils

import org.ggp.base.util.game.Game

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.transforms.VariableConstrainer

import org.ggp.base.validator.StaticValidator

import org.ggp.base.validator.ValidatorException

# 
#  * The standalone version of VariableConstrainer can be run as its own
#  * program. It takes a .kif file as input and generates a new .kif file
#  * with the modified output. The new filename is (original name)_VARCONST.kif.
#  *
#  * The new file is not intended to be particularly legible; it is
#  * intended mainly for use by other programs.
#  *
#  * @author Alex Landau
#  *
#  
class StandaloneVariableConstrainer(object):
    """ generated source for class StandaloneVariableConstrainer """
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        if not args[0].endsWith(".kif") or len(args):
            print "Please enter the path of a .kif file as an argument."
            return
        filename = args[0]
        theGame = Game.createEphemeralGame(Game.preprocessRulesheet(FileUtils.readFileAsString(File(filename))))
        if theGame.getRules() == None or theGame.getRules().size() == 0:
            System.err.println("Problem reading the file " + filename + " or parsing the GDL.")
            return
        try:
            StaticValidator().checkValidity(theGame)
        except ValidatorException as e:
            System.err.println("GDL validation error: " + e.__str__())
            return
        transformedDescription = VariableConstrainer.replaceFunctionValuedVariables(theGame.getRules())
        newFilename = filename.substring(0, filename.lastIndexOf(".kif")) + "_VARCONST.kif"
        try:
            for gdl in transformedDescription:
                out.write(gdl.__str__())
                out.newLine()
            out.close()
        except IOException as e:
            System.err.println("There was an error writing the translated GDL file " + newFilename + ".")
            e.printStackTrace()


if __name__ == '__main__':
    import sys
    StandaloneVariableConstrainer.main(sys.argv)

