from matplotlib.pyplot import figure, imshow, show, title, plot, cm, scatter, savefig
from numpy import linspace, array


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
def plot_clusters(feature_sets, labels, _title='Clustered image', blocking=True, save=True, centers=None, masks=None):
    figure(_title)                                                              # Create new figure
    colours = [cm.Spectral(each) for each in
               linspace(0, 1, len(feature_sets))]                               # Generate set of colours

    for i, (label, colour, feature) in enumerate(zip(labels, colours, feature_sets)):           # For each cluster
        if label == -1:                                                         # If noise plot as black
            colour = [0, 0, 0, 1]

        if masks is None:
            plot(feature[:, 0], feature[:, 1], 'o', markerfacecolor=tuple(colour),
                 markeredgecolor='k', markersize=14)                                # Plot cluster

        if masks is not None:
            plot(feature[masks[i].vertices, 0], feature[masks[i].vertices, 1],
                 color=tuple(colour), linewidth=2)                                  # Plot most of hull
            last = len(masks[i].vertices) - 1                                       # Calculate length of hull points
            ret_path = array([feature[masks[i].vertices[last]],
                              feature[masks[i].vertices[0]]])                       # Calculate last edge of hull

            plot(ret_path[:, 0], ret_path[:, 1], color=tuple(colour), linewidth=2)  # Plot last edge of hull

        if centers is not None:
            plot(centers[i, 0], centers[i, 1], 'o', markerfacecolor=tuple(colour),
                 markeredgecolor='k', markersize=14)                                # Plot centers of mass

    title(_title)                                                               # Add title
    if save:                                                                    # If saving enabled, save figure
        savefig('results/cluster_plot.png')
    show(block=blocking)                                                        # Display figure
