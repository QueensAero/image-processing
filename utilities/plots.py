from matplotlib.pyplot import figure, imshow, show, title, plot, cm, scatter, savefig
from numpy import linspace


# Plots image (mainly for debugging
def display_image(image, _title='Test image', blocking=False):
    figure(_title)                  # Create new figure
    imshow(image, cmap='gray')      # Display image (as greyscale
    title(_title)                   # Display title
    show(block=blocking)            # Show figure/make blocking or not


# Function to plot points from image (thresholded usually)
def plot_image(features, _title='Image plot', blocking=False):
    figure(_title)                              # Create figure
    scatter(features[:, 0], features[:, 1])     # Plot points as scatter plot
    title(_title)                               # Add title
    show(block=blocking)                        # Display figure


# Function to plot list of clusters
def plot_clusters(feature_sets, labels, _title='Clustered image', blocking=True, save=True):
    figure(_title)                                                              # Create new figure
    colours = [cm.Spectral(each) for each in
               linspace(0, 1, len(feature_sets))]                               # Generate set of colours

    for label, colour, feature in zip(labels, colours, feature_sets):           # For each cluster
        if label == -1:                                                         # If noise plot as black
            colour = [0, 0, 0, 1]

        plot(feature[:, 0], feature[:, 1], 'o', markerfacecolor=tuple(colour),
             markeredgecolor='k', markersize=14)                                # Plot cluster
    title(_title)                                                               # Add title
    if save:                                                                    # If saving enabled, save figure
        savefig('results/cluster_plot.png')
    show(block=blocking)                                                        # Display figure
