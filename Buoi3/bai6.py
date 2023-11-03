import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
data = pd.read_csv('Student_Performance.csv')

# Chia dữ liệu thành features (đầu vào) và labels (đầu ra)
features = data.drop('Performance Index', axis=1)
labels = data['Performance Index']

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.2, random_state=42)

# Xây dựng mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(train_features, train_labels)

# Dự đoán kết quả trên tập kiểm tra
predictions = model.predict(test_features)

# Đánh giá mô hình bằng độ đo RMSE
rmse = mean_squared_error(test_labels, predictions, squared=False)
print('Root Mean Squared Error (RMSE):', rmse)

# Hiển thị kết quả trên đồ thị
plt.figure(figsize=(10, 5))

# Đồ thị dự đoán
plt.subplot(1, 2, 1)
plt.scatter(range(len(test_labels)), test_labels, color='blue', label='Thực tế')
plt.scatter(range(len(predictions)), predictions, color='red', label='Dự đoán')
plt.xlabel('Số mẫu')
plt.ylabel('Kết quả')
plt.title('Kết quả dự đoán và thực tế')
plt.legend()

# Đồ thị thực tế
plt.subplot(1, 2, 2)
plt.scatter(range(len(test_labels)), test_labels, color='blue', label='Thực tế')
plt.xlabel('Số mẫu')
plt.ylabel('Kết quả')
plt.title('Kết quả thực tế')
plt.legend()

plt.tight_layout()
plt.show()
