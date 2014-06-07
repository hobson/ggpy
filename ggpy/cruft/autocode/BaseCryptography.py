#!/usr/bin/env python
""" generated source for module BaseCryptography """
# package: org.ggp.base.util.crypto
import java.io.UnsupportedEncodingException

import java.security.InvalidKeyException

import java.security.KeyFactory

import java.security.KeyPair

import java.security.KeyPairGenerator

import java.security.NoSuchAlgorithmException

import java.security.PrivateKey

import java.security.PublicKey

import java.security.Signature

import java.security.SignatureException

import java.security.spec.InvalidKeySpecException

import java.security.spec.PKCS8EncodedKeySpec

import java.security.spec.X509EncodedKeySpec

import external.Base64Coder.Base64Coder

import external.JSON.JSONException

import external.JSON.JSONObject

class BaseCryptography(object):
    """ generated source for class BaseCryptography """
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        k = generateKeys()
        print "{\"PK\":\"" + k.thePublicKey + "\", \"SK\":\"" + k.thePrivateKey + "\"}"

    @classmethod
    def generateKeys(cls):
        """ generated source for method generateKeys """
        try:
            #  Generate a 2048-bit RSA key pair
            keyGen.initialize(2048)
            return EncodedKeyPair(publicKey, privateKey)
        except NoSuchAlgorithmException as e:
            return None

    @classmethod
    def signData(cls, thePrivateKey, theData):
        """ generated source for method signData """
        theSK = decodePrivateKey(thePrivateKey)
        if theSK == None:
            return None
        try:
            sig.initSign(theSK)
            sig.update(theData.getBytes("UTF-8"))
            return encodeSignature(sig.sign())
        except SignatureException as e:
            pass
        except UnsupportedEncodingException as e:
            pass
        except InvalidKeyException as e:
            pass
        except NoSuchAlgorithmException as e:
            pass
        return None

    @classmethod
    def verifySignature(cls, thePublicKey, theSignature, theData):
        """ generated source for method verifySignature """
        thePK = decodePublicKey(thePublicKey)
        if thePK == None:
            raise SignatureException("Could not reconstruct public key.")
        theSigBytes = decodeSignature(theSignature)
        if theSigBytes == None:
            raise SignatureException("Could not reconstruct signature.")
        sig = Signature.getInstance("SHA1WithRSA")
        sig.initVerify(thePK)
        sig.update(theData.getBytes("UTF-8"))
        return sig.verify(theSigBytes)

    #  Class to hold a pair of string-encoded keys 
    class EncodedKeyPair(object):
        """ generated source for class EncodedKeyPair """
        thePublicKey = str()
        thePrivateKey = str()

        @overloaded
        def __init__(self, thePK, theSK):
            """ generated source for method __init__ """
            self.thePublicKey = encodeKey(thePK)
            self.thePrivateKey = encodeKey(theSK)

        @__init__.register(object, str)
        def __init___0(self, theKeyJSON):
            """ generated source for method __init___0 """
            theJSON = JSONObject(theKeyJSON)
            self.thePublicKey = theJSON.getString("PK")
            self.thePrivateKey = theJSON.getString("SK")

    #  Functions for encoding and decoding public and private keys 
    @classmethod
    @overloaded
    def encodeKey(cls, thePK):
        """ generated source for method encodeKey """
        return theCryptographyPrefix + encodeBytes(thePK.getEncoded())

    @classmethod
    @encodeKey.register(object, PrivateKey)
    def encodeKey_0(cls, theSK):
        """ generated source for method encodeKey_0 """
        return theCryptographyPrefix + encodeBytes(theSK.getEncoded())

    @classmethod
    def encodeSignature(cls, theSignatureBytes):
        """ generated source for method encodeSignature """
        return theCryptographyPrefix + encodeBytes(theSignatureBytes)

    @classmethod
    def decodePublicKey(cls, thePK):
        """ generated source for method decodePublicKey """
        if not thePK.startsWith(theCryptographyPrefix):
            return None
        thePK = thePK.replaceFirst(theCryptographyPrefix, "")
        try:
            return kf.generatePublic(X509EncodedKeySpec(decodeBytes(thePK)))
        except NoSuchAlgorithmException as e:
            return None
        except InvalidKeySpecException as e:
            return None

    @classmethod
    def decodePrivateKey(cls, theSK):
        """ generated source for method decodePrivateKey """
        if not theSK.startsWith(theCryptographyPrefix):
            return None
        theSK = theSK.replaceFirst(theCryptographyPrefix, "")
        try:
            return kf.generatePrivate(PKCS8EncodedKeySpec(decodeBytes(theSK)))
        except NoSuchAlgorithmException as e:
            return None
        except InvalidKeySpecException as e:
            return None

    @classmethod
    def decodeSignature(cls, theSig):
        """ generated source for method decodeSignature """
        if not theSig.startsWith(theCryptographyPrefix):
            return None
        theSig = theSig.replaceFirst(theCryptographyPrefix, "")
        return decodeBytes(theSig)

    theCryptographyPrefix = "0"

    #  Functions for encoding/decoding arrays of bytes 
    @classmethod
    def encodeBytes(cls, theBytes):
        """ generated source for method encodeBytes """
        return str(Base64Coder.encode(theBytes))

    @classmethod
    def decodeBytes(cls, theString):
        """ generated source for method decodeBytes """
        return Base64Coder.decode(theString)


if __name__ == '__main__':
    import sys
    BaseCryptography.main(sys.argv)

