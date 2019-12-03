import scripts.resources.Properties as Properties
from scripts.application import NifiRegistryApplication
from scripts.repository import NifiRegistryRepository
import logging
import sys
from scripts.resources import Messages
from scripts.infrastructure import AttributesUtils as attributesUtils

def execute(registryUrl, bucketName, flowName):
    logging.info(Messages.FLOW_CREATION_START)

    if not attributesUtils.isValueValid(registryUrl) or not attributesUtils.isValueValid(bucketName) or not attributesUtils.isValueValid(flowName):
        logging.error(Messages.FLOW_CREATION_PARAMETERS_INVALID_EXCEPTION(registryUrl, bucketName, flowName))
    else:
        bucketIdCallStatus, bucketId = NifiRegistryRepository.getBucketId(registryUrl, bucketName)
        if NifiRegistryApplication.doesItExist(bucketIdCallStatus, bucketId):
            NifiRegistryApplication.createFlow(registryUrl, bucketId, flowName, bucketName)
    logging.info(Messages.FLOW_CREATION_FINISH)


if __name__ == "__main__":

    logging.basicConfig(level=Properties.LOGGING_LEVEL, format=Properties.LOGGING_FORMAT, datefmt=Properties.LOGGING_DATE_FORMAT)

    if len(sys.argv) == 4:
        execute(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        logging.error("Invalid arguments. Correct usage is: CreateBucket.py ${registryUrl} ${bucketName} ${flowName}")
        exit(1)
