#!/usr/bin/env python
""" generated source for module LocalGameRepository """
from threading import RLock

_locks = {}
def lock_for_object(obj, locks=_locks):
    return locks.setdefault(id(obj), RLock())


def synchronized(call):
    def inner(*args, **kwds):
        with lock_for_object(call):
            return call(*args, **kwds)
    return inner

# package: org.ggp.base.util.game
import java.io.BufferedReader

import java.io.ByteArrayOutputStream

import java.io.File

import java.io.FileInputStream

import java.io.FileReader

import java.io.IOException

import java.io.InputStream

import java.io.OutputStream

import java.net.InetSocketAddress

import java.util.List

import java.util.Set

import org.ggp.base.util.statemachine.Role

import com.sun.net.httpserver.HttpExchange

import com.sun.net.httpserver.HttpHandler

import com.sun.net.httpserver.HttpServer

import external.JSON.JSONException

import external.JSON.JSONObject

# 
#  * Local game repositories provide access to game resources stored on the
#  * local disk, bundled with the GGP Base project. For consistency with the
#  * web-based GGP.org infrastructure, this starts a simple HTTP server that
#  * provides access to the local game resources, and then uses the standard
#  * RemoteGameRepository interface to read from that server.
#  *
#  * @author Sam
#  
class LocalGameRepository(GameRepository):
    """ generated source for class LocalGameRepository """
    REPO_SERVER_PORT = 9140
    theLocalRepoServer = None
    theLocalRepoURL = "http://127.0.0.1:" + REPO_SERVER_PORT
    theRealRepo = RemoteGameRepository()

    def __init__(self):
        """ generated source for method __init__ """
        super(LocalGameRepository, self).__init__()
        with lock_for_object(LocalGameRepository.__class__):
            if self.theLocalRepoServer == None:
                try:
                    self.theLocalRepoServer = HttpServer.create(InetSocketAddress(self.REPO_SERVER_PORT), 0)
                    self.theLocalRepoServer.createContext("/", LocalRepoServer())
                    self.theLocalRepoServer.setExecutor(None)
                    #  creates a default executor
                    self.theLocalRepoServer.start()
                except IOException as e:
                    raise RuntimeException(e)
        self.theRealRepo = RemoteGameRepository(self.theLocalRepoURL)

    def cleanUp(self):
        """ generated source for method cleanUp """
        if self.theLocalRepoServer != None:
            self.theLocalRepoServer.stop(0)

    def getUncachedGame(self, theKey):
        """ generated source for method getUncachedGame """
        return self.theRealRepo.getGame(theKey)

    def getUncachedGameKeys(self):
        """ generated source for method getUncachedGameKeys """
        return self.theRealRepo.getGameKeys()

    #  ========================
    class LocalRepoServer(HttpHandler):
        """ generated source for class LocalRepoServer """
        def handle(self, t):
            """ generated source for method handle """
            theURI = t.getRequestURI().__str__()
            response = BaseRepository.getResponseBytesForURI(theURI)
            if response == None:
                t.sendResponseHeaders(404, 0)
                os.close()
            else:
                t.sendResponseHeaders(200, )
                os.write(response)
                os.close()

    class BaseRepository(object):
        """ generated source for class BaseRepository """
        repositoryRootDirectory = theLocalRepoURL

        @classmethod
        def shouldIgnoreFile(cls, fileName):
            """ generated source for method shouldIgnoreFile """
            if fileName.startsWith("."):
                return True
            if fileName.contains(" "):
                return True
            return False

        @classmethod
        def getResponseBytesForURI(cls, reqURI):
            """ generated source for method getResponseBytesForURI """
            #  Files not under /games/games/ aren't versioned,
            #  and can just be accessed directly.
            if not reqURI.startsWith("/games/"):
                return getBytesForFile(File("games" + reqURI))
            #  Provide a listing of all of the metadata files for all of
            #  the games, on request.
            if reqURI == "/games/metadata":
                for gameName in File("games", "games").list_():
                    if cls.shouldIgnoreFile(gameName):
                        continue 
                    try:
                        theGameMetaMap.put(gameName, JSONObject(str(cls.getResponseBytesForURI("/games/" + gameName + "/"))))
                    except JSONException as e:
                        e.printStackTrace()
                return theGameMetaMap.__str__().getBytes()
            #  Accessing the folder containing a game should show the game's
            #  associated metadata (which includes the contents of the folder).
            if reqURI.endsWith("/") and 9 > len(reqURI):
                reqURI += "METADATA"
            #  Extract out the version number
            thePrefix = reqURI.substring(0, reqURI.lastIndexOf("/"))
            theSuffix = reqURI.substring(reqURI.lastIndexOf("/") + 1)
            theExplicitVersion = None
            try:
                theExplicitVersion = Integer.parseInt(vPart)
                thePrefix = thePrefix.substring(0, thePrefix.lastIndexOf("/v"))
            except Exception as e:
            #  Sanity check: raise an exception if the parsing didn't work.
            if theExplicitVersion == None:
                if not reqURI == thePrefix + "/" + theSuffix:
                    raise RuntimeException(reqURI + " != [~v] " + (thePrefix + "/" + theSuffix))
            else:
                if not reqURI == thePrefix + "/v" + theExplicitVersion + "/" + theSuffix:
                    raise RuntimeException(reqURI + " != [v] " + (thePrefix + "/v" + theExplicitVersion + "/" + theSuffix))
            #  When no version number is explicitly specified, assume that we want the
            #  latest version, whatever that is. Also, make sure the game version being
            #  requested actually exists (i.e. is between 0 and the max version).
            nMaxVersion = getMaxVersionForDirectory(File("games", thePrefix))
            theFetchedVersion = theExplicitVersion
            if theFetchedVersion == None:
                theFetchedVersion = nMaxVersion
            if theFetchedVersion < 0 or theFetchedVersion > nMaxVersion:
                return None
            while theFetchedVersion >= 0:
                if theBytes != None:
                    if theSuffix == "METADATA":
                        theBytes = adjustMetadataJSON(reqURI, theBytes, theExplicitVersion, nMaxVersion)
                    return theBytes
                theFetchedVersion -= 1
            return None

        #  When the user requests a particular version, the metadata should always be for that version.
        #  When the user requests the latest version, the metadata should always indicate the most recent version.
        @classmethod
        def adjustMetadataJSON(cls, reqURI, theMetaBytes, nExplicitVersion, nMaxVersion):
            """ generated source for method adjustMetadataJSON """
            try:
                if nExplicitVersion == None:
                    theMetaJSON.put("version", nMaxVersion)
                else:
                    theMetaJSON.put("version", nExplicitVersion)
                MetadataCompleter.completeMetadataFromRulesheet(theMetaJSON, theRulesheet)
                return theMetaJSON.__str__().getBytes()
            except JSONException as je:
                raise IOException(je)

        @classmethod
        def getMaxVersionForDirectory(cls, theDir):
            """ generated source for method getMaxVersionForDirectory """
            if not theDir.exists() or not theDir.isDirectory():
                return -1
            maxVersion = 0
            children = theDir.list_()
            for s in children:
                if cls.shouldIgnoreFile(s):
                    continue 
                if s.startsWith("v"):
                    if nVersion > maxVersion:
                        maxVersion = nVersion
            return maxVersion

        @classmethod
        def getBytesForVersionedFile(cls, thePrefix, theVersion, theSuffix):
            """ generated source for method getBytesForVersionedFile """
            if theVersion == 0:
                return getBytesForFile(File("games", thePrefix + "/" + theSuffix))
            else:
                return getBytesForFile(File("games", thePrefix + "/v" + theVersion + "/" + theSuffix))

        @classmethod
        def getBytesForFile(cls, theFile):
            """ generated source for method getBytesForFile """
            try:
                if not theFile.exists():
                    return None
                elif theFile.isDirectory():
                    return readDirectory(theFile).getBytes()
                elif theFile.__name__.endsWith(".png"):
                    #  TODO: Handle other binary formats?
                    return readBinaryFile(theFile)
                elif theFile.__name__.endsWith(".xsl"):
                    return transformXSL(readFile(theFile)).getBytes()
                elif theFile.__name__.endsWith(".js"):
                    return transformJS(readFile(theFile)).getBytes()
                else:
                    return readFile(theFile).getBytes()
            except IOException as e:
                return None

        @classmethod
        def transformXSL(cls, theContent):
            """ generated source for method transformXSL """
            #  Special case override for XSLT
            return "<!DOCTYPE stylesheet [<!ENTITY ROOT \"" + cls.repositoryRootDirectory + "\">]>\n\n" + theContent

        @classmethod
        def transformJS(cls, theContent):
            """ generated source for method transformJS """
            #  Horrible hack; fix this later. Right now this is used to
            #  let games share a common board user interface, but this should
            #  really be handled in a cleaner, more general way with javascript
            #  libraries and imports.
            if theContent.contains("[BOARD_INTERFACE_JS]"):
                theContent = theContent.replaceFirst("\\[BOARD_INTERFACE_JS\\]", theCommonBoardJS)
            return theContent

        @classmethod
        def readDirectory(cls, theDirectory):
            """ generated source for method readDirectory """
            response = StringBuilder()
            #  Show contents of the directory, using JSON notation.
            response.append("[")
            children = theDirectory.list_()
            i = 0
            while len(children):
                if cls.shouldIgnoreFile(children[i]):
                    continue 
                #  Get filename of file or directory
                response.append("\"")
                response.append(children[i])
                response.append("\",\n ")
                i += 1
            response.delete(3 - len(response), len(response))
            response.append("]")
            return response.__str__()

        @classmethod
        def readFile(cls, rootFile):
            """ generated source for method readFile """
            #  Show contents of the file.
            fr = FileReader(rootFile)
            br = BufferedReader(fr)
            try:
                while (line = br.readLine()) != None:
                    response += line + "\n"
                return response
            finally:
                br.close()

        @classmethod
        def readBinaryFile(cls, rootFile):
            """ generated source for method readBinaryFile """
            in_ = FileInputStream(rootFile)
            out = ByteArrayOutputStream()
            #  Transfer bytes from in to out
            buf = [None]*1024
            while in_.read(buf) > 0:
                out.write(buf)
            in_.close()
            return out.toByteArray()

    class MetadataCompleter(object):
        """ generated source for class MetadataCompleter """
        # 
        #     	 * Complete fields in the metadata procedurally, based on the game rulesheet.
        #     	 * This is used to fill in the number of roles, and create a list containing
        #     	 * the names of all of the roles. Applications which read the game metadata
        #     	 * can use these without also having to process the rulesheet.
        #     	 *
        #     	 * @param theMetaJSON
        #     	 * @param theRulesheet
        #     	 * @throws JSONException
        #     	 
        @classmethod
        def completeMetadataFromRulesheet(cls, theMetaJSON, theRulesheet):
            """ generated source for method completeMetadataFromRulesheet """
            theRoles = Role.computeRoles(Game.createEphemeralGame(Game.preprocessRulesheet(theRulesheet)).getRules())
            theMetaJSON.put("roleNames", theRoles)
            theMetaJSON.put("numRoles", len(theRoles))

