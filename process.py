from numpy import percentile, copy


# Threshold image
# Thresholding is a process where all values below an intensity are removed
def threshold_image(image, percent=95, make_copy=False):
    threshold = percentile(image, percent)  # Calculate cutoff intensity
    if make_copy:                           # Make copy original image
        image = copy(image)

    image[image < threshold] = 0            # Threshold image
    image[image > 0] = 255                  # Set remaining values to maxc
    if make_copy:                           # Return image if copy was made
        return image
