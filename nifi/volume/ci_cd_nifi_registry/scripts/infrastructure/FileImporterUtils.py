import csv

import logging

from scripts.infrastructure import AttributesUtils as attributesUtils

from scripts.resources import Properties as properties

def validateAndLoadFile(environment, csvFile):
    listOfRows = []

    fileName = properties.CONFIG_FOLDER + "/" + environment + "/" + csvFile

    try:
        with open(fileName, 'rb') as csvfile:
            spamreader = csv.DictReader(csvfile, delimiter=',')

            for row in spamreader:

                # Verify if file is consistent

                fieldNameAndValidationList = {
                        "registryUrlFrom": isRegistryUrlFromInvalidIfPresent,
                        "bucketNameFrom": isBucketNameFromInvalidIfPresent,
                        "flowNameFrom": isFlowNameFromInvalidIfPresent,
                        "registryUrlTo": isRegistryUrlToInvalidIfPresent,
                        "bucketNameTo": isBucketNameToInvalidIfPresent,
                        "flowNameTo": isFlowNameToInvalidIfPresent,
                        "version": isVersionInvalidIfPresent
                }

                isThereInvalidFields = False
                for eachFieldName in fieldNameAndValidationList.keys():
                    isThereInvalidFields = isThereInvalidFieldsFinalResult(isThereInvalidFields, row, eachFieldName, isFieldInvalid, fieldNameAndValidationList.get(eachFieldName))


                if isThereInvalidFields:
                    logging.error('status=fail, message="File ' + fileName + ' is inconsistent. Verify all parameters."')
                    raise BaseException

                listOfRows.append(row)

        return listOfRows

    except (BaseException), e:
        logging.error('status=fail, message="' + fileName + ' not found or is invalid"')
        logging.error(e)
        exit(1)


def isRegistryUrlFromInvalidIfPresent(row):
    return attributesUtils.isValueNotPresent(row["registryUrlFrom"]) or attributesUtils.verifyIfValueIsInvalid(row["registryUrlFrom"]) or attributesUtils.isThereAnySpace(row["registryUrlFrom"])

def isBucketNameFromInvalidIfPresent(row):
    return attributesUtils.isValueNotPresent(row["bucketNameFrom"]) or attributesUtils.verifyIfValueIsInvalid(row["bucketNameFrom"]) or attributesUtils.isThereAnySpace(row["bucketNameFrom"])

def isFlowNameFromInvalidIfPresent(row):
    return attributesUtils.isValueNotPresent(row["flowNameFrom"]) or attributesUtils.verifyIfValueIsInvalid(row["flowNameFrom"]) or attributesUtils.isThereAnySpace(row["flowNameFrom"])

def isRegistryUrlToInvalidIfPresent(row):
    return attributesUtils.isValueNotPresent(row["registryUrlTo"]) or attributesUtils.verifyIfValueIsInvalid(row["registryUrlTo"]) or attributesUtils.isThereAnySpace(row["registryUrlTo"])

def isBucketNameToInvalidIfPresent(row):
    return attributesUtils.isValueNotPresent(row["bucketNameTo"]) or attributesUtils.verifyIfValueIsInvalid(row["bucketNameTo"]) or attributesUtils.isThereAnySpace(row["bucketNameTo"])

def isFlowNameToInvalidIfPresent(row):
    return attributesUtils.isValueNotPresent(row["flowNameTo"]) or attributesUtils.verifyIfValueIsInvalid(row["flowNameTo"]) or attributesUtils.isThereAnySpace(row["flowNameTo"])

def isVersionInvalidIfPresent(row):
    return attributesUtils.isValueNotPresent(row["version"]) or attributesUtils.isThereAnySpace(row["version"])


def isFieldInvalid(row, fieldName, validation):
    if row.has_key(fieldName):
        if validation(row):
            logging.error('status=fail, message="' + fieldName + ' field is invalid"')
            return True
    return False


def isThereInvalidFieldsFinalResult(value, row, fieldName, validationWrapper, validation):
    if not value:
        value = validationWrapper(row, fieldName, validation)
    else:
        validationWrapper(row, fieldName, validation)

    return value