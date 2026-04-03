import numpy as np

scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

# Chuẩn hóa Z-score
mean_col = np.mean(scores, axis=0)
std_col = np.std(scores, axis=0)
z_scores = (scores - mean_col) / std_col
print(np.round(z_scores, 2))
print("TB các cột sau chuẩn hóa:", np.mean(z_scores, axis=0))

# 1.	Tính vector trung bình từng môn.
average_scores_per_subject = np.mean(scores, axis=0)
print("\nĐiểm trung bình của từng môn học:")
print(average_scores_per_subject)

#2.	Tính vector độ lệch chuẩn từng môn.
std_dev_per_subject = np.std(scores, axis=0)
print("\nĐộ lệch chuẩn của từng môn học:")
print(std_dev_per_subject)

#3.	Chuẩn hóa toàn bộ ma trận bằng broadcasting
z_scores = (scores - mean_col) / std_col
print("\nMa trận chuẩn hóa Z-score:")
print(np.round(z_scores, 2))

#4.	In ma trận đã chuẩn hóa, làm tròn 2 chữ số thập phân
print("\nMa trận chuẩn hóa Z-score (làm tròn 2 chữ số):")
print(np.round(z_scores, 2))

#5.	Kiểm tra lại trung bình các cột sau chuẩn hóa có gần bằng 0 hay không
print("\nTrung bình các cột sau chuẩn hóa Z-score:")
print(np.mean(z_scores, axis=0))


# Chuẩn hóa về khoảng [0, 1]
min_col = np.min(scores, axis=0)
max_col = np.max(scores, axis=0)
min_max_scores = (scores - min_col) / (max_col - min_col)
print("Ma trận chuẩn hóa [0,1]:")
print(np.round(min_max_scores, 2))