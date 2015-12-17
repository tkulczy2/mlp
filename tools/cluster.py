__author__ = 'theodor'

from sklearn.cluster import KMeans, MiniBatchKMeans, MeanShift, AgglomerativeClustering, DBSCAN, estimate_bandwidth

def cluster():
    """ This function has not been tested/does not work

    """



    # The following bandwidth can be automatically detected using
    bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(X)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)