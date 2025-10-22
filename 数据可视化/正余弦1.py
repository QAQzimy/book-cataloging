import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,1000)

y=np.sin(x)
z=np.cos(x**2)

#设置宽度和高度，dpi为每英寸像素，默认为80
plt.figure(figsize=(8,4))

#args：传递xy值到点，label：给曲线取一个名字，用于在legend显示
#color：颜色可以用英文单词，或是以“#”字符开头的三个16进制数，如#ff0000为红色，（1.0,0.0,0.0）为红色
#linewidth：曲线宽度
#“b--”：b表示蓝色，--表示虚线。在IPython中输入plt.plot? 可查看所有参数说明
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$(x^2)$")

#设置x，y，标题(title)
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin a    con  a^2")
#xlim,ylim。分别设置XY轴的显示范围
plt.ylim(-1.2,1.2)
#显示每条曲线的标签(label)和样式的矩形区域
plt.legend()

#展示
plt.show()
