#!/usr/bin/python -tt
#btlogger.py
import logging

logger = logging.getLogger('buditaplogger')
hdlr = logging.FileHandler('/var/log/buditaplogger.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

class btlogger:
	
	def __init__(self, logtype, message):
		self.logtype = logtype
		self.logmessage = message
		if self.logtype == 'ERROR':
			logger.error(self.logmessage)
		else:
			logger.info(self.logmessage)
