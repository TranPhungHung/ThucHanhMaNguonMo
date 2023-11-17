import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

# Định nghĩa hàm làm mịn ảnh
def apply_smoothing(image_path):
    image = cv2.imread(image_path)
    smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)  # Có thể thay đổi kích thước kernel và độ mờ tùy ý
    return smoothed_image

# Xử lý sự kiện khi người dùng nhấn nút "Làm mịn"
def smooth_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        smoothed_image = apply_smoothing(file_path)
        smoothed_image = cv2.cvtColor(smoothed_image, cv2.COLOR_BGR2RGB)
        smoothed_image = Image.fromarray(smoothed_image)
        smoothed_image = smoothed_image.resize((400, 400), Image.ANTIALIAS)
        smoothed_image = ImageTk.PhotoImage(smoothed_image)
        image_label.configure(image=smoothed_image)
        image_label.image = smoothed_image

# Tạo giao diện người dùng
window = tk.Tk()
window.title("Ứng dụng Làm mịn ảnh")

# Tạo nút "Chọn ảnh"
select_button = tk.Button(window, text="Chọn ảnh", command=smooth_image)
select_button.pack(pady=10)

# Tạo nhãn để hiển thị ảnh
image_label = tk.Label(window)
image_label.pack()

window.mainloop()
