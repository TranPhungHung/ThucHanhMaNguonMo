import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

# Định nghĩa hàm tách biên ảnh
def apply_edge_detection(image_path):
    image = cv2.imread(image_path, 0)
    edges = cv2.Canny(image, 100, 200)  # Thay đổi ngưỡng tùy ý
    return edges

# Xử lý sự kiện khi người dùng nhấn nút "Tách biên"
def detect_edges():
    file_path = filedialog.askopenfilename()
    if file_path:
        edges = apply_edge_detection(file_path)
        edges_image = Image.fromarray(edges)
        edges_image = edges_image.resize((400, 400), Image.ANTIALIAS)
        edges_image = ImageTk.PhotoImage(edges_image)
        image_label.configure(image=edges_image)
        image_label.image = edges_image

# Tạo giao diện người dùng
window = tk.Tk()
window.title("Ứng dụng Tách biên ảnh")

# Tạo nút "Chọn ảnh"
select_button = tk.Button(window, text="Chọn ảnh", command=detect_edges)
select_button.pack(pady=10)

# Tạo nhãn để hiển thị ảnh
image_label = tk.Label(window)
image_label.pack()

window.mainloop()
