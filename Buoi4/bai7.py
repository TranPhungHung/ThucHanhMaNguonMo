import cv2
from PIL import ImageTk, Image
import matplotlib.pyplot as plt


image = cv2.imread('/content/anh1.jpg')
smoothed_image = cv2.GaussianBlur(image, (5, 5), 3)  # Có thể thay đổi kích thước kernel và độ mờ tùy ý
   

# Tạo một figure với kích thước mới (width, height)
plt.figure(figsize=(8, 8))

plt.subplot(121),plt.imshow(image)
plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(smoothed_image)
plt.title('Smoothed'),plt.xticks([]),plt.yticks([])

plt.show()
