import linecache


# from pymatgen.core import Structure
# from prettytable import PrettyTable


def get_total_charge(str_path, str_keyword):
    num_lines = sum(1 for line in open(str_path))
    line_num = 0
    msg = "There is no result"
    with open(str_path, 'r') as file:
        for line in reversed(file.readlines()):
            line_num = line_num + 1
            if str_keyword in line.strip():
                msg = "'%s' string in line %d" % (str_keyword, num_lines - line_num + 1)
                break
    print(msg)
    return num_lines - line_num + 1


def get_d_orbital_charge(str_input):
    num = [float(s) for s in str_input.split(" ")]
    return num


def main():
    # Variables
    path = "S:\\projects\\05_LLTO_2N_Ov_ISIF_3_U\\LLTO-2N-5-OV-groundstate-MAG\\OUTCAR"
    f = open(path)
    f.close()
    line_num = get_total_charge(path, "total charge")
    theline = linecache.getline(path, line_num + 4)
    print(theline)
    # for lines in reversed(lines):
    #     if 'total charge' in lines:
    #         print(lines)
    #         break

    # groundstate_path = Structure.from_file(path + "LLTO-2N-5-OV-1-ISIF0-CONTCAR")

    # Make Table
    # pt = PrettyTable()
    # pt.field_names = ["Index", "Formula", "N+ Fraction", "Volume", "Lattice Angles", "Lattice Number"]
    #
    # pt.add_row(
    #     ["LLTO-2N-5-OV-1-ISIF0", s2.formula, s2.composition.get_atomic_fraction("N"), s2.volume, s2.lattice.angles,
    #      s2.lattice.abc])

    # print(pt)


if __name__ == '__main__':
    main()
