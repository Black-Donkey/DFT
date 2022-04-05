from pymatgen.core import Structure
from pymatgen.io import cif
import numpy as np
import matplotlib.pyplot as plt


def main():
    input_path = "S:\\projects\\12_LLTO_U2_N0_OV1\\LLTO_U2_N0_OV1_2\\STEP2"
    structure_from_cif = Structure.from_file(input_path)
    species = [s.specie.Z for s in structure_from_cif]
    o_index_list = np.where(np.array(species) == 8)[0].tolist()
    li_index_list = np.where(np.array(species) == 3)[0].tolist()
    la_index_list = np.where(np.array(species) == 57)[0].tolist()
    ti_index_list = np.where(np.array(species) == 22)[0].tolist()
