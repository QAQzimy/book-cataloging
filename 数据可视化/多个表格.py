import matplotlib.pyplot as plt

for idx, color in enumerate("rgbyck"):
    plt.subplot(320+idx+1, facecolor=color)
plt.show()

# enumerate（“RGBYCK”）是一个Python内置函数，它可以将一个可迭代对象转换为一个枚举对象，同时返回每个元素的索引和值。
# 在这个例子中，可迭代对象是字符串“RGBYCK”，枚举对象将返回每个字符的索引和值。
# 例如，当使用enumerate（“RGBYCK”）时，它将返回以下结果：
# [(0, ‘R’), (1, ‘G’), (2, ‘B’), (3, ‘Y’), (4, ‘C’), (5, ‘K’)]。
# 这个函数在循环中经常被使用，以便同时访问索引和值


