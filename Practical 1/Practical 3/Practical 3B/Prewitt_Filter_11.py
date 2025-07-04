import numpy as np
import cv2
import matplotlib.pyplot as plt
 
def apply_prewitt_filter(image_path):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: Unable to load image.")
        return
    # Define Prewitt operator kernels
    prewitt_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)
    prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)
    # Apply filters
    grad_x = cv2.filter2D(img, -1, prewitt_x)
    grad_y = cv2.filter2D(img, -1, prewitt_y)
    # Combine gradients
    gradient_magnitude = cv2.magnitude(grad_x.astype(np.float32), grad_y.astype(np.float32))
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    # Display results
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image')
    plt.subplot(1, 3, 2), plt.imshow(grad_x, cmap='gray'), plt.title('Prewitt X')
    plt.subplot(1, 3, 3), plt.imshow(grad_y, cmap='gray'), plt.title('Prewitt Y')
    plt.figure(figsize=(5, 5))
    plt.imshow(gradient_magnitude, cmap='gray'), plt.title('Gradient Magnitude')
    plt.show()
 
# Example usage
apply_prewitt_filter('C:/Users/admin/Desktop/Nupur (M.Sc.IT)/CV Practical/Practical 4/Flower.jpg')
