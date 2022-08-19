"""
conda create -n t3 python=3.9
conda activate t39
conda install gdal=3.5.1 -c conda-forge  # 提示安装多个安装包，包括numpy 1.23.1
"""

import numpy as np
import osgeo
from osgeo import gdal
import sys

d = gdal.Open(r'D:/data/LC08_L1TP_125034_20130830_20170502_01_T1_B4.TIF')

w, h, c = d.RasterXSize, d.RasterYSize, d.RasterCount
print(f"w={w}, h={h}, c={c}")
print(f"python version={sys.version_info}")
print(f"numpy version={np.__version__}")
print(f"gdal version={osgeo.__version__}")