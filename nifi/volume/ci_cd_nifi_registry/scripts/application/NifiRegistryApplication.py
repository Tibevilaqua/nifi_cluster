from scripts.repository import NifiRegistryRepository
from scripts.resources import Properties
from scripts.repository import OSRepository
from scripts.infrastructure import MessageloggingUtils
from scripts.resources import Messages
import logging

def promoteVersionToFlowInBucket(registryUrlFrom, registryUrlTo, bucketName, flowName, version):

    try:
        OSRepository.createDir(Properties.TEMP_FOLDER_TO_BE_CREATED_DURING_EXECUTION)

        # Get BucketId and FlowId from the origin NIFI registry
        bucketIdFromCallStatus, flowIdFromCallStatus,  bucketId, flowId = getFlowIdAndBucketId(registryUrlFrom, bucketName, flowName)

        NifiRegistryRepository.exportFlowVersion(registryUrlFrom, flowId, version, Properties.TEMP_FOLDER_AND_FLOW_FILE_TO_BE_CREATED_DURING_EXECUTION)

        # Get BucketId and FlowId from the destination NIFI registry
        bucketIdToCallStatus, flowIdToCallStatus, bucketId, flowId = getFlowIdAndBucketId(registryUrlTo, bucketName, flowName)

        # CreateBucket if it does not yet exist at the destination
        if not doesItExist(bucketIdToCallStatus, bucketId):
            bucketIdToCallStatus, bucketId = createBucket(registryUrlTo, bucketName, False)

        # CreateFlow if it does not yet exist at the destination
        if not doesItExist(flowIdToCallStatus, flowId) and bucketId:
            flowIdFromCallStatus, flowId = createFlow(registryUrlTo, bucketId, flowName, bucketName, False)

        NifiRegistryRepository.importFlowVersion(registryUrlTo, flowId, Properties.TEMP_FOLDER_AND_FLOW_FILE_TO_BE_CREATED_DURING_EXECUTION)

        logging.info(Messages.PROMOTION_EXECUTED_SUCCESSFULLY(registryUrlTo, bucketName, flowName, version))
    finally:
        OSRepository.deleteDir(Properties.TEMP_FOLDER_TO_BE_CREATED_DURING_EXECUTION)


def createBucket(registryURL, bucketName, shouldVerifyIfBucketExists=True):
    bucketIdCallStatus = None
    bucketId = None

    if shouldVerifyIfBucketExists:
        bucketIdCallStatus, bucketId = NifiRegistryRepository.getBucketId(registryURL, bucketName)

    # If Bucket does not exist
    if not shouldVerifyIfBucketExists or not bucketId and len(bucketId) == 0:
        bucketIdCallStatus, bucketId = NifiRegistryRepository.createBucket(registryURL, bucketName)
        MessageloggingUtils.logInfoIfZero(bucketIdCallStatus, Messages.BUCKET_CREATED(registryURL, bucketName))
    else:
        logging.info(Messages.BUCKET_ALREADY_EXISTS(registryURL, bucketName))

    return bucketIdCallStatus, bucketId


def createFlow(registryUrl, bucketId, flowName, bucketName, shouldVerifyIfFlowExists=True):
    flowIdCallStatus = None
    flowId = None

    if shouldVerifyIfFlowExists:
        flowIdCallStatus, flowId = NifiRegistryRepository.getFlowId(registryUrl, bucketId, flowName)

    # If Flow does not exist
    if not shouldVerifyIfFlowExists or not flowId and len(flowId) == 0:
        flowIdCallStatus, flowId = NifiRegistryRepository.createFlow(registryUrl, bucketId, flowName)
        MessageloggingUtils.logInfoIfZero(flowIdCallStatus, Messages.FLOW_CREATED(registryUrl, bucketName, flowName))
    else:
        logging.info(Messages.FLOW_ALREADY_EXISTS(registryUrl, bucketName, flowName))

    return flowIdCallStatus, flowId

def validateIntegrationConsistency(registryUrlFrom, registryUrlTo, bucketName, flowName, version):

    if not NifiRegistryRepository.doesInstanceExist(registryUrlFrom):
        logging.info(Messages.REGISTRY_DOES_NOT_EXISTS(registryUrlFrom))
        return 1, Messages.SKIPPING_LINE(registryUrlFrom, registryUrlTo, bucketName, flowName, version)
    if not NifiRegistryRepository.doesInstanceExist(registryUrlTo):
        logging.info(Messages.REGISTRY_DOES_NOT_EXISTS(registryUrlTo))
        return 1, Messages.SKIPPING_LINE(registryUrlFrom, registryUrlTo, bucketName, flowName, version)

    # Get BucketId and FlowId from the origin NIFI registry
    bucketIdFromCallStatus, flowIdFromCallStatus, bucketIdFrom, flowIdFrom = getFlowIdAndBucketId(registryUrlFrom, bucketName, flowName)

    # Get BucketId and FlowId from the destination NIFI registry
    bucketIdToCallStatus, flowIdToCallStatus, bucketIdTo, flowIdTo = getFlowIdAndBucketId(registryUrlTo, bucketName,flowName)

    versionStatusFrom, versionTextFrom = NifiRegistryRepository.listFlowVersion(registryUrlFrom, flowIdFrom, version)

    # Validating if any of the values do not exist on the origin nifi registry
    if bucketIdFromCallStatus != 0 or flowIdFromCallStatus != 0 or versionStatusFrom != 0:
        MessageloggingUtils.logInfoIfNotZero(bucketIdFromCallStatus, Messages.BUCKET_NOT_FOUND(bucketName, registryUrlFrom))
        MessageloggingUtils.logInfoIfNotZero(flowIdFromCallStatus, Messages.FLOW_NOT_FOUND(flowName, registryUrlFrom))
        MessageloggingUtils.logInfoIfNotZero(versionStatusFrom, Messages.VERSION_NOT_FOUND(registryUrlFrom, bucketName, flowName, version))
        return 1, Messages.SKIPPING_LINE(registryUrlFrom, registryUrlTo, bucketName, flowName, version)

    # Validating if the version already exists in the destination nifi registry
    if bucketIdToCallStatus == 0 or flowIdToCallStatus == 0:
        versionStatusTo, versionTextTo = NifiRegistryRepository.listFlowVersion(registryUrlTo, flowIdTo, version)


        if versionStatusTo == 0 and versionTextTo == version:
            logging.info(Messages.VERSION_ALREADY_EXISTS_AT_DESTINATION_NIFI_REGISTRY(registryUrlTo, bucketName, flowName,version))
            return 1, Messages.SKIPPING_LINE(registryUrlFrom, registryUrlTo, bucketName, flowName, version)


    return 0, Messages.VALIDATION_SUCCESSFUL

def getFlowIdAndBucketId(registryURL,  bucketName, flowName):
    bucketIdCallStatus, bucketId = NifiRegistryRepository.getBucketId(registryURL, bucketName)
    flowIdCallStatus, flowId = NifiRegistryRepository.getFlowId(registryURL, bucketId, flowName)
    return bucketIdCallStatus, flowIdCallStatus, bucketId, flowId

def doesItExist(returnedStatus, returnedText):
    return True if returnedStatus == 0 or len(returnedText) > 0 else False