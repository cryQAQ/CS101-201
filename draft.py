import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy

# 设置参数
loc, scale = 0, 1 # 位置参数和尺度参数

# 生成随机样本
x = np.linspace(-5, 5, 1000)
y = cauchy.pdf(x, loc=loc, scale=scale)

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title("Cauchy Distribution")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.grid()
plt.show()