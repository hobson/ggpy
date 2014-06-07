#!/usr/bin/env python
""" generated source for module FileUtils """
# package: org.ggp.base.util.files
import java.io.BufferedReader

import java.io.File

import java.io.FileNotFoundException

import java.io.FileOutputStream

import java.io.FileReader

import java.io.IOException

import java.io.PrintStream

class FileUtils(object):
    """ generated source for class FileUtils """
    # 
    #      * @param filePath the name of the file to open.
    #      
    @classmethod
    def readFileAsString(cls, file_):
        """ generated source for method readFileAsString """
        try:
            while (numRead = reader.read(buf)) != -1:
                fileData.append(buf, 0, numRead)
            reader.close()
            return fileData.__str__()
        except FileNotFoundException as e:
            return None
        except IOException as e:
            e.printStackTrace()
            return None

    @classmethod
    def writeStringToFile(cls, file_, s):
        """ generated source for method writeStringToFile """
        out = PrintStream(FileOutputStream(file_, False))
        try:
            out.print_(s)
        finally:
            out.close()

