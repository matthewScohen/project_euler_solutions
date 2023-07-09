import math
import numpy as np
import matplotlib.pyplot as plt

size = 10
order = 20
fig, ax = plt.subplots()
ax.scatter(0, 0)
for i in range(1, order+1):
    x = np.arange(-i*size/2, i*size/2+size, size)
    y = np.full(np.size(x), i * size)
    ax.scatter(x, y)
    for x1 in x:
        for y1 in y:
            if y1 <= 60:
                plt.axline((0, 0), (x1, y1))
# plt.axline((0, 0), (5, 30))
# plt.axline((0, 0), (-5, 30))
# plt.axline((0, 0), (5, 10))
# plt.axline((0, 0), (-5, 10))
# plt.axline((0, 0), (0, 20))
# plt.axline((0, 0), (-10, 40))
# plt.axline((0, 0), (10, 40))
plt.show()
