from pymatgen.core import Structure
from pymatgen.io import cif
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def calculate_radius(structure, list_o_index, list_neighbor_index, int_cluster_number):
    # Generate training data
    distance_list = []
    for neighbor_index in list_neighbor_index:
        distance_list.append([Structure.get_distance(structure, o_index, neighbor_index) for o_index in list_o_index])
    cluster = []
    for plot_index in range(0, len(list_neighbor_index)):
        cluster.append(np.array([plot_index / 1e6] * len(distance_list[plot_index])).tolist())
    cluster_distance = sum(distance_list, [])
    cluster = sum(cluster, [])
    data = np.transpose(np.array([cluster, cluster_distance]))

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


def main():
    input_path = "U2_N2_OV0.cif"
    structure_from_cif = Structure.from_file(input_path)
    species = [s.specie.Z for s in structure_from_cif]
    li_index_list = np.where(np.array(species) == 3)[0].tolist()
    la_index_list = np.where(np.array(species) == 57)[0].tolist()
    ti_index_list = np.where(np.array(species) == 22)[0].tolist()
    n_index_list = np.where(np.array(species) == 7)[0].tolist()
    o_index_list = np.where(np.array(species) == 8)[0].tolist()

    # Calculate radius for neighbor elements
    radius_la = calculate_radius(structure_from_cif, o_index_list, la_index_list, 8)
    radius_li = calculate_radius(structure_from_cif, o_index_list, li_index_list, 15)
    radius_n = calculate_radius(structure_from_cif, o_index_list, n_index_list, 10)

    # Calculate distances for all neighbor elements
    neighbor_radius_la = structure_from_cif.get_all_neighbors(r=radius_la)
    neighbor_radius_li = structure_from_cif.get_all_neighbors(r=radius_li)
    neighbor_radius_n = structure_from_cif.get_all_neighbors(r=radius_n)
    del neighbor_radius_la[0:o_index_list[0]]
    del neighbor_radius_li[0:o_index_list[0]]
    del neighbor_radius_n[0:o_index_list[0]]

    # Count neighbor elements
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
    n_class = []
    for a in range(0, len(neighbor_radius_n)):
        n_count = 0
        for b in range(0, len(neighbor_radius_n[a])):
            if neighbor_radius_n[a][b].species_string == "N":
                n_count += 1
        n_class.append(n_count)
    n_class = [i * 100 for i in n_class]

    # Generate ID (fingerprint) for each oxygen
    fingerprint_list = list(np.sum([la_class, li_class, n_class], axis=0))
    unique_fingerprint_list = list(set(fingerprint_list))

    # structure_from_cif.replace()
    output_path = "U2_N2_OV1"
    for i in range(0, len(unique_fingerprint_list)):
        file_index = output_path + "_" + str(i) + ".cif"
        substitute_index = fingerprint_list.index(unique_fingerprint_list[i]) + o_index_list[0]
        structure_from_cif.replace(i=substitute_index, species="Al")
        cif.CifWriter(structure_from_cif).write_file(filename=file_index)
        structure_from_cif.replace(i=substitute_index, species="O")
        structure_from_cif_ov = Structure.from_file(file_index)
        structure_from_cif_ov.remove_species(species=["Al"])
        cif.CifWriter(structure_from_cif_ov).write_file(filename=file_index)

    for item in set(fingerprint_list):
        print("fingerprint %d has found %d" % (item, fingerprint_list.count(item)))


if __name__ == '__main__':
    main()
