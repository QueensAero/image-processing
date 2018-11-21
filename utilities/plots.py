from matplotlib.pyplot import figure, imshow, show, title, plot, cm
from numpy import linspace


# Plots image (mainly for debugging
def display_image(image, _title='Test image', blocking=False):
    figure(_title)                 # Create new figure
    imshow(image, cmap='gray')      # Display image (as greyscale
    if _title != 'Test image':
        title(_title)
    show(block=blocking)            # Show figure/make blocking or not


def plot_clusters(clusters, sample_mask, labels, n, _title='Clustered image'):
    figure(_title)
    colours = [cm.Spectral(each) for each in linspace(0, 1, n)]
    for k, col in zip(labels, colours):
        if k == -1:
            col = [0, 0, 0, 1]

        class_mask = (labels == k)
        coord = clusters[class_mask & sample_mask]
        plot(coord[:, 0], coord[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=14)

        coord = clusters[class_mask & ~sample_mask]
        plot(coord[:, 0], coord[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='b', markersize=6)

    title(_title)
    show()
