from scripts.resources import Properties

# NIFI Registry commands

def getListBucketsCommand(registryURL, bucketName):
    return Properties.NIFI_REGISTRY_COMMAND_PREFIX + " list-buckets -u " + registryURL + " | grep " + bucketName + " | awk '{print $3}'"

def getListFlowsCommand(registryURL, bucketId, flowName):
    return Properties.NIFI_REGISTRY_COMMAND_PREFIX + " list-flows -u " + registryURL + " -b " + bucketId + " | grep " + flowName + " | awk '{print $3}'"

def getListFlowVersionsCommand(registryURL, flowId):
    return Properties.NIFI_REGISTRY_COMMAND_PREFIX + " list-flow-versions -u " + registryURL + " -f " + flowId

def getExportFlowVersionCommand(registryURL, flowId, version, exportToFilePathName):
    return Properties.NIFI_REGISTRY_COMMAND_PREFIX + " export-flow-version -u " + registryURL + " -f " + flowId + " -fv " + version + " -o " + exportToFilePathName

def getImportFlowVersionCommand(registryURL, flowId, importToFilePathName):
    return Properties.NIFI_REGISTRY_COMMAND_PREFIX + " import-flow-version -u " + registryURL + " -f " + flowId + " -i " + importToFilePathName

def getListFlowVersionCommand(registryURL, flowId, version):
    return Properties.NIFI_REGISTRY_COMMAND_PREFIX + " list-flow-versions -u " + registryURL + " -f " + flowId + " | awk '{print $1}' "