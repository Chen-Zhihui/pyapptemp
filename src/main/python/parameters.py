import logging
logging.info(f"{__file__}")

from pyproj import Geod
import random

application_title = "应用名称"
application_name  = "STMatch"
application_com = "SFF"
application_com_website = "www.sff.com"

debug = False

geod = Geod(ellps='WGS84')

dlat = 0.25
dlon = 0.25
lat_range= dlat * 3
lon_range= dlon * 3
r = 7.7 * 1000

SCENCE_MAX_HALF_WIDTH = 7.7 * 1000 

