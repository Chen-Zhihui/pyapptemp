import logging
logging.info(f"{__file__}")
from abc import get_cache_token
from fbs_runtime.application_context import cached_property
from fbs_runtime.application_context.PyQt5 import ApplicationContext
import qtawesome as qta
from qtpy.QtCore import QStandardPaths, QDir
import qtpy
import logging
import os
import sys
import json
from main.python.widget.rxtool import QtUiScheduler
import main.python.parameters as parameters


class AppConf(object):

    def __init__(self) -> None:
        self.db_filepath = ""

    def load(self, path) :
        try:
            f = open(path)
            j = json.load(f)
            self.db_filepath = j["db_filepath"]
            f.close()
        except:
            pass
        finally:
            pass

    def save(self, path):
        f = open(path, "w")
        c = {
            "db_filepath" : self.db_filepath
        }
        json.dump(c,f)
        f.close()

    def set_db_filepath(self, path):
        self.db_filepath = path

class AppContext(ApplicationContext):

    @cached_property
    def config(self):
        return AppConf()


appctxt = AppContext()       # 1. Instantiate ApplicationContext


logging.info("Application context created")
logging.info(appctxt.app)

# icon_clear = get_icon("")
from cartopy import config 
from main.python.context import appctxt
config["repo_data_dir"] = appctxt.get_resource("cartopy_data")

from .icons import icon_app_mainwin
appctxt.app.setWindowIcon(icon_app_mainwin)                        


appctxt.app.setOrganizationName(parameters.application_com)
appctxt.app.setOrganizationDomain(parameters.application_com_website)
appctxt.app.setApplicationName(parameters.application_name)
appctxt.app.setApplicationDisplayName(parameters.application_title)
appctxt.app.setWindowIcon(icon_app_mainwin)

data_dir = QDir(QDir.homePath()).absoluteFilePath(appctxt.app.applicationName())
if not os.path.exists(data_dir):
    os.mkdir(data_dir)
logging.info("Application Data Dir = {}".format(data_dir))


# data file path
def user_file_path(name):
    return os.path.normpath(os.path.join(data_dir, name))

CONFIG_FILE_PATH = user_file_path("stmatch.json")

def load_config():
    logging.info(f"{__file__}, load config file from {CONFIG_FILE_PATH}")
    appctxt.config.load(CONFIG_FILE_PATH)
    logging.info(f"{__file__}, db path = {appctxt.config.db_filepath}")

def save_config():
    logging.info(f"{__file__}, save config file to {CONFIG_FILE_PATH}")
    logging.info(f"{__file__}, db path = {appctxt.config.db_filepath}")
    appctxt.config.save(CONFIG_FILE_PATH)

appctxt.app.lastWindowClosed.connect(save_config)

try :
    load_config()
except:
    save_config()
finally:
    pass

if __name__ == "__main__":
    for i in [16, 24, 32, 48, 64, 256]:
        icon_app_mainwin.pixmap(i, i).save(f"{i}.png")
        icon_app_mainwin.pixmap(i, i).save(f"{i}.ico")
    