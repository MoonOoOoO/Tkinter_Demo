import matplotlib.pyplot as plt
import numpy as np

plt.subplot(3, 1, 1)
line, = plt.plot([1, 2, 3, 4], [1, 4, 9, 16], '-')
# line.set_antialiased(False)  # 关闭抗锯齿
plt.axis([0, 6, 0, 20])

t = np.arange(0., 5., 0.2)
plt.subplot(3, 1, 2)
plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')

data = {
    'a': np.arange(50),
    'c': np.random.randint(0, 50, 50),
    'd': np.random.randn(50)  # 返回正态分布一个随机值
}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 10

plt.subplot(3, 1, 3)
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('a')
plt.ylabel('b')
plt.show()
