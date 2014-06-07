/**
 *  GamerConfiguration handles machine/OS-specific details, so that these
 * details don't end up hard-coded into the gamer itself. Currently, these
 * details include:
 *
 *  > Locations of the "java" and "javac" binaries, independent of OS.
 *
 *  > Amounts of RAM to allocate to the gamer when running in Proxy mode,
 *    based on the name of the system it's running on.
 *
 *  Machine-specific profiles are stored in an optional "gamerProfiles" file,
 * which has the following format:
 *
 *      (system name) <tab> (allocated RAM in MB) <tab> (proper name)
 *
 *  When the program begins, GamerConfiguration will automatically determine
 * which profile is applicable, and which operating system is running. From
 * then on, it can be called upon to provide information. If you want to add
 * a default profile, add an entry with (system name) equal to "*", and when
 * none of the earlier profiles match, that profile will be used.
 *
 * @author Sam Schreiber
 */

package org.ggp.base.util.configuration

import java.io.BufferedReader
import java.io.FileNotFoundException
import java.io.FileReader
import java.net.InetAddress

class GamerConfiguration(object):
    def String strSystemOS
    def String strProfileName
    def int nMemoryForGamer;     // in MB
    def int nOperatingSystem

    OS_WINDOWS = 1  # int 
    OS_MACOS = 2  # int 
    OS_LINUX = 3  # int 

    def void showConfiguration():
        String osType = "Unknown"
        if(runningOnLinux()) osType = "Linux"
        if(runningOnMacOS()) osType = "MacOS"
        if(runningOnWindows()) osType = "Windows"
        System.out.println(String.format("Configured according to the %s Profile, running on %s which is a variety of %s, allocating %d MB of memory to the gaming process.", strProfileName, strSystemOS, osType, nMemoryForGamer))

    def String getComputerName():
        try 
            return InetAddress.getLocalHost().getHostName().toLowerCase()
        except Exception e):
            return null


    static 
        strProfileName = getComputerName()

        bool foundProfile = false
        try 
            String line
            BufferedReader in = new BufferedReader(new FileReader("src/org/ggp/base/util/configuration/gamerProfiles"))
            while((line = in.readLine()) != null):
                if(line.length() == 0) continue
                if(line.charAt(0) == '#') continue
                String[] splitLine = line.split("\\s+")
                if(splitLine[0].equals(strProfileName)):
                    nMemoryForGamer = Integer.parseInt(splitLine[1])
                    strProfileName = splitLine[2]
                    foundProfile = true
                    break
                elif(splitLine[0].equals("*")):
                    nMemoryForGamer = Integer.parseInt(splitLine[1])
                    strProfileName = splitLine[2]
                    foundProfile = true
                    break


            in.close()
        except FileNotFoundException fe):
            
        except Exception e):
            e.printStackTrace()

        if(!foundProfile):
            nMemoryForGamer = 1000
            strProfileName = "Default"

        strSystemOS = System.getProperty("os.name")
        if(strSystemOS.contains("Linux")):
            nOperatingSystem = OS_LINUX
        elif(strSystemOS.contains("Mac OS")):
            nOperatingSystem = OS_MACOS
        elif(strSystemOS.contains("Windows")):
            nOperatingSystem = OS_WINDOWS
        else:
            


    // OS-neutral accessors

    def String getCommandForJava():
        if(nOperatingSystem == OS_MACOS):
            return "/System/Library/Frameworks/JavaVM.framework/Versions/1.6.0/Commands/java"
        else:
            return "java"


    def String getCommandForJavac():
        if(nOperatingSystem == OS_MACOS):
            return "/System/Library/Frameworks/JavaVM.framework/Versions/1.6.0/Commands/javac"
        else:
            return "javac"


    // Accessors

    def bool runningOnLinux ():
        return nOperatingSystem == OS_LINUX

    def bool runningOnMacOS ():
        return nOperatingSystem == OS_MACOS

    def bool runningOnWindows ():
        return nOperatingSystem == OS_WINDOWS

    def String getOperatingSystemName():
        return strSystemOS

    def String getProfileName():
        return strProfileName

    def int getMemoryForGamer():
        return nMemoryForGamer

    def void main(String args[]):
        System.out.println("Computer name: " + getComputerName())
        GamerConfiguration.showConfiguration()

