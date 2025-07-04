from PIL import Image 
import numpy as np
 
def shift_image(img, depth_img, shift_amount=10): 
	# Ensure base image has alpha 
	img = img.convert("RGBA") 
	data = np.array(img)
 
	# Ensure depth image is grayscale (for single value) 
	depth_img = depth_img.convert("L") 
	depth_data = np.array(depth_img) 
	deltas = ((depth_data / 255.0) * float(shift_amount)).astype(int)
	# This creates the transparent resulting image. 
	# For now, we're dealing with pixel data. 
	shifted_data = np.zeros_like(data)
 
	height, width, _ = data.shape
 
	for y, row in enumerate(deltas): 
		for x, dx in enumerate(row): 
			if x + dx < width and x + dx >= 0: 
				shifted_data[y, x + dx] = data[y, x]
 
	# Convert the pixel data to an image. 
	shifted_image = Image.fromarray(shifted_data.astype(np.uint8))
 
	return shifted_image
 
img = Image.open("2D_1.jpeg") 
depth_img = Image.open("2D_2.jpeg") 
shifted_img = shift_image(img, depth_img, shift_amount=10) 
shifted_img.show()
