import logging


"""
Logging Demo 1
Logging Levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
logging.basicConfig(filename='test.log',level=logging.DEBUG)

logging.debug("This is debug msg")
logging.warning('This is warning msg')
logging.info('this is info msg')
logging.error('This is info msg')

