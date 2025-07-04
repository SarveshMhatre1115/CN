from PIL import Image
import os

def make_overlapping_crops(image_path, output_dir, crop_size=(200, 200), overlap=50):
    # Load image
    img = Image.open(image_path)
    width, height = img.size

    crop_width, crop_height = crop_size
    step_x = crop_width - overlap
    step_y = crop_height - overlap

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    crop_count = 0

    for y in range(0, height - crop_height + 1, step_y):
        for x in range(0, width - crop_width + 1, step_x):
            crop_box = (x, y, x + crop_width, y + crop_height)
            crop = img.crop(crop_box)
            crop.save(os.path.join(output_dir, f"crop_{crop_count + 1}.png"))
            crop_count += 1

            if crop_count == 4:  # Only 4 crops
                return

    print(f"Generated {crop_count} overlapping crops.")

# Example usage
make_overlapping_crops("img.jpeg", "output_crops", crop_size=(200, 200), overlap=50)
