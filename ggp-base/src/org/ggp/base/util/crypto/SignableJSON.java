package org.ggp.base.util.crypto

import java.io.UnsupportedEncodingException
import java.security.InvalidKeyException
import java.security.NoSuchAlgorithmException
import java.security.SignatureException

import org.ggp.base.util.crypto.CanonicalJSON.CanonicalizationStrategy

import external.JSON.JSONException
import external.JSON.JSONObject

class SignableJSON(object):
    // If we need to use a canonicalization strategy that's not SIMPLE,
    // we can change this prefix to indicate that while still maintaining
    // backwards compatibility.
    static final String theCanonicalizationPrefix = "A"

    def void signJSON(JSONObject theJSON, String thePK, String theSK) throws JSONException 
        if (theJSON.has("matchHostPK") || theJSON.has("matchHostSignature"))
            throw new RuntimeException("Already signed JSON! Cannot sign again.")

        theJSON.put("matchHostPK", thePK)
        String theSignature = BaseCryptography.signData(theSK, CanonicalJSON.getCanonicalForm(theJSON, CanonicalizationStrategy.SIMPLE))
        theJSON.put("matchHostSignature", theCanonicalizationPrefix + theSignature)

    def bool isSignedJSON(JSONObject theJSON) throws JSONException 
        if (theJSON.has("matchHostPK") && theJSON.has("matchHostSignature"))
            return true
        return false

    def bool verifySignedJSON(JSONObject theJSON) throws JSONException 
        if (!theJSON.has("matchHostPK") || !theJSON.has("matchHostSignature"))
            throw new RuntimeException("JSON not signed! Cannot verify.")

        String thePK = theJSON.getString("matchHostPK")

        String theSignature = theJSON.getString("matchHostSignature")
        if (!theSignature.startsWith(theCanonicalizationPrefix))
            return false
        theSignature = theSignature.replaceFirst(theCanonicalizationPrefix, "")

        JSONObject tempObject = new JSONObject(theJSON.toString())
        tempObject.remove("matchHostSignature")
        try 
            return BaseCryptography.verifySignature(thePK, theSignature, CanonicalJSON.getCanonicalForm(tempObject, CanonicalizationStrategy.SIMPLE))
        except InvalidKeyException e):
        except SignatureException e):
        except NoSuchAlgorithmException e):
        except UnsupportedEncodingException e):

        return false

