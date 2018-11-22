# Clustering notes

## Code layout

### Import

The image is imported as a greyscale numpy array.

```
im = import_image('test_1.png', gray_scale=True)
```


### Get features

The features are taken from the image by thresholding, then taking all non-zero 
elements. *NOTE* all non-zero elements are transposed, putting them into an array 
of pairs (x, y).

```
thresh_image = threshold_image(im, make_copy=True, percent=99.5)
features = transpose(nonzero(thresh_image))
```


### Cluster

The clustering is done using the dbscan algorithm, that (effectively) associates all
points within a range (eps) of one another. The features provided (see *Get features*)
are given as an array of pairs.

```
# Cluster
clusters = DBSCAN(eps=10).fit(features)
```


### Generate masks and labels

The masks and labels are effectively categorizing the pairs of points into clusters, 
then assigning them unique IDs (labels). Colours are then generated for each of the 
labels (unique).

```
cluster_mask = zeros_like(clusters.labels_, dtype=bool)
cluster_mask[clusters.core_sample_indices_] = True
labels = clusters.labels_

unique_labels = set(labels)
colours = [cm.Spectral(each) for each in linspace(0, 1, len(unique_labels))]
```


### Plot image

The image is then plotted by taking each point cluster (based on colour) and plotting
them (again, each cluster getting its own colour).

```
figure('Clusters')
for k, col in zip(labels, colours):
    if k == -1:
        col = [0, 0, 0, 1]

    class_mask = (labels == k)
    coord = features[class_mask & cluster_mask]
    plot(coord[:, 0], coord[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=14)

    coord = features[class_mask & ~cluster_mask]
    plot(coord[:, 0], coord[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='b', markersize=6)

title('Cluster image')
show()
```