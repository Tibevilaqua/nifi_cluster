import scripts.resources.Properties as Properties

from scripts.infrastructure import FileImporterUtils as fileImporterUtils
from scripts.resources import Properties as properties
from scripts.application import NifiRegistryApplication
import logging
import sys
from scripts.resources import Messages

def execute(environment):
    logging.info(Messages.PROMOTE_VERSION_START)
    for eachConfig in fileImporterUtils.validateAndLoadFile(environment, properties.REGISTRY_DEPLOYMENT_CONTROLLER):
        validationStatusResult, validationTextResult = NifiRegistryApplication.validateIntegrationConsistency(eachConfig.get(properties.RDC_registryUrlFrom), eachConfig.get(properties.RDC_bucketNameFrom), eachConfig.get(properties.RDC_flowNameFrom), eachConfig.get(properties.RDC_registryUrlTo), eachConfig.get(properties.RDC_bucketNameTo), eachConfig.get(properties.RDC_flowNameTo), str(eachConfig.get(properties.RDC_registryVersion)))

        if validationStatusResult == 0:
            NifiRegistryApplication.promoteVersionToFlowInBucket(eachConfig.get(properties.RDC_registryUrlFrom), eachConfig.get(properties.RDC_bucketNameFrom), eachConfig.get(properties.RDC_flowNameFrom), eachConfig.get(properties.RDC_registryUrlTo), eachConfig.get(properties.RDC_bucketNameTo), eachConfig.get(properties.RDC_flowNameTo), str(eachConfig.get(properties.RDC_registryVersion)))
        else:
            logging.info(validationTextResult)

    logging.info(Messages.PROMOTE_VERSION_FINISH)

if __name__ == "__main__":
    logging.basicConfig(level=Properties.LOGGING_LEVEL, format=Properties.LOGGING_FORMAT, datefmt=Properties.LOGGING_DATE_FORMAT)

    if len(sys.argv) == 2:
        execute(sys.argv[1])
    else:
        logging.error("Invalid arguments. Correct usage is: PromoteVersionController.py ${environment}")
        exit(1)
