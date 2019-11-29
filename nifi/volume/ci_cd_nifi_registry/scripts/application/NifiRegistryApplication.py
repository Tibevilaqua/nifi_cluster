from scripts.repository import NifiRegistryRepository
from scripts.resources import Properties
from scripts.repository import OSRepository
from scripts.infrastructure import ErrorMessageloggingUtils
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

        NifiRegistryRepository.importFlowVersion(registryUrlTo, flowId, Properties.TEMP_FOLDER_AND_FLOW_FILE_TO_BE_CREATED_DURING_EXECUTION)

        logging.info(Messages.PROMOTION_EXECUTED_SUCCESSFULLY(registryUrlTo, bucketName, flowName, version))
    finally:
        OSRepository.deleteDir(Properties.TEMP_FOLDER_TO_BE_CREATED_DURING_EXECUTION)

def validateIntegrationConsistency(registryUrlFrom, registryUrlTo, bucketName, flowName, version):

    # Get BucketId and FlowId from the origin NIFI registry
    bucketIdFromCallStatus, flowIdFromCallStatus, bucketIdFrom, flowIdFrom = getFlowIdAndBucketId(registryUrlFrom, bucketName, flowName)

    # Get BucketId and FlowId from the destination NIFI registry
    bucketIdToCallStatus, flowIdToCallStatus, bucketIdTo, flowIdTo = getFlowIdAndBucketId(registryUrlTo, bucketName,flowName)

    versionStatusFrom, versionTextFrom = NifiRegistryRepository.listFlowVersion(registryUrlFrom, flowIdFrom, version)


    # Validating if any of the values do not exist on the origin nifi registry
    if bucketIdFromCallStatus != 0 or flowIdFromCallStatus != 0 or bucketIdToCallStatus != 0 or flowIdToCallStatus != 0 or versionStatusFrom != 0:
        ErrorMessageloggingUtils.logErrorIfNotZero(bucketIdFromCallStatus, Messages.BUCKET_NOT_FOUND(bucketName, registryUrlFrom))
        ErrorMessageloggingUtils.logErrorIfNotZero(flowIdFromCallStatus, Messages.BUCKET_NOT_FOUND(flowName, registryUrlFrom))
        ErrorMessageloggingUtils.logErrorIfNotZero(bucketIdToCallStatus, Messages.BUCKET_NOT_FOUND(bucketName, registryUrlTo))
        ErrorMessageloggingUtils.logErrorIfNotZero(flowIdToCallStatus, Messages.BUCKET_NOT_FOUND(flowName, registryUrlTo))
        ErrorMessageloggingUtils.logErrorIfNotZero(versionStatusFrom, Messages.VERSION_NOT_FOUND(registryUrlFrom, bucketName, flowName, version))
        return 1, Messages.SKIPPING_LINE(registryUrlFrom, registryUrlTo, bucketName, flowName, version)


    versionStatusTo, versionTextTo = NifiRegistryRepository.listFlowVersion(registryUrlTo, flowIdTo, version)

    # Validating if the version already exists in the destination nifi registry
    if versionStatusTo == 0 and versionTextTo == version:
        logging.error(Messages.VERSION_ALREADY_EXISTS_AT_DESTINATION_NIFI_REGISTRY(registryUrlTo, bucketName, flowName,version))
        return 1, Messages.SKIPPING_LINE(registryUrlFrom, registryUrlTo, bucketName, flowName, version)


    return 0, Messages.VALIDATION_SUCCESSFUL

def getFlowIdAndBucketId(registryURL,  bucketName, flowName):
    bucketIdCallStatus, bucketId = NifiRegistryRepository.getBucketId(registryURL, bucketName)
    flowIdCallStatus, flowId = NifiRegistryRepository.getFlowId(registryURL, bucketId, flowName)
    return bucketIdCallStatus, flowIdCallStatus, bucketId, flowId
