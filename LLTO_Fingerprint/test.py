from pymatgen.core import Structure, Lattice
from prettytable import PrettyTable
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import where
from sklearn.cluster import KMeans

if __name__ == '__main__':
    coordinates = []
    species = []
    neighbor = []
    structure_from_cif = Structure.from_file("U2_N0_OV0_1.cif")
    for s in structure_from_cif:
        coordinates.append(s.frac_coords.tolist())
        species.append(s.specie.Z)
        # neighbor.append(s.get_neighbors(r=2))
    element = set(species)
    o_index_list = np.where(np.array(species) == 8)[0].tolist()
    li_index_list = np.where(np.array(species) == 3)[0].tolist()
    la_index_list = np.where(np.array(species) == 57)[0].tolist()
    ti_index_list = np.where(np.array(species) == 22)[0].tolist()

    distance_list = []
    for la_index in la_index_list:
        distance_list.append(
            [Structure.get_distance(structure_from_cif, o_index, la_index) for o_index in o_index_list])

    cluster_la = []

    for plot_index in range(0, len(la_index_list)):
        # plt.scatter(np.array([plot_index] * len(distance_list[plot_index])), distance_list[plot_index])
        cluster_la.append(np.array([plot_index / 1000] * len(distance_list[plot_index])).tolist())
    # plt.show()

    # Cluster the neighbor atoms
    cluster_number = 8
    cluster_distance = sum(distance_list, [])
    cluster_la = sum(cluster_la, [])
    data = np.transpose(np.array([cluster_la, cluster_distance]))
    cluster_model = KMeans(n_clusters=cluster_number).fit(data)
    labels = cluster_model.labels_
    center = cluster_model.cluster_centers_

    plt.scatter(data[:, 0], data[:, 1], c=labels)
    plt.scatter(center[:, 0], center[:, 1], c='red')
    plt.show()
    neighbor_class = np.argmin(center[:, 1])
    index_neighbor = [i for i, x in enumerate(labels) if x == neighbor_class]
    average_distance = max([cluster_distance[i] for i in index_neighbor])

    # neighbor = structure_from_cif.get_all_neighbors(r=3)
