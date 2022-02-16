from pymatgen.core import Structure, Lattice
from prettytable import PrettyTable
import pandas as pd
import matplotlib as plt

if __name__ == '__main__':
    coordinates = []
    species = []
    neighbor = []
    structure_from_cif = Structure.from_file("U2_N0_OV0_1.cif")
    for s in structure_from_cif:
        print(s)
        coordinates.append(s.frac_coords.tolist())
        species.append(s.specie.Z)
        # neighbor.append(s.get_neighbors(r=2))
    element = set(species)

    neighbor = structure_from_cif.get_all_neighbors(r=3)
    # ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
    #
    # ax.scatter(x[:10], y[:10], z[:10], c='y')  # 绘制数据点
    #
    # ax.set_zlabel('Z')  # 坐标轴
    # ax.set_ylabel('Y')
    # ax.set_xlabel('X')
    # plt.show()
