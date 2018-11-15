from numpy import histogram as make_histogram
from matplotlib.pyplot import figure, show, title, hist


# Function that plots a histogram of an image
def plot_histogram(image):
    histogram = make_histogram(image)   # Use numpy to calculate

    figure('Histogram')                 # Make new figure
    hist(histogram[0])                  # Plot histogram
    title('Histogram')                  # Add title
    show(block=False)                   # Show image (non-blocking)
