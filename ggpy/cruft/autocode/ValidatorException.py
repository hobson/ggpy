#!/usr/bin/env python
""" generated source for module ValidatorException """
# package: org.ggp.base.validator
@SuppressWarnings("serial")
class ValidatorException(Exception):
    """ generated source for class ValidatorException """
    @overloaded
    def __init__(self, explanation):
        """ generated source for method __init__ """
        super(ValidatorException, self).__init__("Validator: " + explanation)

    @__init__.register(object, str, Throwable)
    def __init___0(self, explanation, t):
        """ generated source for method __init___0 """
        super(ValidatorException, self).__init__(t)

