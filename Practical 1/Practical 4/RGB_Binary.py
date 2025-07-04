import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# Load the grayscale image
image = cv2.imread('cartoon.jpeg', cv2.IMREAD_GRAYSCALE)

total=np.sum(image)
w,h=image.shape
avg=int(total/(w*h))

# Apply thresholding
threshold_value = avg  # You can adjust this value
_, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
 
# Display the thresholded image
#cv2.imshow('Thresholded Image', thresholded_image)

#Image1 
plt.figure(figsize = (10,5)) 
plt.subplot(1,2,2) 
#plt.imshow(image) 
plt.imshow(image, cmap = 'gray') 
plt.title('Original Image') 
plt.axis('off') 

#Image2 
plt.subplot(1,2,1) 
#plt.imshow(thresholded_image) 
plt.imshow(thresholded_image, cmap = 'gray') 
plt.title('Thresholded Image') 
plt.axis('off') 
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
