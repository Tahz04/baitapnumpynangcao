import numpy as np
import matplotlib.pyplot as plt

# 1. Mô phỏng 1 random walk [cite: 71, 72, 73, 74, 75, 77]
np.random.seed(42)
steps = np.random.choice([-1, 1], size=100)
walk = np.cumsum(steps)

print("10 vị trí đầu tiên:", walk[:10])
print("Vị trí cuối cùng:", walk[-1])
print("Vị trí lớn nhất:", np.max(walk))
print("Vị trí nhỏ nhất:", np.min(walk))

plt.plot(walk)
plt.title("Random Walk 1 chiều")
plt.xlabel("Bước")
plt.ylabel("Vị trí")
plt.grid(True)
plt.show()

# 2. Yêu cầu nâng cao: Mô phỏng 100 random walk [cite: 78, 79, 80]
steps_many = np.random.choice([-1, 1], size=(100, 100))
walks_many = np.cumsum(steps_many, axis=1)

final_positions = walks_many[:, -1]
print("Số walk kết thúc dương:", np.sum(final_positions > 0))

hit_10 = np.any(np.abs(walks_many) >= 10, axis=1)
print("Số walk chạm ngưỡng |10|:", np.sum(hit_10))