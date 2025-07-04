import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# Load the image
image_path = 'C:/Users/admin/Desktop/Nupur (M.Sc.IT)/CV Practical/Practical 4/Flower.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
 
# Check if the image was loaded successfully
if original_image is None:
    print("Error loading the image.")
else:
    # Apply Sobel filter in the x and y directions
    sobel_x = cv2.Sobel(original_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(original_image, cv2.CV_64F, 0, 1, ksize=3)
 
    # Convert the results to absolute values and then to 8-bit
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)
 
    # Combine the Sobel images to get the gradient magnitude
    gradient_magnitude = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
 
    # Display the original image and the gradient magnitude
    #cv2.imshow('Original Image', original_image)
    #cv2.imshow('Gradient Magnitude', gradient_magnitude)

    #Image1
    plt.figure(figsize = (10,5))
    plt.subplot(1,2,2)
    #plt.imshow(original_image)
    plt.imshow(original_image, cmap = 'gray')
    plt.title('Original Image')
    plt.axis('off')

    #Image2
    plt.subplot(1,2,1)
    #plt.imshow(gradient_magnitude)
    plt.imshow(gradient_magnitude, cmap = 'gray')
    plt.title('Gradient Magnitude')
    plt.axis('off')
    plt.show()

 
    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
