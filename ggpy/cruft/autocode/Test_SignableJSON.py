#!/usr/bin/env python
""" generated source for module Test_SignableJSON """
# package: org.ggp.base.util.crypto
import junit.framework.TestCase

import org.ggp.base.util.crypto.BaseCryptography.EncodedKeyPair

import external.JSON.JSONException

import external.JSON.JSONObject

# 
#  * Unit tests for the SignableJSON class, which provides an easy way
#  * for code to sign JSON objects using PK/SK pairs, and check whether
#  * a particular object has been signed.
#  *
#  * @author Sam
#  
class Test_SignableJSON(TestCase):
    """ generated source for class Test_SignableJSON """
    def testSimpleSigning(self):
        """ generated source for method testSimpleSigning """
        p = BaseCryptography.generateKeys()
        x = JSONObject("{3:{7:9,c:4,2:5,a:6},1:2,2:3,moves:14,states:21,alpha:'beta'}")
        assertFalse(SignableJSON.isSignedJSON(x))
        SignableJSON.signJSON(x, p.thePublicKey, p.thePrivateKey)
        assertTrue(SignableJSON.isSignedJSON(x))
        assertTrue(SignableJSON.verifySignedJSON(x))
        x2 = JSONObject(x.__str__().replace(",", ", ").replace("{", "{ ").replace("}", "} "))
        assertTrue(SignableJSON.isSignedJSON(x2))
        assertTrue(SignableJSON.verifySignedJSON(x2))
        x3 = JSONObject("{1:2,2:3,3:4}")
        assertFalse(SignableJSON.isSignedJSON(x3))

