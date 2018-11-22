from numpy import zeros_like
from sklearn.cluster import DBSCAN


def cluster_points(features):
    db = DBSCAN(eps=10).fit(features)                                   # Perform clustering
    sample_mask = zeros_like(db.labels_, dtype=bool)                    # Generate mask
    sample_mask[db.core_sample_indices_] = True                         # Set indexes to true
    labels = db.labels_                                                 # Get labels
    unique_labels = set(labels)

    cluster_sets = []
    for label in unique_labels:
        cluster_sets.append(features[labels == label])

    return cluster_sets, labels
