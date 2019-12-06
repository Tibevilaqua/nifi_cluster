# Lambdas
BUCKET_NOT_FOUND = lambda bucketName, nifiRegistryURL : "Bucket {} not found in the {} Nifi Registry instance or the Nifi Registry URL is wrong.".format(bucketName, nifiRegistryURL)
FLOW_NOT_FOUND = lambda flowName, nifiRegistryURL : "Flow {} not found in the {} Nifi Registry instance or the Nifi Registry URL is wrong.".format(flowName, nifiRegistryURL)
SKIPPING_LINE = lambda registryUrlFrom, bucketNameFrom, flowNameFrom, registryUrlTo, bucketNameTo, flowNameTo, version : "Skipping line {},{},{},{},{},{},{}".format(registryUrlFrom, bucketNameFrom, flowNameFrom, registryUrlTo, bucketNameTo, flowNameTo, version)
VERSION_NOT_FOUND = lambda registryUrl, bucketName, flowName, version : "Version {} not found in registry {}, Bucket {}, Flow {}".format(version, registryUrl, bucketName, flowName)
VERSION_ALREADY_EXISTS_AT_DESTINATION_NIFI_REGISTRY = lambda registryUrl, bucketName, flowName, version : "Version {} already exists in registry {}, Bucket {}, Flow {}".format(version, registryUrl, bucketName, flowName)
PROMOTION_EXECUTED_SUCCESSFULLY = lambda registryUrl, bucketName, flowName, version : "Version {} has been promoted successfully to the registry {}, Bucket {}, Flow {}".format(version, registryUrl, bucketName, flowName)
BUCKET_CREATION_PARAMETERS_INVALID_EXCEPTION  = lambda registryUrl, bucketName : "The parameters registryURL {} or bucketName {} are invalid".format(registryUrl, bucketName)
FLOW_CREATION_PARAMETERS_INVALID_EXCEPTION  = lambda registryUrl, bucketName, flowName : "The parameters registryURL {} or bucketName {} or the flowName {} are invalid".format(registryUrl, bucketName, flowName)
BUCKET_CREATED = lambda registryUrl, bucketName : "The Bucket {} has been created at the registry {}".format(bucketName, registryUrl)
BUCKET_ALREADY_EXISTS = lambda registryUrl, bucketName : "The Bucket {} already exists at the Registry {}".format(registryUrl, bucketName)
FLOW_CREATED = lambda registryUrl, bucketName, flowName : "The Flow {} has been created in the Bucket {} at the Registry {}".format(flowName, bucketName, registryUrl)
FLOW_ALREADY_EXISTS = lambda registryUrl, bucketName, flowName : "The Flow {} already exists in the Bucket {} at the Registry {}".format(registryUrl, bucketName, flowName)
REGISTRY_DOES_NOT_EXISTS = lambda registryUrl : "The Registry instance {} could not be found".format(registryUrl)


PROMOTE_VERSION_START = "Starting version promotion process"
PROMOTE_VERSION_FINISH = "Finishing version promotion process"

BUCKET_CREATION_START = "Starting bucket creation process"
BUCKET_CREATION_FINISH = "Finishing bucket creation process"

FLOW_CREATION_START = "Starting flow creation process"
FLOW_CREATION_FINISH = "Finishing flow creation process"

# Constants
VALIDATION_SUCCESSFUL = "Validation successful"
