from utilities.file_utilities import import_image
from process import threshold_image
from numpy import nonzero, transpose, flip
from cluster import cluster_points, make_mask
from utilities.plots import plot_clusters
from utilities.utilities import count_clusters
# Script to import test image then threshold and cluster points

# Import image
im = import_image('test_1.png', gray_scale=True)
thresh_image = threshold_image(im, make_copy=True, percent=99.5)

# Get features
features = transpose(nonzero(transpose(flip(flip(thresh_image, axis=1)))))     # Get non-zero points

# Cluster image
cluster_sets, labels = cluster_points(features)
print('Number of clusters: ', count_clusters(labels))

# Make masks
centers, masks = make_mask(cluster_sets)

# Plot clusters
plot_clusters(cluster_sets, labels, centers=centers, masks=masks)

