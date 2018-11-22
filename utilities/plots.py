from matplotlib.pyplot import figure, imshow, show, title, plot, cm, scatter
from numpy import linspace


# Plots image (mainly for debugging
def display_image(image, _title='Test image', blocking=False):
    figure(_title)                 # Create new figure
    imshow(image, cmap='gray')      # Display image (as greyscale
    if _title != 'Test image':
        title(_title)
    show(block=blocking)            # Show figure/make blocking or not


def plot_image(features, _title='Image plot', blocking=False):
    figure(_title)
    scatter(features[:, 0], features[:, 1])
    title(_title)
    show(block=blocking)


def plot_clusters(feature_sets, labels, _title='Clustered image', blocking=True):
    figure(_title)
    colours = [cm.Spectral(each) for each in linspace(0, 1, len(feature_sets))]

    for label, colour, feature in zip(labels, colours, feature_sets):
        if label == -1:
            colour = [0, 0, 0, 1]

        plot(feature[:, 0], feature[:, 1], 'o', markerfacecolor=tuple(colour), markeredgecolor='k', markersize=14)

        # coord = feature_points[class_mask & ~sample_mask]
        # plt.plot(feature[:, 0], feature[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='b', markersize=6)
    title(_title)
    show(block=blocking)
