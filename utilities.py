from PIL import Image
from numpy import array


# Function to import test images
def import_image(filename, abs_path=False):
    file_path = filename                            # Initialize filename
    if not abs_path:                                # If not listed as an absolute path
        file_path = 'test_images/' + file_path      # Add test_images/ directory to path

    im = array(Image.open(file_path))               # Import image

    return im

