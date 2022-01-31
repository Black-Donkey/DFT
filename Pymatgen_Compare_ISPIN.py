from pymatgen.core import Structure
from prettytable import PrettyTable


def main():
    path = "S:\\projects\\04_LLTO_2N_Ov_ISIF_3\\LLTO-2N-5-OV-ISIF0-1\\STEP2\\"
    s1 = Structure.from_file("LLTO-2N-5-OV-1.cif")
    s2 = Structure.from_file(path + "LLTO-2N-5-OV-1-ISIF0-CONTCAR")
    s3 = Structure.from_file("LLTO-2N-5-OV-1-ISIF3-CONTCAR")

    pt = PrettyTable()
    pt.field_names = ["Index", "Formula", "N+ Fraction", "Volume", "Lattice Angles", "Lattice Number"]
    pt.add_row(["LLTO-2N-5-OV-1", s1.formula, s1.composition.get_atomic_fraction("N"), s1.volume, s1.lattice.angles, s1.lattice.abc])
    pt.add_row(["LLTO-2N-5-OV-1-ISIF0", s2.formula, s2.composition.get_atomic_fraction("N"), s2.volume, s2.lattice.angles, s2.lattice.abc])
    pt.add_row(["LLTO-2N-5-OV-1-ISIF3", s3.formula, s3.composition.get_atomic_fraction("N"), s3.volume, s3.lattice.angles, s3.lattice.abc])
    print(pt)


if __name__ == '__main__':
    main()
