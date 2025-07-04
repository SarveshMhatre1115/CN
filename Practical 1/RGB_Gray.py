#Method1
import cv2 
img = cv2.imread("bheem.jpg") 
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow("Original Image", img) 
cv2.imshow("Grayscale Image", gray_image)

#Method2
import cv2 
img = cv2.imread("bheem.jpg") 
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow("Original Image", img) 
converted_image = cv2.imread("bheem.jpg", cv2.IMREAD_GRAYSCALE) 
cv2.imshow("Converted Image", converted_image) 
