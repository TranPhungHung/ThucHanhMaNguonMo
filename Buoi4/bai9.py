import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('/content/anh1.jpg')
enhanced_image = cv2.convertScaleAbs(image, alpha=1.2, beta=10)  # Thay đổi alpha và beta tùy ý

# Tạo một figure với kích thước mới (width, height)
plt.figure(figsize=(8, 8))

plt.subplot(121),plt.imshow(image)
plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(enhanced_image)
plt.title('Enhanced'),plt.xticks([]),plt.yticks([])

plt.show()
