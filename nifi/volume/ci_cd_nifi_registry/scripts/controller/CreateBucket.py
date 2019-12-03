import scripts.resources.Properties as Properties
from scripts.application import NifiRegistryApplication
import logging
import sys
from scripts.resources import Messages
from scripts.infrastructure import AttributesUtils as attributesUtils

def execute(registryUrl, bucketName):
    logging.info(Messages.BUCKET_CREATION_START)

    if not attributesUtils.isValueValid(registryUrl) or not attributesUtils.isValueValid(bucketName):
        logging.error(Messages.BUCKET_CREATION_PARAMETERS_INVALID_EXCEPTION(registryUrl, bucketName))
    else:
        NifiRegistryApplication.createBucket(registryUrl, bucketName)
    logging.info(Messages.BUCKET_CREATION_FINISH)


if __name__ == "__main__":

    logging.basicConfig(level=Properties.LOGGING_LEVEL, format=Properties.LOGGING_FORMAT, datefmt=Properties.LOGGING_DATE_FORMAT)

    if len(sys.argv) == 3:
        execute(sys.argv[1], sys.argv[2])
    else:
        logging.error("Invalid arguments. Correct usage is: CreateBucket.py ${registryUrl} ${bucketName}")
        exit(1)
