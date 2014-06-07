#!/usr/bin/env python
""" generated source for module Test_BaseCryptography """
# package: org.ggp.base.util.crypto
import junit.framework.TestCase

import org.ggp.base.util.crypto.BaseCryptography.EncodedKeyPair

# 
#  * Unit tests for the BaseCryptography class, which implements
#  * a wrapper for the use of asymmetric public/private key cryptography
#  * for use in GGP.
#  *
#  * @author Sam
#  
class Test_BaseCryptography(TestCase):
    """ generated source for class Test_BaseCryptography """
    def testSimpleCryptography(self):
        """ generated source for method testSimpleCryptography """
        #  Not an ideal unit test because generating the key takes a while,
        #  but it's useful to have test coverage at all so we'll make due.
        theKeys = BaseCryptography.generateKeys()
        theSK = theKeys.thePrivateKey
        thePK = theKeys.thePublicKey
        theData = "Hello world!"
        theSignature = BaseCryptography.signData(theSK, theData)
        assertTrue(BaseCryptography.verifySignature(thePK, theSignature, theData))

