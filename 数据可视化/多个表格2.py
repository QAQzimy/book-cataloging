import matplotlib.pyplot as plt

plt.subplot(221) # 第一行的左图
plt.subplot(222) # 第一行的右图
plt.subplot(212) # 第二整行
plt.show()

#https://blog.csdn.net/zxyhhjs2017/article/details/85095621?spm=1018.2226.3001.9630.1&extra%5Btitle%5D=python---subplot%E5%87%BD%E6%95%B0&extra%5Bposition%5D=result&extra%5Butm_medium%5D=distribute.pc_search_result.none-task-cask-2~all~insert_cask~default-1-null.142%5Ev96%5Epc_search_result_base3&extra%5Butm_source%5D=vip_chatgpt_common_search_pc_result
#如果 numRows ＝ 2, numCols ＝ 3, 那整个绘制图表样式为 2X3 的图片区域, 用坐标表示为
#(1, 1), (1, 2), (1, 3)
#(2, 1), (2, 2), (2, 3)
#分别表示为
#(231),(232),(233),(234),(235),(236)
#在不输入时，该位置显示白色
#如果 numRows ＝ 2, numCols ＝ 1, 那整个绘制图表样式为 2X1 的图片区域, 用坐标表示为
#(1,1)
#(1,2)
