import logging

def logInfoIfNotZero(status, message):
    if status != 0:
        logging.info(message)


def logInfoIfZero(status, message):
    if status == 0:
        logging.info(message)