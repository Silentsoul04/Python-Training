#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# man date.
# linux -> crontab.
# window -> scheduler. 
# time.strftime()
# https://docs.python.org/2/howto/logging.html#useful-handlers

import logging
from subprocess import Popen,PIPE
from logging.handlers import SysLogHandler

# l.basicConfig(filename='my_disk.log',filemode='a',level=l.DEBUG,
# 			  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c')


## Advanced tutorials
# Loggers expose the interface that application code directly uses.
# ex: root
# Handlers send the log records (created by loggers) to the appropriate destination.
# ex: filename='my_disk.log',filemode='a'
# Filters provide a finer grained facility for determining which log records to output.
# ex: level=l.DEBUG
# Formatters specify the layout of log records in the final output.
# ex: format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c'



# create logger
logger = logging.getLogger('disk monitor')  # logger name.
logger.setLevel(logging.DEBUG)              # filter for logger.

# create console handler and set level to debug
ch = SysLogHandler(address="/dev/log")               # handler
ch.setLevel(logging.DEBUG)                 # filter for handler.

# create formatter
formatter = logging.Formatter('- %(name)s - %(levelname)s - %(message)s')  # Formatter

# add formatter to ch
ch.setFormatter(formatter)  #  handler and formatter.

# add ch to logger
logger.addHandler(ch)       # logger and handler

## 
# Main program
##

# #disk_size = int(raw_input("please enter the disk size:"))
# df -h / |tail -n 1|awk '{print $5}'|sed 's#%##'

if __name__ == '__main__':
	p1 = Popen(['df','-h','/'],stdout=PIPE)
	p2 = Popen(['tail','-n','1'],stdin=p1.stdout,stdout=PIPE)
	disk_size = int(p2.communicate()[0].split()[4].split('%')[0])

	if disk_size < 50:
		logger.info("The disk looks health at {}.".format(disk_size))
	elif disk_size < 75:
		logger.warning("The disk looks to give some warnings {}.".format(disk_size))
	elif disk_size < 85:
		logger.error("The disk is puking some errors {}".format(disk_size))
	elif disk_size < 100:
		logger.critical("The Application is sleeping now {}".format(disk_size))

