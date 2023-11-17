import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

# Định nghĩa hàm tăng cường chất lượng ảnh
def enhance_brightness(image_path):
    image = cv2.imread(image_path)
    enhanced_image = cv2.convertScaleAbs(image, alpha=1.2, beta=10)  # Thay đổi alpha và beta tùy ý
    return enhanced_image

# Xử lý sự kiện khi người dùng nhấn nút "Tăng cường sáng"
def enhance_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        enhanced_image = enhance_brightness(file_path)
        enhanced_image = cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB)
        enhanced_image = Image.fromarray(enhanced_image)
        enhanced_image = enhanced_image.resize((400, 400), Image.ANTIALIAS)
        enhanced_image = ImageTk.PhotoImage(enhanced_image)
        image_label.configure(image=enhanced_image)
        image_label.image = enhanced_image

# Tạo giao diện người dùng
window = tk.Tk()
window.title("Ứng dụng Tăng cường chất lượng ảnh thiếu sáng")

# Tạo nút "Chọn ảnh"
select_button = tk.Button(window, text="Chọn ảnh", command=enhance_image)
select_button.pack(pady=10)

# Tạo nhãn để hiển thị ảnh
image_label = tk.Label(window)
image_label.pack()

window.mainloop()
