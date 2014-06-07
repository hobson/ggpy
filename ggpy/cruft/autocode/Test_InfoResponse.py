#!/usr/bin/env python
""" generated source for module Test_InfoResponse """
# package: org.ggp.base.util.presence
import junit.framework.TestCase

# 
#  * Unit tests for the BaseCryptography class, which implements
#  * a wrapper for the use of asymmetric public/private key cryptography
#  * for use in GGP.
#  *
#  * @author Sam
#  
class Test_InfoResponse(TestCase):
    """ generated source for class Test_InfoResponse """
    def testFormingInfoResponse(self):
        """ generated source for method testFormingInfoResponse """
        response = InfoResponse()
        assertEquals(response.toSymbol().__str__(), "( )")
        response.setName("PlayerName")
        assertEquals(response.toSymbol().__str__(), "( ( name PlayerName ) )")
        response.setStatus("available")
        assertEquals(response.toSymbol().__str__(), "( ( name PlayerName ) ( status available ) )")

    def testParsingInfoResponse(self):
        """ generated source for method testParsingInfoResponse """
        input = "( ( name PlayerName ) ( status available ) )"
        response = InfoResponse.create(input)
        assertEquals(response.__name__, "PlayerName")
        assertEquals(response.getStatus(), "available")

    def testParsingInfoResponseWithExtras(self):
        """ generated source for method testParsingInfoResponseWithExtras """
        input = "( whatsup ( name PlayerName ) ( ( foo bar ) baz ) ( status available ) zzq )"
        response = InfoResponse.create(input)
        assertEquals(response.__name__, "PlayerName")
        assertEquals(response.getStatus(), "available")

    def testParsingInfoResponseWithNoStatus(self):
        """ generated source for method testParsingInfoResponseWithNoStatus """
        input = "( whatsup ( ) ( baz ) ( name PlayerName ) )"
        response = InfoResponse.create(input)
        assertEquals(response.__name__, "PlayerName")
        assertEquals(response.getStatus(), None)

    def testParsingInfoResponseWithNoInfo(self):
        """ generated source for method testParsingInfoResponseWithNoInfo """
        input = "( )"
        response = InfoResponse.create(input)
        assertEquals(response.__name__, None)
        assertEquals(response.getStatus(), None)

    def testParsingBadlyFormedInfoResponse(self):
        """ generated source for method testParsingBadlyFormedInfoResponse """
        input = "("
        response = InfoResponse.create(input)
        assertEquals(response.__name__, None)
        assertEquals(response.getStatus(), None)

    def testParsingStatusOnlyInfoResponse(self):
        """ generated source for method testParsingStatusOnlyInfoResponse """
        input = "busy"
        response = InfoResponse.create(input)
        assertEquals(response.__name__, None)
        assertEquals(response.getStatus(), "busy")

    def testParsingInfoResponseLegacyJSON(self):
        """ generated source for method testParsingInfoResponseLegacyJSON """
        input = "{\"name\":\"PlayerName\",\"status\":\"available\"}"
        response = InfoResponse.create(input)
        assertEquals(response.__name__, None)
        assertEquals(response.getStatus(), input)

