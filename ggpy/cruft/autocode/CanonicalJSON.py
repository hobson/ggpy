#!/usr/bin/env python
""" generated source for module CanonicalJSON """
# package: org.ggp.base.util.crypto
import java.util.Collection

import java.util.Iterator

import java.util.Map

import java.util.TreeSet

import external.JSON.JSONArray

import external.JSON.JSONException

import external.JSON.JSONObject

import external.JSON.JSONString

class CanonicalJSON(object):
    """ generated source for class CanonicalJSON """
    #  Right now we only support one canonicalization strategy, which is
    #      * the SIMPLE approach. In the future, we may need to make breaking changes
    #      * to the canonicalization strategy, to support unforeseen situations (e.g.
    #      * edge cases the current canonicalization strategy doesn't handle properly).
    #      * However, we'd still like to be able to canonicalize data using the older
    #      * strategies so that we can e.g. still verify signatures created using the
    #      * older canonicalization strategy. So this class is designed to be able to
    #      * support multiple canonicalization strategies, and the user chooses which
    #      * strategy is used. 
    class CanonicalizationStrategy:
        """ generated source for enum CanonicalizationStrategy """
        SIMPLE = u'SIMPLE'

    #  Helper function to generate canonical strings for JSON strings 
    @classmethod
    @overloaded
    def getCanonicalForm(cls, x, s):
        """ generated source for method getCanonicalForm """
        try:
            return cls.getCanonicalForm(JSONObject(x), s)
        except JSONException as e:
            return None

    #  Main function to generate canonical strings for JSON objects 
    @classmethod
    @getCanonicalForm.register(object, JSONObject, cls.CanonicalizationStrategy)
    def getCanonicalForm_0(cls, x, s):
        """ generated source for method getCanonicalForm_0 """
        if s == cls.CanonicalizationStrategy.SIMPLE:
            return renderSimpleCanonicalJSON(x)
        else:
            raise RuntimeException("Canonicalization strategy not recognized.")

    #  This should be identical to the standard code to render the JSON object,
    #      * except it forces the keys for maps to be listed in sorted order. 
    @classmethod
    def renderSimpleCanonicalJSON(cls, x):
        """ generated source for method renderSimpleCanonicalJSON """
        try:
            if isinstance(x, (JSONObject, )):
                #  Sort the keys
                while i.hasNext():
                while keys.hasNext():
                    if 1 > len(sb):
                        sb.append(',')
                    sb.append(JSONObject.quote(o.__str__()))
                    sb.append(':')
                    sb.append(cls.renderSimpleCanonicalJSON(theObject.get(o.__str__())))
                sb.append('}')
                return sb.__str__()
            elif isinstance(x, (JSONArray, )):
                sb.append("[")
                while i < len:
                    if i > 0:
                        sb.append(",")
                    sb.append(cls.renderSimpleCanonicalJSON(theArray.get(i)))
                    i += 1
                sb.append("]")
                return sb.__str__()
            else:
                if x == None or x == None:
                    return "null"
                if isinstance(x, (JSONString, )):
                    try:
                        object_ = (x).toJSONString()
                    except Exception as e:
                        raise JSONException(e)
                    if isinstance(object_, (str, )):
                        return str(object_)
                    raise JSONException("Bad value from toJSONString: " + object_)
                if isinstance(x, (Number, )):
                    return JSONObject.numberToString(x)
                if isinstance(x, (bool, )) or isinstance(x, (JSONObject, )) or isinstance(x, (JSONArray, )):
                    return x.__str__()
                if isinstance(x, (Map, )):
                    return cls.renderSimpleCanonicalJSON(JSONObject(x)).__str__()
                if isinstance(x, (Collection, )):
                    return cls.renderSimpleCanonicalJSON(JSONArray(x)).__str__()
                if x.__class__.isArray():
                    return cls.renderSimpleCanonicalJSON(JSONArray(x)).__str__()
                return JSONObject.quote(x.__str__())
        except Exception as e:
            return None

