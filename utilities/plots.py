from matplotlib.pyplot import figure, imshow, show


# Plots image (mainly for debugging
def display_image(image, blocking=False):
    figure('Image')                 # Create new figure
    imshow(image, cmap='gray')      # Display image (as greyscale
    show(block=blocking)            # Show figure/make blocking or not
