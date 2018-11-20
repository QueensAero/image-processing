from matplotlib.pyplot import figure, imshow, show, title


# Plots image (mainly for debugging
def display_image(image, _title='Test image', blocking=False):
    figure(_title)                 # Create new figure
    imshow(image, cmap='gray')      # Display image (as greyscale
    if _title != 'Test image':
        title(_title)
    show(block=blocking)            # Show figure/make blocking or not
