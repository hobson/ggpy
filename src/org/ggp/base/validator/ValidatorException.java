package org.ggp.base.validator

class ValidatorException(Exception):
    def __init__(self, String explanation):
        super("Validator: " + explanation)

    def ValidatorException(explanation='', Throwable t):
        super("Validator: " + explanation, t)
