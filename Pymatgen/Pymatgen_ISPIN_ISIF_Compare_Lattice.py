from pymatgen.core import Structure
from prettytable import PrettyTable
import pandas as pd


def main():
    path1 = "S:\\projects\\07_LLTO_ISIF_ISPIN_DIFF\\01_LLTO_ISIF0_ISPIN1\\STEP2\\"
    path2 = "S:\\projects\\07_LLTO_ISIF_ISPIN_DIFF\\02_LLTO_ISIF0_ISPIN2\\STEP2\\"
    path3 = "S:\\projects\\07_LLTO_ISIF_ISPIN_DIFF\\03_LLTO_ISIF3_ISPIN1\\STEP2\\"
    path4 = "S:\\projects\\07_LLTO_ISIF_ISPIN_DIFF\\04_LLTO_ISIF3_ISPIN2\\STEP2\\"
    path5 = "S:\\projects\\07_LLTO_ISIF_ISPIN_DIFF\\05_N_LLTO_ISIF0_ISPIN1\\STEP2\\"
    path6 = "S:\\projects\\07_LLTO_ISIF_ISPIN_DIFF\\06_N_LLTO_ISIF0_ISPIN2\\STEP2\\"
    path7 = "S:\\projects\\07_LLTO_ISIF_ISPIN_DIFF\\07_N_LLTO_ISIF3_ISPIN1\\STEP2\\"
    path8 = "S:\\projects\\07_LLTO_ISIF_ISPIN_DIFF\\08_N_LLTO_ISIF3_ISPIN2\\STEP2\\"
    path9 = "S:\\projects\\07_LLTO_ISIF_ISPIN_DIFF\\09_N_LLTO_OV_ISIF0_ISPIN1\\STEP2\\"
    path10 = "S:\\projects\\07_LLTO_ISIF_ISPIN_DIFF\\10_N_LLTO_OV_ISIF0_ISPIN2\\STEP2\\"
    path11 = "S:\\projects\\07_LLTO_ISIF_ISPIN_DIFF\\11_N_LLTO_OV_ISIF3_ISPIN1\\STEP2\\"
    path12 = "S:\\projects\\07_LLTO_ISIF_ISPIN_DIFF\\12_N_LLTO_OV_ISIF3_ISPIN2\\STEP2\\"

    s1 = Structure.from_file(path1 + "CONTCAR")
    s2 = Structure.from_file(path2 + "CONTCAR")
    s3 = Structure.from_file(path3 + "CONTCAR")
    s4 = Structure.from_file(path4 + "CONTCAR")
    s5 = Structure.from_file(path5 + "CONTCAR")
    s6 = Structure.from_file(path6 + "CONTCAR")
    s7 = Structure.from_file(path7 + "CONTCAR")
    s8 = Structure.from_file(path8 + "CONTCAR")
    s9 = Structure.from_file(path9 + "CONTCAR")
    s10 = Structure.from_file(path10 + "CONTCAR")
    s11 = Structure.from_file(path11 + "CONTCAR")
    s12 = Structure.from_file(path12 + "CONTCAR")

    lst_index = ["01_LLTO_ISIF0_ISPIN1", "02_LLTO_ISIF0_ISPIN2", "03_LLTO_ISIF3_ISPIN1", "04_LLTO_ISIF3_ISPIN2",
                 "05_N_LLTO_ISIF0_ISPIN1", "06_N_LLTO_ISIF0_ISPIN2", "07_N_LLTO_ISIF3_ISPIN1", "08_N_LLTO_ISIF3_ISPIN2",
                 "09_N_LLTO_OV_ISIF0_ISPIN1", "10_N_LLTO_OV_ISIF0_ISPIN2", "11_N_LLTO_OV_ISIF3_ISPIN1",
                 "12_N_LLTO_OV_ISIF3_ISPIN2"]
    lst_formula = [s1.formula, s1.formula, s1.formula, s1.formula, s1.formula, s1.formula, s1.formula, s1.formula,
                   s1.formula, s1.formula, s1.formula, s1.formula]
    lst_n_fraction = [s1.composition.get_atomic_fraction("N"), s1.composition.get_atomic_fraction("N"),
                      s1.composition.get_atomic_fraction("N"), s1.composition.get_atomic_fraction("N"),
                      s1.composition.get_atomic_fraction("N"), s1.composition.get_atomic_fraction("N"),
                      s1.composition.get_atomic_fraction("N"), s1.composition.get_atomic_fraction("N"),
                      s1.composition.get_atomic_fraction("N"), s1.composition.get_atomic_fraction("N"),
                      s1.composition.get_atomic_fraction("N"), s1.composition.get_atomic_fraction("N")]
    lst_volume = [s1.volume, s1.volume, s1.volume, s1.volume, s1.volume, s1.volume, s1.volume, s1.volume, s1.volume,
                  s1.volume, s1.volume, s1.volume]
    lst_lattice_angles = [s1.lattice.angles, s1.lattice.angles, s1.lattice.angles, s1.lattice.angles,
                          s1.lattice.angles, s1.lattice.angles, s1.lattice.angles, s1.lattice.angles,
                          s1.lattice.angles, s1.lattice.angles, s1.lattice.angles, s1.lattice.angles]
    lst_lattice_number = [s1.lattice.abc, s1.lattice.abc, s1.lattice.abc, s1.lattice.abc, s1.lattice.abc,
                          s1.lattice.abc, s1.lattice.abc, s1.lattice.abc, s1.lattice.abc, s1.lattice.abc,
                          s1.lattice.abc, s1.lattice.abc]
    lst_total_energy = [-737.67773557, -737.67773612, -737.47148272, -737.85826126, -735.90418046, -736.19720729,
                        -735.74980860, -736.01665789, -1466.09809181, -1466.09764283, -1466.44056007, -1465.77935593]
    dic_data = {"Index": lst_index, "Formula": lst_formula, "N+ Fraction": lst_n_fraction, "Volume": lst_volume,
                "Lattice Angles": lst_lattice_angles, "Lattice Number": lst_lattice_number, "Energy": lst_total_energy}
    output = pd.DataFrame(dic_data)
    output.to_csv("data.csv", index=False, encoding='utf8')

    pt = PrettyTable()
    pt.field_names = ["Index", "Formula", "N+ Fraction", "Volume", "Lattice Angles", "Lattice Number"]
    pt.add_row(["01_LLTO_ISIF0_ISPIN1", s1.formula, s1.composition.get_atomic_fraction("N"), s1.volume,
                s1.lattice.angles, s1.lattice.abc])
    pt.add_row(["02_LLTO_ISIF0_ISPIN2", s2.formula, s2.composition.get_atomic_fraction("N"), s2.volume,
                s2.lattice.angles, s2.lattice.abc])
    pt.add_row(["03_LLTO_ISIF3_ISPIN1", s3.formula, s3.composition.get_atomic_fraction("N"), s3.volume,
                s3.lattice.angles, s3.lattice.abc])
    pt.add_row(["04_LLTO_ISIF3_ISPIN2", s4.formula, s4.composition.get_atomic_fraction("N"), s4.volume,
                s4.lattice.angles, s4.lattice.abc])
    pt.add_row(["05_N_LLTO_ISIF0_ISPIN1", s5.formula, s5.composition.get_atomic_fraction("N"), s5.volume,
                s5.lattice.angles, s5.lattice.abc])
    pt.add_row(["06_N_LLTO_ISIF0_ISPIN2", s6.formula, s6.composition.get_atomic_fraction("N"), s6.volume,
                s6.lattice.angles, s6.lattice.abc])
    pt.add_row(["07_N_LLTO_ISIF3_ISPIN1", s7.formula, s7.composition.get_atomic_fraction("N"), s7.volume,
                s7.lattice.angles, s7.lattice.abc])
    pt.add_row(["08_N_LLTO_ISIF3_ISPIN2", s8.formula, s8.composition.get_atomic_fraction("N"), s8.volume,
                s8.lattice.angles, s8.lattice.abc])
    pt.add_row(["09_N_LLTO_OV_ISIF0_ISPIN1", s9.formula, s9.composition.get_atomic_fraction("N"), s9.volume,
                s9.lattice.angles, s9.lattice.abc])
    pt.add_row(["10_N_LLTO_OV_ISIF0_ISPIN2", s10.formula, s10.composition.get_atomic_fraction("N"), s10.volume,
                s10.lattice.angles, s10.lattice.abc])
    pt.add_row(["11_N_LLTO_OV_ISIF3_ISPIN1", s11.formula, s11.composition.get_atomic_fraction("N"), s11.volume,
                s11.lattice.angles, s11.lattice.abc])
    pt.add_row(["12_N_LLTO_OV_ISIF3_ISPIN2", s12.formula, s12.composition.get_atomic_fraction("N"), s12.volume,
                s12.lattice.angles, s12.lattice.abc])
    print(pt)


if __name__ == '__main__':
    main()
