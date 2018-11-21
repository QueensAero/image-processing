from utilities.file_utilities import import_image
import matplotlib.pyplot as plt
from utilities.histogram import plot_histogram
from utilities.plots import display_image
from process import threshold_image
from numpy import nonzero, transpose, flip, zeros_like, linspace
from sklearn.cluster import DBSCAN


# Import image
im = import_image('test_1.png', gray_scale=True)

# plot_histogram(im)

thresh_image = threshold_image(im, make_copy=True, percent=99.5)
# display_image(im, 'Original image')
# display_image(thresh_image, 'Threshold image')

# Get features
features = nonzero(transpose(flip(flip(thresh_image, axis=1))))     # Get non-zero points
feature_points = transpose(features)                                # Get points as array of tuples

db = DBSCAN(eps=10).fit(feature_points)                                   # Perform clustering
sample_mask = zeros_like(db.labels_, dtype=bool)                    # Generate mask
sample_mask[db.core_sample_indices_] = True                         # Set indexes to true
labels = db.labels_                                                 # Get labels

num_clusters = len(set(labels)) - (1 if -1 in labels else 0)        # Get number of clusters
print('Estimated num of clusters', num_clusters)


plt.figure('without anything')                                      # Initialize plot of points
plt.scatter(features[0], features[1])                               # Plot features
# plt.show()

unique_labs = set(labels)
colours = [plt.cm.Spectral(each) for each in linspace(0, 1, len(unique_labs))]

plt.figure('Clusters')
for k, col in zip(unique_labs, colours):
    if k == -1:
        col = [0, 0, 0, 1]

    class_mask = (labels == k)
    coord = feature_points[class_mask & sample_mask]
    plt.plot(coord[:, 0], coord[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=14)

    coord = feature_points[class_mask & ~sample_mask]
    plt.plot(coord[:, 0], coord[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='b', markersize=6)

plt.title('Cluster image')
plt.show()
