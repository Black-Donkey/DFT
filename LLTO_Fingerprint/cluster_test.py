from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
x, _ = make_blobs(n_samples=300, centers=5, cluster_std=.8)
plt.scatter(x[:, 0], x[:, 1])
plt.show()

aggloclust = AgglomerativeClustering(n_clusters=5).fit(x)
print(aggloclust)
AgglomerativeClustering(affinity='euclidean', compute_full_tree='auto',
                        connectivity=None, linkage='ward', memory=None, n_clusters=5,
                        )

labels = aggloclust.labels_

plt.scatter(x[:, 0], x[:, 1], c=labels)
plt.show()


cluster_model = AgglomerativeClustering(n_clusters=cluster_number).fit(data)
    print(cluster_model)
    labels = list(cluster_model.labels_)
    plt.scatter(data[:, 0], data[:, 1], c=labels)
    average_distance = 100
    for index_class in range(0, cluster_number):
        index_neighbor = [i for i, x in enumerate(labels) if x == index_class]
        average_distance = min(average_distance, np.mean([cluster_distance[i] for i in index_neighbor]))