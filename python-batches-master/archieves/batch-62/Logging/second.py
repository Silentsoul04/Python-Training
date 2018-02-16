#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# man date

import logging

logging.basicConfig(filename="myapp.log",filemode='a',level=logging.DEBUG,format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s',
	datefmt = '%c')

# levels
logging.debug("this is an debug message")
logging.info("this is an information message.")
logging.warning("this is an warning message")
logging.error("This is an error message")
logging.critical("This is an critical message")

'''
(myenv) khyaathi@khyaathi-Technologies:~/Documents/tuxfux-hlp-notes/python-notes/batch-62/Logging$ python first.py 
WARNING:root:this is an warning message
ERROR:root:This is an error message
CRITICAL:root:This is an critical message
(myenv) khyaathi@khyaathi-Technologies:~/Documents/tuxfux-hlp-notes/python-notes/batch-62/Logging$ 
'''

