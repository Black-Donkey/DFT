from pymatgen.core import Structure
from pymatgen.io import cif, vasp
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def calculate_radius(other_element_index_list, int_cluster_number):
    # Generate training data
    distance_list = []
    for other_element_index in other_element_index_list:
        distance_list.append(
            [Structure.get_distance(structure_from_cif, o_index, other_element_index) for o_index in o_index_list])
    cluster_la = []
    for plot_index in range(0, len(other_element_index_list)):
        cluster_la.append(np.array([plot_index / 1e6] * len(distance_list[plot_index])).tolist())
    cluster_distance = sum(distance_list, [])
    cluster_la = sum(cluster_la, [])
    data = np.transpose(np.array([cluster_la, cluster_distance]))
    # Train kNN model
    model = KMeans(n_clusters=int_cluster_number).fit(data)
    labels = model.labels_
    center = model.cluster_centers_
    plt.scatter(data[:, 0], data[:, 1], c=labels)
    plt.scatter(center[:, 0], center[:, 1], c='red')
    plt.show()
    # Find the neighbor atoms and radius
    neighbor_class = np.argmin(center[:, 1])
    index_neighbor = [i for i, x in enumerate(labels) if x == neighbor_class]
    radius = max([cluster_distance[i] for i in index_neighbor])
    return radius


if __name__ == '__main__':
    coordinates = []
    species = []
    neighbor = []
    structure_from_cif = Structure.from_file("U2_N0_OV0_1.cif")
    for s in structure_from_cif:
        coordinates.append(s.frac_coords.tolist())
        species.append(s.specie.Z)
    o_index_list = np.where(np.array(species) == 8)[0].tolist()
    li_index_list = np.where(np.array(species) == 3)[0].tolist()
    la_index_list = np.where(np.array(species) == 57)[0].tolist()
    ti_index_list = np.where(np.array(species) == 22)[0].tolist()

    # Cluster the neighbor atoms
    radius_la = calculate_radius(la_index_list, 8)
    radius_li = calculate_radius(li_index_list, 15)
    neighbor_radius_la = structure_from_cif.get_all_neighbors(r=radius_la)
    neighbor_radius_li = structure_from_cif.get_all_neighbors(r=radius_li)

    la_class = []
    for a in range(0, len(neighbor_radius_la)):
        la_count = 0
        for b in range(0, len(neighbor_radius_la[a])):
            if neighbor_radius_la[a][b].species_string == "La":
                la_count += 1
        la_class.append(la_count)

    li_class = []
    for a in range(0, len(neighbor_radius_li)):
        li_count = 0
        for b in range(0, len(neighbor_radius_li[a])):
            if neighbor_radius_li[a][b].species_string == "Li":
                li_count += 1
        li_class.append(li_count)

    li_class = [i * 10 for i in li_class]
    fingerprint_list = np.sum([la_class, li_class], axis=0).tolist()
    unique_fingerprint_list = list(set(fingerprint_list))

    # structure_from_cif.replace()

    cif.CifWriter(structure_from_cif).write_file(filename="file.cif")
