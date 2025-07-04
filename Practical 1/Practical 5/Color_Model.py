import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# Load the image
image = cv2.imread('images.jpeg')
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
 
# Convert to HSV (Hue, Saturation, Value)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 
# Convert to LAB (CIELAB) color space
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
 
# Convert to YCbCr
ycbcr_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2YCrCb)
 
# Convert to CMYK
#cmyk_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2CMYK)
 
# Convert to YIQ
yiq_image = np.zeros_like(rgb_image, dtype=np.float32)
 
yiq_image[:,:,0] = 0.299 * rgb_image[:,:,2] + 0.587 * rgb_image[:,:,1] + 0.114 * rgb_image[:,:,0]
yiq_image[:,:,1] = 0.596 * rgb_image[:,:,2] - 0.274 * rgb_image[:,:,1] - 0.322 * rgb_image[:,:,0]
yiq_image[:,:,2] = 0.211 * rgb_image[:,:,2] - 0.523 * rgb_image[:,:,1] + 0.312 * rgb_image[:,:,0]
 
yiq_image = np.clip(yiq_image, 0, 255).astype(np.uint8)
 
# Display the original and converted images
#cv2.imshow('Original Image', image)
#cv2.imshow('HSV Image', hsv_image)
#cv2.imshow('LAB Image', lab_image)
#cv2.imshow('YCbCr Image', ycbcr_image)
#cv2.imshow('CMYK Image', cmyk_image)
#cv2.imshow('YIQ Image', yiq_image)

#Image1 
plt.figure(figsize = (10,5)) 
plt.subplot(4,2,1) 
plt.imshow(rgb_image) 
#plt.imshow(image, cmap = 'gray') 
plt.title('Original Image') 
plt.axis('off')

#Image2
plt.subplot(4,2,2) 
plt.imshow(hsv_image) 
#plt.imshow(hsv_image, cmap = 'gray') 
plt.title('HSV Image') 
plt.axis('off')

#Image3
plt.subplot(4,2,3) 
plt.imshow(rgb_image) 
#plt.imshow(image, cmap = 'gray') 
plt.title('Original Image') 
plt.axis('off')

#Image4
plt.subplot(4,2,4) 
plt.imshow(lab_image) 
#plt.imshow(lab_image, cmap = 'gray') 
plt.title('LAB Image') 
plt.axis('off')

#Image5  
plt.subplot(4,2,5) 
plt.imshow(rgb_image) 
#plt.imshow(image, cmap = 'gray') 
plt.title('Original Image') 
plt.axis('off')

#Image6
plt.subplot(4,2,6) 
plt.imshow(ycbcr_image) 
#plt.imshow(ycbcr_image, cmap = 'gray') 
plt.title('YCbCr Image') 
plt.axis('off')

#Image7
plt.subplot(4,2,7) 
plt.imshow(rgb_image) 
#plt.imshow(image, cmap = 'gray') 
plt.title('Original Image') 
plt.axis('off')

#Image8
plt.subplot(4,2,8) 
plt.imshow(yiq_image) 
#plt.imshow(yiq_image, cmap = 'gray') 
plt.title('YIQ Image') 
plt.axis('off')
plt.show()
 
# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
