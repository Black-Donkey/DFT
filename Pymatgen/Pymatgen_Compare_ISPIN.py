from pymatgen.core import Structure
from prettytable import PrettyTable


def main():
    path1 = "S:\\projects\\06_LLTO_ISPIN\\LLTO_1N_5_ISIF_3_ISPIN_1\\STEP2\\"
    path2 = "S:\\projects\\06_LLTO_ISPIN\\LLTO_1N_5_ISIF_3_ISPIN_2\\STEP2\\"
    s1 = Structure.from_file(path1 + "CONTCAR")
    s2 = Structure.from_file(path2 + "CONTCAR")

    pt = PrettyTable()
    pt.field_names = ["Index", "Formula", "N+ Fraction", "Volume", "Lattice Angles", "Lattice Number"]
    pt.add_row(["ISPIN1", s1.formula, s1.composition.get_atomic_fraction("N"), s1.volume, s1.lattice.angles, s1.lattice.abc])
    pt.add_row(["ISPIN2", s2.formula, s2.composition.get_atomic_fraction("N"), s2.volume, s2.lattice.angles, s2.lattice.abc])
    print(pt)


if __name__ == '__main__':
    main()
