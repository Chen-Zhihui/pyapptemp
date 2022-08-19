'''

logging.info("Open Metrics Mgr DB {}".format(metrics_sys_files))
logging.exception(sys.exc_info()[0])
logging.info(self.names)
logging.info(self.oids)
logging.info("\n{}".format(self.index.head()))
logging.info("\n{}".format(self.buddy.head()) if self.buddy else "buddy=None")
logging.error("load file error {}".format(path))
'''

import logging
import os
import os.path

from pathlib import Path
filepath = Path.home().joinpath( 'Documents', 'stmatch.log.txt' )

from logging.config import dictConfig
f = logging.FileHandler( f"{filepath}") 
f.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
f.setFormatter(formatter)

logging_config = dict(
    version = 1,
    formatters = {
        'f': {'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
    filters = {
        "stmatch" : { "name" :"", } 
    },
    handlers = {
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG,
              "filters" : ["stmatch"],
            },
        },
    root = {
        'handlers': ['h'],
        'level': logging.INFO,
        },
)
dictConfig(logging_config)

logging.root.addHandler(f)

