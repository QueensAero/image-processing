from PIL import Image
from numpy import array


# Function to import test images
def import_image(filename, abs_path=False, gray_scale=False):
    file_path = filename                            # Initialize filename
    if not abs_path:                                # If not listed as an absolute path
        file_path = 'test_images/' + file_path      # Add test_images/ directory to path

    raw_image = Image.open(file_path)               # Import image
    if gray_scale:                                  # Convert to greyscale
        raw_image = raw_image.convert('L')

    image_data = array(raw_image)                   # Convert to matrix

    return image_data
