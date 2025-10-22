from __future__ import division
from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
np.random.seed(12345)
plt.rc('figure', figsize=(10, 6))
from pandas import Series, DataFrame
import pandas as pd
np.set_printoptions(precision=4)

#get_ipython().magic(u'matplotlib inline')
#get_ipython().magic(u'pwd')



#条形图
from pylab import *
n = 12
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

#这是一个使用Matplotlib库中的plt.bar函数来绘制柱状图的代码示例。
# 其中X是一个包含每个柱子的位置的数组，Y1是一个包含每个柱子高度的数组。
# facecolor参数指定了柱子的填充颜色，edgecolor参数指定了柱子的边框颜色。
# 在这个例子中，柱子的填充颜色为淡蓝色，边框颜色为白色。
# +号表示柱子的方向是朝上的
bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x,y in zip(X,Y1):
 text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')
ylim(-1.25,+1.25)
show()
