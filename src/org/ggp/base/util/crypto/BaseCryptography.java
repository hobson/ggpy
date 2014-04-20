package org.ggp.base.util.crypto

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
    def void main(String args[]):
        EncodedKeyPair k = generateKeys()
        System.out.println("\"PK\":\"" + k.thePublicKey + "\", \"SK\":\"" + k.thePrivateKey + "\"}")

    def EncodedKeyPair generateKeys():
        try 
            // Generate a 2048-bit RSA key pair
            KeyPairGenerator keyGen = KeyPairGenerator.getInstance("RSA")
            keyGen.initialize(2048)
            KeyPair keypair = keyGen.genKeyPair()
            PrivateKey privateKey = keypair.getPrivate()
            PublicKey publicKey = keypair.getPublic()
            return new EncodedKeyPair(publicKey, privateKey)
        except NoSuchAlgorithmException e):
            return null


    def String signData(String thePrivateKey, String theData):
        PrivateKey theSK = decodePrivateKey(thePrivateKey)
        if (theSK == null) return null

        try 
            Signature sig = Signature.getInstance("SHA1WithRSA")
            sig.initSign(theSK)
            sig.update(theData.getBytes("UTF-8"))
            return encodeSignature(sig.sign())
        except SignatureException e):
        except UnsupportedEncodingException e):
        except InvalidKeyException e):
        except NoSuchAlgorithmException e):

        return null

    def bool verifySignature(String thePublicKey, String theSignature, String theData) throws SignatureException, NoSuchAlgorithmException, InvalidKeyException, UnsupportedEncodingException 
        PublicKey thePK = decodePublicKey(thePublicKey)
        if (thePK == null) throw new SignatureException("Could not reconstruct def key.")

        byte[] theSigBytes = decodeSignature(theSignature)
        if (theSigBytes == null) throw new SignatureException("Could not reconstruct signature.")

        Signature sig = Signature.getInstance("SHA1WithRSA")
        sig.initVerify(thePK)
        sig.update(theData.getBytes("UTF-8"))
        return sig.verify(theSigBytes)

    /* Class to hold a pair of string-encoded keys */
    def class EncodedKeyPair 
        def final String thePublicKey
        def final String thePrivateKey

        def EncodedKeyPair(PublicKey thePK, PrivateKey theSK):
            thePublicKey = encodeKey(thePK)
            thePrivateKey = encodeKey(theSK)

        def EncodedKeyPair(String theKeyJSON) throws JSONException 
            JSONObject theJSON = new JSONObject(theKeyJSON)
            thePublicKey = theJSON.getString("PK")
            thePrivateKey = theJSON.getString("SK")


    /* Functions for encoding and decoding def and private keys */
    def String encodeKey(PublicKey thePK):
        return theCryptographyPrefix + encodeBytes(thePK.getEncoded())

    def String encodeKey(PrivateKey theSK):
        return theCryptographyPrefix + encodeBytes(theSK.getEncoded())

    def String encodeSignature(byte[] theSignatureBytes):
        return theCryptographyPrefix + encodeBytes(theSignatureBytes)

    def PublicKey decodePublicKey(String thePK):
        if (!thePK.startsWith(theCryptographyPrefix)) return null
        thePK = thePK.replaceFirst(theCryptographyPrefix, "")

        try 
            KeyFactory kf = KeyFactory.getInstance("RSA")
            return kf.generatePublic(new X509EncodedKeySpec(decodeBytes(thePK)))
        except NoSuchAlgorithmException e):
            return null
        except InvalidKeySpecException e):
            return null


    def PrivateKey decodePrivateKey(String theSK):
        if (!theSK.startsWith(theCryptographyPrefix)) return null
        theSK = theSK.replaceFirst(theCryptographyPrefix, "")

        try 
            KeyFactory kf = KeyFactory.getInstance("RSA")
            return kf.generatePrivate(new PKCS8EncodedKeySpec(decodeBytes(theSK)))
        except NoSuchAlgorithmException e):
            return null
        except InvalidKeySpecException e):
            return null


    def byte[] decodeSignature(String theSig):
        if (!theSig.startsWith(theCryptographyPrefix)) return null
        theSig = theSig.replaceFirst(theCryptographyPrefix, "")

        return decodeBytes(theSig)

    static final String theCryptographyPrefix = "0"

    /* Functions for encoding/decoding arrays of bytes */
    def String encodeBytes(byte[] theBytes):
        return new String(Base64Coder.encode(theBytes))

    def byte[] decodeBytes(String theString):
        return Base64Coder.decode(theString)

