def count_clusters(labels):
    return len(set(labels)) - (1 if -1 in labels else 0)  # Get number of clusters
