import logging

def logErrorIfNotZero(status, errorMessage):
    if status != 0:
        logging.error(errorMessage)