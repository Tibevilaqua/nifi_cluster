import unittest
from scripts.controller import CreateBucket
import os
import logging
from scripts.resources import Properties

class ReplicateVersionControllerTest(unittest.TestCase):

    def setUp(self):
        # Set-up
        os.chdir(str(str(os.getcwd().split("ci_cd_nifi_registry")[0]) + "ci_cd_nifi_registry"))

    """
        Given that the project does not have any swap folder, all files should remain as they are (no edition)
    """
    def test_run(self):
        logging.basicConfig(level=Properties.LOGGING_LEVEL, format=Properties.LOGGING_FORMAT, datefmt=Properties.LOGGING_DATE_FORMAT)
        CreateBucket.execute("http://localhost:18080", "test7")
        CreateBucket.execute("http://localhost:18080", "test7")


if __name__ == '__main__':
    unittest.main()
