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
                        "registryUrlTo": isRegistryUrlToInvalidIfPresent,
                        "bucketName": isBucketNameInvalidIfPresent,
                        "flowName": isFlowNameInvalidIfPresent,
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

def isRegistryUrlToInvalidIfPresent(row):
    return attributesUtils.isValueNotPresent(row["registryUrlTo"]) or attributesUtils.verifyIfValueIsInvalid(row["registryUrlTo"]) or attributesUtils.isThereAnySpace(row["registryUrlTo"])

def isBucketNameInvalidIfPresent(row):
    return attributesUtils.isValueNotPresent(row["bucketName"]) or attributesUtils.verifyIfValueIsInvalid(row["bucketName"]) or attributesUtils.isThereAnySpace(row["bucketName"])

def isFlowNameInvalidIfPresent(row):
    return attributesUtils.isValueNotPresent(row["flowName"]) or attributesUtils.verifyIfValueIsInvalid(row["flowName"]) or attributesUtils.isThereAnySpace(row["flowName"])

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