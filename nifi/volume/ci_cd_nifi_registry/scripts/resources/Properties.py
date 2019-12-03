import logging

# Application variables
CONFIG_FOLDER = "config"
NIFI_REGISTRY_COMMAND_PREFIX = "/Users/tiagobevilaqua/opt/anz/aca/nifi-toolkit-1.10.0/bin/cli.sh registry"

TEMP_FOLDER_TO_BE_CREATED_DURING_EXECUTION = "temp"
TEMPORARY_FLOW_FILE_OUTPUT_NAME = "flow_temp.json"
TEMP_FOLDER_AND_FLOW_FILE_TO_BE_CREATED_DURING_EXECUTION = TEMP_FOLDER_TO_BE_CREATED_DURING_EXECUTION + "/" + TEMPORARY_FLOW_FILE_OUTPUT_NAME

# Registry Deployment Controllet Model (Object)
REGISTRY_DEPLOYMENT_CONTROLLER = "registry_deployment_controller.csv"
RDC_registryUrlFrom = "registryUrlFrom"
RDC_registryUrlTo = "registryUrlTo"
RDC_bucketName = "bucketName"
RDC_flowName = "flowName"
RDC_registryVersion = "version"


#Logging
LOGGING_LEVEL = logging.DEBUG
LOGGING_FORMAT = "%(levelname)s - %(asctime)s - %(message)s"
LOGGING_DATE_FORMAT = "%H:%M:%S"