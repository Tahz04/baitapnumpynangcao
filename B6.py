import numpy as np
import pandas as pd

# Phần 2. Dữ liệu thô ban đầu [cite: 95, 96]
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV03", "SV05", "SV06", "SV07", "SV08"],
    "Tuoi": [20, 21, 19, 19, None, 22, 35, 20],
    "GioiTinh": ["Nam", "Nữ", "nu", "nu", "Nam", "Nữ", "Nam", None],
    "GioTuHoc": [2.5, 3, None, 4, 2, 10, -1, 3.5],
    "GioMangXaHoi": [4, 5, 3.5, 3.5, 20, 2, 5, None],
    "DiemTB": [3.1, 2.8, 3.5, 3.5, 2.0, 3.8, 4.5, None]
}
df = pd.DataFrame(data)

# Xử lý và làm sạch dữ liệu
print("Kích thước dữ liệu ban đầu:", df.shape)
print("Dữ liệu thiếu theo cột:\n", df.isnull().sum())

# Xóa bản ghi trùng
df = df.drop_duplicates(subset="MaSV")

# Chuẩn hóa giới tính
df["GioiTinh"] = df["GioiTinh"].replace({"nu": "Nữ", "Nữ": "Nữ", "Nam": "Nam"})
df["GioiTinh"] = df["GioiTinh"].fillna("Không rõ")

# Điền dữ liệu thiếu bằng trung bình
cols_to_fill = ["Tuoi", "GioTuHoc", "GioMangXaHoi", "DiemTB"]
for col in cols_to_fill:
    df[col] = df[col].fillna(df[col].mean())

# Sửa dữ liệu bất thường bằng trung bình
df.loc[df["Tuoi"] > 30, "Tuoi"] = df["Tuoi"].mean()
df.loc[df["GioTuHoc"] < 0, "GioTuHoc"] = df["GioTuHoc"].mean()
df.loc[df["GioMangXaHoi"] > 12, "GioMangXaHoi"] = df["GioMangXaHoi"].mean()
df.loc[df["DiemTB"] > 4.0, "DiemTB"] = df["DiemTB"].mean()

print("\nDữ liệu sau làm sạch:\n", df)

# Chuẩn hóa biến số [cite: 106, 107, 111, 112]
cols = ["Tuoi", "GioTuHoc", "GioMangXaHoi", "DiemTB"]

# Min-Max Scaling
df_minmax = df.copy()
for col in cols:
    df_minmax[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

# Z-score Scaling
df_zscore = df.copy()
for col in cols:
    df_zscore[col] = (df[col] - df[col].mean()) / df[col].std()

print("\nDữ liệu sau chuẩn hóa Min-Max:\n", df_minmax)
print("\nDữ liệu sau chuẩn hóa Z-score:\n", df_zscore)