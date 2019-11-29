import os
import shutil

from scripts.infrastructure import AttributesUtils


def createDir(dir):
    os.mkdir(dir)

def deleteDir(dir):
    if AttributesUtils.isValueValid(str(dir)):
        shutil.rmtree(dir)
    else:
        print(str(dir) + " is invalid. Stopping execution. Check deleteDir method in the OSRepository class")