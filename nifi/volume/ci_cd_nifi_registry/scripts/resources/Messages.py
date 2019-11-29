# Lambdas
BUCKET_NOT_FOUND = lambda bucketName, nifiRegistryURL : "Bucket {} not found in the {} Nifi Registry instance or the Nifi Registry URL is wrong.".format(bucketName, nifiRegistryURL)
FLOW_NOT_FOUND = lambda flowName, nifiRegistryURL : "Flow {} not found in the {} Nifi Registry instance or the Nifi Registry URL is wrong.".format(flowName, nifiRegistryURL)
SKIPPING_LINE = lambda registryUrlFrom, registryUrlTo, bucketName, flowName, version : "Skipping line {},{},{},{},{}".format(registryUrlFrom, registryUrlTo, bucketName, flowName, version)
VERSION_NOT_FOUND = lambda registryUrl, bucketName, flowName, version : "Version {} not found in registry {}, bucket {}, flow {}".format(version, registryUrl, bucketName, flowName)
VERSION_ALREADY_EXISTS_AT_DESTINATION_NIFI_REGISTRY = lambda registryUrl, bucketName, flowName, version : "Version {} already exists in registry {}, bucket {}, flow {}".format(version, registryUrl, bucketName, flowName)
PROMOTION_EXECUTED_SUCCESSFULLY = lambda registryUrl, bucketName, flowName, version : "Version {} has been promoted successfully to the registry {}, bucket {}, flow {}".format(version, registryUrl, bucketName, flowName)

PROMOTE_VERSION_START = "Starting version promotion process"
PROMOTE_VERSION_FINISH = "Finishing version promotion process"

# Constants
VALIDATION_SUCCESSFUL = "Validation successful"
