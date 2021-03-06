package org.ggp.base.util.files

import java.io.BufferedReader
import java.io.File
import java.io.FileNotFoundException
import java.io.FileOutputStream
import java.io.FileReader
import java.io.IOException
import java.io.PrintStream

class FileUtils(object):
    /**
     * @param filePath the name of the file to open.
     */
    def String readFileAsString(File file):
        try 
        	BufferedReader reader = new BufferedReader(new FileReader(file))
            StringBuilder fileData = new StringBuilder(10000)
            char[] buf = new char[1024]
            int numRead=0
            while((numRead=reader.read(buf)) != -1)
                fileData.append(buf, 0, numRead)

            reader.close()
            return fileData.toString()
        except FileNotFoundException e):
            return null
        except IOException e):
            e.printStackTrace()
            return null

    def void writeStringToFile(File file, String s) throws IOException 
        PrintStream out = new PrintStream(new FileOutputStream(file, false))
        try 
            out.print(s)
        } finally 
            out.close()

