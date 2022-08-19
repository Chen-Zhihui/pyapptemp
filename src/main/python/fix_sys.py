import sys
import os
import logging
import logging
logging.info(f"{__file__}")
for k in os.environ.keys():
    logging.info(f"{k}={os.environ[k]}") #["QT_QPA_PLATFORM_PLUGIN_PATH"])