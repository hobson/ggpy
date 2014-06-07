#!/usr/bin/env python
""" generated source for module GamerConfiguration """
# 
#  *  GamerConfiguration handles machine/OS-specific details, so that these
#  * details don't end up hard-coded into the gamer itself. Currently, these
#  * details include:
#  *
#  *  > Locations of the "java" and "javac" binaries, independent of OS.
#  *
#  *  > Amounts of RAM to allocate to the gamer when running in Proxy mode,
#  *    based on the name of the system it's running on.
#  *
#  *  Machine-specific profiles are stored in an optional "gamerProfiles" file,
#  * which has the following format:
#  *
#  *      (system name) <tab> (allocated RAM in MB) <tab> (proper name)
#  *
#  *  When the program begins, GamerConfiguration will automatically determine
#  * which profile is applicable, and which operating system is running. From
#  * then on, it can be called upon to provide information. If you want to add
#  * a default profile, add an entry with (system name) equal to "*", and when
#  * none of the earlier profiles match, that profile will be used.
#  *
#  * @author Sam Schreiber
#  
# package: org.ggp.base.util.configuration
import java.io.BufferedReader

import java.io.FileNotFoundException

import java.io.FileReader

import java.net.InetAddress

class GamerConfiguration(object):
    """ generated source for class GamerConfiguration """
    strSystemOS = str()
    strProfileName = str()
    nMemoryForGamer = int()

    #  in MB
    nOperatingSystem = int()
    OS_WINDOWS = 1
    OS_MACOS = 2
    OS_LINUX = 3

    @classmethod
    def showConfiguration(cls):
        """ generated source for method showConfiguration """
        osType = "Unknown"
        if runningOnLinux():
            osType = "Linux"
        if runningOnMacOS():
            osType = "MacOS"
        if runningOnWindows():
            osType = "Windows"
        print "Configured according to the {:s} Profile, running on {:s} which is a variety of {:s}, allocating {:d} MB of memory to the gaming process.".format(cls.strProfileName, cls.strSystemOS, osType, cls.nMemoryForGamer)

    @classmethod
    def getComputerName(cls):
        """ generated source for method getComputerName """
        try:
            return InetAddress.getLocalHost().getHostName().lower()
        except Exception as e:
            return None

    foundProfile = False
    line = str()
    in_ = BufferedReader(FileReader("src/org/ggp/base/util/configuration/gamerProfiles"))
    splitLine = line.split("\\s+")

    @classmethod
    def getCommandForJava(cls):
        """ generated source for method getCommandForJava """
        if cls.nOperatingSystem == cls.OS_MACOS:
            return "/System/Library/Frameworks/JavaVM.framework/Versions/1.6.0/Commands/java"
        else:
            return "java"

    @classmethod
    def getCommandForJavac(cls):
        """ generated source for method getCommandForJavac """
        if cls.nOperatingSystem == cls.OS_MACOS:
            return "/System/Library/Frameworks/JavaVM.framework/Versions/1.6.0/Commands/javac"
        else:
            return "javac"

    @classmethod
    def runningOnLinux(cls):
        """ generated source for method runningOnLinux """
        return cls.nOperatingSystem == cls.OS_LINUX

    @classmethod
    def runningOnMacOS(cls):
        """ generated source for method runningOnMacOS """
        return cls.nOperatingSystem == cls.OS_MACOS

    @classmethod
    def runningOnWindows(cls):
        """ generated source for method runningOnWindows """
        return cls.nOperatingSystem == cls.OS_WINDOWS

    @classmethod
    def getOperatingSystemName(cls):
        """ generated source for method getOperatingSystemName """
        return cls.strSystemOS

    @classmethod
    def getProfileName(cls):
        """ generated source for method getProfileName """
        return cls.strProfileName

    @classmethod
    def getMemoryForGamer(cls):
        """ generated source for method getMemoryForGamer """
        return cls.nMemoryForGamer

    @classmethod
    def main(cls, args):
        """ generated source for method main """
        print "Computer name: " + cls.getComputerName()
        GamerConfiguration.showConfiguration()


if __name__ == '__main__':
    import sys
    GamerConfiguration.main(sys.argv)

