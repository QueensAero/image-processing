from numpy import zeros_like, zeros, mean
from sklearn.cluster import DBSCAN
from scipy.spatial import ConvexHull


def cluster_points(features):
    db = DBSCAN(eps=10).fit(features)                   # Perform clustering
    sample_mask = zeros_like(db.labels_, dtype=bool)    # Generate mask
    sample_mask[db.core_sample_indices_] = True         # Set indexes to true
    labels = db.labels_                                 # Get labels
    unique_labels = set(labels)                         # Make set of unique labels

    cluster_sets = []                                   # Initialize list of clusters
    for label in unique_labels:                         # For each cluster
        cluster_sets.append(features[labels == label])  # Add points within to cluster

    return cluster_sets, labels


# Function to calculate cluster masks
def make_mask(clusters):
    centers = zeros(len(clusters), dtype=(int, 2))      # Calculate centers of mass
    masks = []                                          # Initialize array of masks

    for i, cluster in enumerate(clusters):              # For each cluster
        centers[i] = mean(cluster, axis=0)              # Calculate center
        masks.append(ConvexHull(cluster))               # Calculate mask

    return centers, masks
