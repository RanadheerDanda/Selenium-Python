"""
Logging Format
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
"""
import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
logging.debug("This is debug msg")
logging.warning('This is warning msg')
logging.info('this is info msg')
logging.error('This is info msg')
