from pymatgen.core import Structure, Lattice
from prettytable import PrettyTable
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
        distance_list.append([Structure.get_distance(structure_from_cif, o_index, la_index) for o_index in o_index_list])

    for la_index in la_index_list:
        plt.scatter(np.array([la_index]*len(distance_list[la_index])), distance_list[la_index])
    plt.show()

    neighbor = structure_from_cif.get_all_neighbors(r=3)
    # ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
    #
    # ax.scatter(x[:10], y[:10], z[:10], c='y')  # 绘制数据点
    #
    # ax.set_zlabel('Z')  # 坐标轴
    # ax.set_ylabel('Y')
    # ax.set_xlabel('X')
    # plt.show()
