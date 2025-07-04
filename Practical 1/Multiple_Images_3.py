import cv2 
import matplotlib.pyplot as plt 
img = cv2.imread("bheem.jpg") 
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

#cv2.imshow("Original Image", img) 
#cv2.imshow("GrayScale Image", gray_image) 

#Image1 
plt.figure(figsize = (10,5)) 
plt.subplot(1,2,2) 
plt.imshow(img) 
#plt.imshow(img, cmap = 'gray') 
plt.title('Original Image') 
plt.axis('off') 

#Image2 
plt.subplot(1,2,1) 
plt.imshow(gray_image) 
#plt.imshow(gray_image, cmap = 'gray') 
plt.title('GrayScale Image') 
plt.axis('off') 
plt.show()
