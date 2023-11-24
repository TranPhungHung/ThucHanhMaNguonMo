import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tập tin CSV
data = pd.read_csv("Student_Performance.csv")

# Tính min, max, trung bình của từng cột dữ liệu
min_values = data.min()
max_values = data.max()
mean_values = data.mean()

# In kết quả
print("Min values:")
print(min_values)
print("\nMax values:")
print(max_values)
print("\nMean values:")
print(mean_values)

# Vẽ đồ thị phân bố của từng cột dữ liệu
data.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()
