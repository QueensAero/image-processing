from utilities.file_utilities import import_image
import matplotlib.pyplot as plt
from utilities.histogram import plot_histogram
from utilities.plots import display_image
from process import threshold_image
from numpy import nonzero, transpose, flip, zeros_like, linspace
from sklearn.cluster import DBSCAN


# Import image
im = import_image('test_1.png', gray_scale=True)
plot_histogram(im)


thresh_image = threshold_image(im, make_copy=True, percent=99.5)
display_image(im, 'Original image')
display_image(thresh_image, 'Threshold image')
features = nonzero(transpose(flip(flip(thresh_image, axis=1))))     # Get non-zero points


def cluster_points(features):
    db = DBSCAN(eps=10).fit(features)                                   # Perform clustering
    sample_mask = zeros_like(db.labels_, dtype=bool)                    # Generate mask
    sample_mask[db.core_sample_indices_] = True                         # Set indexes to true
    labels = db.labels_                                                 # Get labels

