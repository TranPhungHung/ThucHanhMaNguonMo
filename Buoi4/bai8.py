import cv2
import matplotlib.pyplot as plt


image = cv2.imread('/content/anh1.jpg')
edges = cv2.Canny(image, 100, 200)  # Thay đổi ngưỡng tùy ý


# Tạo một figure với kích thước mới (width, height)
plt.figure(figsize=(8, 8))

plt.subplot(121),plt.imshow(image)
plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edges)
plt.title('Edge'),plt.xticks([]),plt.yticks([])

plt.show()
