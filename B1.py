import numpy as np

scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

#1 in ra ma ma trận điểm
print("Ma trận điểm:")
print(scores)

# tính điểm trung bình ma trận điểm
average_scores = np.mean(scores )
print("\nĐiểm trung bình của ma trận điểm:")
print(average_scores)

# tinh diem trung bình của từng học sinh
average_scores_per_student = np.mean(scores, axis=1)
print("\nĐiểm trung bình của từng học sinh:")
print(average_scores_per_student)

#  tinh diem trung bình của từng môn học
average_scores_per_subject = np.mean(scores, axis=0)
print("\nĐiểm trung bình của từng môn học:")
print(average_scores_per_subject)

# tim diem cao nhat va thap nhat trong ma tran diem
highest_score = np.max(scores)
lowest_score = np.min(scores)
print("\nĐiểm cao nhất trong ma trận điểm:", highest_score)
print("Điểm thấp nhất trong ma trận điểm:", lowest_score)

# tinh do lech chuan theo tung mon hoc
std_dev_per_subject = np.std(scores, axis=0)
print("\nĐộ lệch chuẩn của từng môn học:")
print(std_dev_per_subject)

# tim hoc sinh co diem tb cao nhat
highest_avg_score = np.max(average_scores_per_student)
print("\nHọc sinh có điểm trung bình cao nhất (điểm):", highest_avg_score)
