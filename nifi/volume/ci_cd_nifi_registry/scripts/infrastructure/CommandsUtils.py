from scripts.resources import Properties

# NIFI Registry commands

IGNORE_JAVA_HOME = " | grep -vi JAVA_HOME "

def getListBucketsCommand(registryURL, bucketName):
    return Properties.NIFI_REGISTRY_COMMAND_PREFIX + " list-buckets -u " + registryURL + IGNORE_JAVA_HOME+ " | grep -w " + bucketName + " | awk '{print $3}'"

def getListFlowsCommand(registryURL, bucketId, flowName):
    return Properties.NIFI_REGISTRY_COMMAND_PREFIX + " list-flows -u " + registryURL + " -b " + bucketId + IGNORE_JAVA_HOME + " | grep -w " + flowName + " | awk '{print $3}' "

def getListFlowVersionsCommand(registryURL, flowId):
    return Properties.NIFI_REGISTRY_COMMAND_PREFIX + " list-flow-versions -u " + registryURL + " -f " + flowId + IGNORE_JAVA_HOME

def getExportFlowVersionCommand(registryURL, flowId, version, exportToFilePathName):
    return Properties.NIFI_REGISTRY_COMMAND_PREFIX + " export-flow-version -u " + registryURL + " -f " + flowId + " -fv " + version + " -o " + exportToFilePathName

def getImportFlowVersionCommand(registryURL, flowId, importToFilePathName):
    return Properties.NIFI_REGISTRY_COMMAND_PREFIX + " import-flow-version -u " + registryURL + " -f " + flowId + " -i " + importToFilePathName

def getListFlowVersionCommand(registryURL, flowId):
    return Properties.NIFI_REGISTRY_COMMAND_PREFIX + " list-flow-versions -u " + registryURL + " -f " + flowId + IGNORE_JAVA_HOME + " | awk '{print $1}' "

def getCreateBucketCommand(registryURL, bucketName):
    # cli.sh registry create-bucket -u http://nifi_registry:18080 -bn test123
    return Properties.NIFI_REGISTRY_COMMAND_PREFIX + " create-bucket -u " + registryURL + " -bn " + bucketName + IGNORE_JAVA_HOME

def getCreateFlowCommand(registryURL, bucketId, flowName):
    # cli.sh registry create-flow -b bee62f19-a3d5-4b2a-839d-a8fb692208d0 -u http://nifi_registry:18080 -fn ccc
    return Properties.NIFI_REGISTRY_COMMAND_PREFIX + " create-flow -u " + registryURL + " -b " + bucketId + " -fn " + flowName + IGNORE_JAVA_HOME

def getDoesInstanceExistCommand(registryURL):
    # cli.sh registry list-buckets -u http://localhost:18080
    return Properties.NIFI_REGISTRY_COMMAND_PREFIX + " list-buckets -u " + registryURL + IGNORE_JAVA_HOME
