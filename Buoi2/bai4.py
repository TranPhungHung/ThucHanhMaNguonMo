import pandas as pd

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv('diemPython.csv')

# Hàm tạo báo cáo
def tao_bao_cao_hoc_phan(df):
    # Sắp xếp theo số thứ tự (STT)
    df = df.sort_values('STT')

    # Tạo tiêu đề báo cáo
    print("BÁO CÁO HỌC PHẦN MÔN HỌC")
    print("------------------------")

    # Hiển thị thông tin môn học
    for index, row in df.iterrows():
        print("Mã lớp:", row['Mã lớp'])
        print("Số SV:", row['Số SV'])
        print("Loại A+: ", row['Loại A+'])
        print("Loại A: ", row['Loại A'])
        print("Loại B+: ", row['Loại B+'])
        print("Loại B: ", row['Loại B'])
        print("Loại C+: ", row['Loại C+'])
        print("Loại C: ", row['Loại C'])
        print("Loại D+: ", row['Loại D+'])
        print("Loại D: ", row['Loại D'])
        print("Loại F: ", row['Loại F'])
        print("------------------------")

# Gọi hàm tạo báo cáo
tao_bao_cao_hoc_phan(df)
