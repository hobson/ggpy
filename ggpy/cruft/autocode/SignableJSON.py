#!/usr/bin/env python
""" generated source for module SignableJSON """
# package: org.ggp.base.util.crypto
import java.io.UnsupportedEncodingException

import java.security.InvalidKeyException

import java.security.NoSuchAlgorithmException

import java.security.SignatureException

import org.ggp.base.util.crypto.CanonicalJSON.CanonicalizationStrategy

import external.JSON.JSONException

import external.JSON.JSONObject

class SignableJSON(object):
    """ generated source for class SignableJSON """
    #  If we need to use a canonicalization strategy that's not SIMPLE,
    #  we can change this prefix to indicate that while still maintaining
    #  backwards compatibility.
    theCanonicalizationPrefix = "A"

    @classmethod
    def signJSON(cls, theJSON, thePK, theSK):
        """ generated source for method signJSON """
        if theJSON.has("matchHostPK") or theJSON.has("matchHostSignature"):
            raise RuntimeException("Already signed JSON! Cannot sign again.")
        theJSON.put("matchHostPK", thePK)
        theSignature = BaseCryptography.signData(theSK, CanonicalJSON.getCanonicalForm(theJSON, CanonicalizationStrategy.SIMPLE))
        theJSON.put("matchHostSignature", cls.theCanonicalizationPrefix + theSignature)

    @classmethod
    def isSignedJSON(cls, theJSON):
        """ generated source for method isSignedJSON """
        if theJSON.has("matchHostPK") and theJSON.has("matchHostSignature"):
            return True
        return False

    @classmethod
    def verifySignedJSON(cls, theJSON):
        """ generated source for method verifySignedJSON """
        if not theJSON.has("matchHostPK") or not theJSON.has("matchHostSignature"):
            raise RuntimeException("JSON not signed! Cannot verify.")
        thePK = theJSON.getString("matchHostPK")
        theSignature = theJSON.getString("matchHostSignature")
        if not theSignature.startsWith(cls.theCanonicalizationPrefix):
            return False
        theSignature = theSignature.replaceFirst(cls.theCanonicalizationPrefix, "")
        tempObject = JSONObject(theJSON.__str__())
        tempObject.remove("matchHostSignature")
        try:
            return BaseCryptography.verifySignature(thePK, theSignature, CanonicalJSON.getCanonicalForm(tempObject, CanonicalizationStrategy.SIMPLE))
        except InvalidKeyException as e:
            pass
        except SignatureException as e:
            pass
        except NoSuchAlgorithmException as e:
            pass
        except UnsupportedEncodingException as e:
            pass
        return False

