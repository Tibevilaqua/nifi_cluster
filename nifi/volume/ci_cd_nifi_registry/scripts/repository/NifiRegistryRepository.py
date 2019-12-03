import commands
import logging
from scripts.infrastructure import CommandsUtils

def getBucketId(registryURL, bucketName):
    command = CommandsUtils.getListBucketsCommand(registryURL, bucketName)
    return executeCommand(command)

def getFlowId(registryURL, bucketId, flowName):
    command = CommandsUtils.getListFlowsCommand(registryURL, bucketId, flowName)
    return executeCommand(command)

def exportFlowVersion(registryURL, flowId, version, exportToFilePathName):
    command = CommandsUtils.getExportFlowVersionCommand(registryURL, flowId, version, exportToFilePathName)
    return executeCommand(command)

def importFlowVersion(registryURL, flowId, exportToFilePathName):
    command = CommandsUtils.getImportFlowVersionCommand(registryURL, flowId, exportToFilePathName)
    return executeCommand(command)

def listFlowVersion(registryURL, flowId, version):
    command = CommandsUtils.getListFlowVersionCommand(registryURL, flowId, version)
    return executeCommand(command, version)

def createBucket(registryURL, bucketName):
    command = CommandsUtils.getCreateBucketCommand(registryURL, bucketName)
    return executeCommand(command)

def createFlow(registryURL, bucketId, flowName):
    command = CommandsUtils.getCreateFlowCommand(registryURL, bucketId, flowName)
    return executeCommand(command)

def doesInstanceExist(registryURL):
    command = CommandsUtils.getDoesInstanceExistCommand(registryURL)
    status, text = executeCommand(command)
    return True if status == 0 else False

def executeCommand(command, filter=False):

    logging.debug("Command being executed: " + command)

    status, text = commands.getstatusoutput(command)

    # This if will never occur because the "| grep and | awk" commands after the API call will always return "0" even though the first API fails.
    # These pipes were added for formatting in the interest of time and should be replaced later with a parsing utils class created in this project. In
    # this way, we'll be able to have non 0 responses.
    if (status != 0):
        logging.error("Error while trying to execute command: " + command)
        logging.error(text)
        logging.error(status)
        return 1, "Error while trying to execute command: " + command

    if filter:
        index = text.find(filter)
        text = "" if index < 0 else text[index:index+len(filter)]

    # Workaround so that the above layers of the project can rely on the status rather than the text itself. This can be removed once the aforementioned is implemented.
    if len(text) == 0:
        return 1, text

    return status, text