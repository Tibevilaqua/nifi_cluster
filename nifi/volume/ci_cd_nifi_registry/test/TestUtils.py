import os
import shutil

def createAndWriteToFile(path, content):
    file1 = open(path, "a")
    file1.write(content)
    file1.close()


def readFile(path):
    file1 = open(path, "r")
    return file1.read()


def createSetUpStructure(swapTestDir, testTarGzPath=None):
    # Set-up
    if os.path.isdir(swapTestDir):
        shutil.rmtree(swapTestDir)

    if testTarGzPath:
        if os.path.isfile(testTarGzPath):
            os.remove(testTarGzPath)

    os.mkdir(swapTestDir)
    os.mkdir(swapTestDir + "/.git")
    createAndWriteToFile(swapTestDir + "/.git/config", "url=123")
    os.mkdir(swapTestDir + "/swap_dev")
    os.mkdir(swapTestDir + "/swap_qa")

    createAndWriteToFile(swapTestDir + "/properties.Config", "[APPLICATION]\nVERSION=1.0.0\nARTIFACTORY_DEPLOYMENT_FOLDER=splunk-connect\nTYPE=TAR")

    os.mkdir(swapTestDir + "/swap_prod_pull")
    os.mkdir(swapTestDir + "/swap_prod_pull/differentDir")

    os.mkdir(swapTestDir + "/swap_prod_push")
    os.mkdir(swapTestDir + "/swap_prod_push/anotherdir")
    os.mkdir(swapTestDir + "/swap_prod_push/anotherdir/andAnotherMore")

    createAndWriteToFile(swapTestDir + "/swap_dev/properties", "dev")
    createAndWriteToFile(swapTestDir + "/swap_qa/properties", "qa")
    createAndWriteToFile(swapTestDir + "/swap_prod_pull/differentDir/properties", "prodPull1")
    createAndWriteToFile(swapTestDir + "/swap_prod_push/properties", "prodPush1")
    createAndWriteToFile(swapTestDir + "/swap_prod_push/anotherdir/properties", "prodPush2")
    createAndWriteToFile(swapTestDir + "/swap_prod_push/anotherdir/andAnotherMore/properties", "prodPush3")
    createAndWriteToFile(swapTestDir + "/pom.xml", "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<project xmlns=\"http://maven.apache.org/POM/4.0.0\"\nxmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\nxsi:schemaLocation=\"http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd\">\n<modelVersion>4.0.0</modelVersion>\n<groupId>test</groupId>\n<artifactId>test</artifactId>\n<version>1.1.0</version>\n</project>")



def createStructureWithoutSwapFolders(swapTestDir):
    # Set-up
    if os.path.isdir(swapTestDir):
        shutil.rmtree(swapTestDir)


    os.mkdir(swapTestDir)
    os.mkdir(swapTestDir + "/.git")
    createAndWriteToFile(swapTestDir + "/.git/config", "url=123")
    os.mkdir(swapTestDir + "/controller")
    os.mkdir(swapTestDir + "/business")
    os.mkdir(swapTestDir + "/application")

    createAndWriteToFile(swapTestDir + "/properties.Config", "[APPLICATION]\nVERSION=1.0.0\nARTIFACTORY_DEPLOYMENT_FOLDER=splunk-connect\nTYPE=JAVA")

    createAndWriteToFile(swapTestDir + "/controller/endpoint.java", "Endpoint implementation")
    createAndWriteToFile(swapTestDir + "/business/somethingBusiness.java", "some Logic")
    createAndWriteToFile(swapTestDir + "/application/MyFile.txt", "123")
