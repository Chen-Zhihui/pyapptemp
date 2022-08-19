import logging
logging.info(f"{__file__}")
import matplotlib

matplotlib.use('Qt5Agg')


# matplotlib style
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）
# print(plt.style.available)
"""
['Solarize_Light2', '_classic_test_patch', 
'bmh', 'classic', 'dark_background', 
'fast', 'fivethirtyeight', 'ggplot', 
'grayscale', 'seaborn', 
'seaborn-bright', 
'seaborn-colorblind', 
'seaborn-dark', 'seaborn-dark-palette', 
'seaborn-darkgrid', 'seaborn-deep', 
'seaborn-muted', 'seaborn-notebook', 
'seaborn-paper', 'seaborn-pastel', 
'seaborn-poster', 'seaborn-talk', 
'seaborn-ticks', 'seaborn-white', 
'seaborn-whitegrid', 
'tableau-colorblind10']
"""
import matplotlib.style as mplstyle 
# mplstyle.use('fast')
# mplstyle.use(['dark_background', 'ggplot', 'fast'])
mplstyle.use(["dark_background"])