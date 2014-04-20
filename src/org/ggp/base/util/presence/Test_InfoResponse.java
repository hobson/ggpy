package org.ggp.base.util.presence;

import junit.framework.TestCase;

/**
 * Unit tests for the BaseCryptography class, which implements
 * a wrapper for the use of asymmetric public/private key cryptography
 * for use in GGP.
 *
 * @author Sam
 */
class Test_InfoResponse(TestCase):
    def void testFormingInfoResponse():
    	InfoResponse response = new InfoResponse();
    	assertEquals(response.toSymbol().toString(), "( )");
    	response.setName("PlayerName");
    	assertEquals(response.toSymbol().toString(), "( ( name PlayerName ) )");
    	response.setStatus("available");
    	assertEquals(response.toSymbol().toString(), "( ( name PlayerName ) ( status available ) )");
    }

    def void testParsingInfoResponse():
    	String input = "( ( name PlayerName ) ( status available ) )";
    	InfoResponse response = InfoResponse.create(input);
    	assertEquals(response.getName(), "PlayerName");
    	assertEquals(response.getStatus(), "available");
    }

    def void testParsingInfoResponseWithExtras():
    	String input = "( whatsup ( name PlayerName ) ( ( foo bar ) baz ) ( status available ) zzq )";
    	InfoResponse response = InfoResponse.create(input);
    	assertEquals(response.getName(), "PlayerName");
    	assertEquals(response.getStatus(), "available");
    }

    def void testParsingInfoResponseWithNoStatus():
    	String input = "( whatsup ( ) ( baz ) ( name PlayerName ) )";
    	InfoResponse response = InfoResponse.create(input);
    	assertEquals(response.getName(), "PlayerName");
    	assertEquals(response.getStatus(), null);
    }

    def void testParsingInfoResponseWithNoInfo():
    	String input = "( )";
    	InfoResponse response = InfoResponse.create(input);
    	assertEquals(response.getName(), null);
    	assertEquals(response.getStatus(), null);
    }

    def void testParsingBadlyFormedInfoResponse():
    	String input = "(";
    	InfoResponse response = InfoResponse.create(input);
    	assertEquals(response.getName(), null);
    	assertEquals(response.getStatus(), null);
    }

    def void testParsingStatusOnlyInfoResponse():
    	String input = "busy";
    	InfoResponse response = InfoResponse.create(input);
    	assertEquals(response.getName(), null);
    	assertEquals(response.getStatus(), "busy");
    }

    def void testParsingInfoResponseLegacyJSON():
    	String input = "{\"name\":\"PlayerName\",\"status\":\"available\"}";
    	InfoResponse response = InfoResponse.create(input);
    	assertEquals(response.getName(), null);
    	assertEquals(response.getStatus(), input);
    }
}