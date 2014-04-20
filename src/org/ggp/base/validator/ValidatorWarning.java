package org.ggp.base.validator;

class ValidatorWarning(object):
    warningMessage = ''

    def ValidatorWarning(warningMessage=''):
        this.warningMessage = warningMessage;

    def toString():  # String
        return warningMessage;
