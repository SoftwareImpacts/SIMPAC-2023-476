import cv2
import numpy as np
from skimage.segmentation import slic
from skimage.color import label2rgb
import matplotlib.pyplot as plt

# Load an image
image_path = 'C:\Users\jaike\Desktop\Picture2.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform COTP-based image enhancement (assuming you have the COTP algorithm implemented)
enhanced_image = enhance_with_cotp(gray_image)

# Perform segmentation using SLIC (or any other segmentation algorithm)
segments = slic(enhanced_image, n_segments=100, compactness=10)

# Create a mask for a specific segment
target_segment_index = 42
segment_mask = (segments == target_segment_index)

# Apply the mask to the original image to visualize the segmented region
segmented_region = cv2.bitwise_and(image, image, mask=segment_mask.astype(np.uint8))

# Display the original image, enhanced image, and segmented region
plt.figure(figsize=(10, 6))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(132)
plt.imshow(enhanced_image, cmap='gray')
plt.title('Enhanced Image')

plt.subplot(133)
plt.imshow(cv2.cvtColor(segmented_region, cv2.COLOR_BGR2RGB))
plt.title('Segmented Region')

plt.tight_layout()
plt.show()
