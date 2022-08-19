import logging
logging.info(f"{__file__}")
import os 
os.environ['QT_API'] = 'pyqt5'

import PyQt5
import sys 

dirname = os.path.dirname(os.path.dirname(os.__file__))
plugin_path = os.path.join(dirname, "Library", "plugins", "platforms")
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = plugin_path