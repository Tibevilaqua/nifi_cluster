import re
import logging

def isValueNotPresent(value):
    return True if value == "None" or value == "" or value is None else False

def isThereALetterInTheValue(value):
    for match in re.findall(r"([a-zA-Z])", value):
        return True
    return False


def isValueValid(value):
    """
    A valid value is considered to be at least 2 characters long and must have a letter in it.
    i.e:
    12 = invalid
    1a = valid
    / = invalid
    /a = valid
    :param value: Value to be evaluated
    :return: if value is valid or not
    """
    return True if not isValueNotPresent(value) and not len(value) < 2 and isThereALetterInTheValue(value) else False


def verifyIfValueIsInvalid(value):
    if not isValueValid(value):
        return True
    return False

def verifyIfValueIsInvalidIfNotEmpty(value):
    """
        If value present (not empty), validate its validity
        :param value:
        :return: True if present and valid or if not present. False if present and invalid
        """
    if value:
        if not isValueValid(value):
            return True

    return False

def isThereAnySpace(value):
    if " " in value:
        logging.error("You have an invalid space in the value: \'%s\'", value)
        return True
    return False

def isThereSpacesAtTheBeginningOrAtTheEnd(value):
    """
    :return: True if there's a space at the beginning or at the end of the value. False otherwise
    """
    return value.strip() != value


def getBoolean(value):
    """
    :return: True or False depending on the value of the String.
    """
    if str(value).lower() == "true":
        return True
    else:
        return False

# def isVersionFormatInvalid(value):
#     """
#     :return:  True if at the very least the format [0-9]+\.[0-9]+\.[0-9]+ is true
#     """
#     for _ in re.findall("([0-9]+\.[0-9]+\.[0-9]+)|(" + Config.APPS_VERSION_WILDCARD + ")", value):
#         return False
#     return True