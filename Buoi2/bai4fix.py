import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
data = pd.read_csv('diemPython.csv')

# Tính tổng số sinh viên
total_students = data['Số SV'].sum()
print('Tong so sv di thi')
print(total_students)
# Tính số sinh viên của từng loại điểm
point_categories = ['Loại A+', 'Loại A', 'Loại B+', 'Loại B', 'Loại C+', 'Loại C', 'Loại D+', 'Loại D', 'Loại F']
point_counts = data[point_categories].sum()
print('Tong so sv xep vao tung nhom diem')
print(point_counts)
# Tìm lớp có nhiều sinh viên đạt điểm A nhất
max_a_class = data.loc[data['Loại A'] == data['Loại A'].max(), 'Mã lớp'].values[0]
print('lop co tong so sv dat loai A cao nhat')
print(max_a_class)
# Vẽ đồ thị so sánh số sinh viên đạt điểm A và B+ của tất cả các lớp
classes = data['Mã lớp']
points_a = data['Loại A']
points_b_plus = data['Loại B+']

plt.plot(classes, points_a, label='Loại A')
plt.plot(classes, points_b_plus, label='Loại B+')

plt.xlabel('Mã lớp')
plt.ylabel('Số sinh viên')
plt.title('Số sinh viên đạt điểm A và B+ của các lớp')
plt.legend()

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
