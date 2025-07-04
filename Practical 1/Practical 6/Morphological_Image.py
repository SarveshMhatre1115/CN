import cv2
import numpy as np
from skimage.morphology import skeletonize
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("doraemon.jpg")
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
gray_image = cv2.imread("doraemon.jpg", cv2.IMREAD_GRAYSCALE)
_,binary_image = cv2.threshold(rgb_image, 127, 255, cv2.THRESH_BINARY)

# Create a kernel
kernel = np.ones((5,5), np.uint8)

# Apply morphological operations
erosion = cv2.erode(rgb_image, kernel, iterations=1)
dilation = cv2.dilate(rgb_image, kernel, iterations=1)
opening = cv2.dilate(erosion, kernel, iterations=1)
closing = cv2.erode(dilation, kernel, iterations=1)

binary = binary_image // 255  # Normalize to 0 and 1
skeleton = skeletonize(binary)  # Apply thinning

# Convert back to uint8 (0 and 255)
skeleton = (skeleton * 255).astype(np.uint8)

#Image1 
plt.figure(figsize = (10,5)) 
plt.subplot(2,4,1) 
plt.imshow(rgb_image) 
#plt.imshow(image, cmap = 'gray') 
plt.title('Original Image') 
plt.axis('off')

#Image2
plt.subplot(2,4,2) 
#plt.imshow(gray_image) 
plt.imshow(gray_image, cmap = 'gray') 
plt.title('GrayScale Image') 
plt.axis('off')

#Image3
plt.subplot(2,4,3) 
plt.imshow(binary_image) 
#plt.imshow(binary_image, cmap = 'gray') 
plt.title('Binary Image') 
plt.axis('off')

#Image4
plt.subplot(2,4,4) 
plt.imshow(erosion) 
#plt.imshow(erosion, cmap = 'gray') 
plt.title('Eroded Image') 
plt.axis('off')

#Image5  
plt.subplot(2,4,5) 
plt.imshow(dilation) 
#plt.imshow(dilation, cmap = 'gray') 
plt.title('Dilated Image') 
plt.axis('off')

#Image6
plt.subplot(2,4,6) 
plt.imshow(opening) 
#plt.imshow(opening, cmap = 'gray') 
plt.title('Opening Image') 
plt.axis('off')

#Image7
plt.subplot(2,4,7) 
plt.imshow(closing) 
#plt.imshow(closing, cmap = 'gray') 
plt.title('Closing Image') 
plt.axis('off')

#Image8
plt.subplot(2,4,8) 
plt.imshow(skeleton) 
#plt.imshow(skeleton, cmap = 'gray') 
plt.title('SKeleton Image') 
plt.axis('off')
plt.show()

