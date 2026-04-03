import numpy as np
quantity = np.array([
    [10, 12, 9, 14],
    [5, 7, 8, 6],
    [20, 18, 25, 22]
])
price = np.array([15000, 25000, 10000])

# Tính toán doanh thu [cite: 46, 47, 48, 49, 50, 52]
revenue = quantity * price.reshape(3, 1)
print("Doanh thu từng sản phẩm theo ngày:\n", revenue)

sum_product = np.sum(revenue, axis=1)
sum_day = np.sum(revenue, axis=0)

print("Tổng doanh thu từng sản phẩm:", sum_product)
print("Tổng doanh thu từng ngày:", sum_day)
print("Ngày có doanh thu cao nhất (Ngày thứ):", np.argmax(sum_day) + 1)

ratio = sum_product / np.sum(sum_product)
print("Tỷ trọng doanh thu từng sản phẩm:", np.round(ratio * 100, 2), "%")