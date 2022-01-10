import linecache


# from pymatgen.core import Structure
# from prettytable import PrettyTable


def get_total_charge_first_line(str_path, str_keyword):
    int_total_lines = sum(1 for line in open(str_path))
    int_line_idx = 0
    msg = "[Error]: There is no result"
    with open(str_path, 'r') as file:
        for line in reversed(file.readlines()):
            int_line_idx = int_line_idx + 1
            if str_keyword in line.strip():
                msg = "'%s' string in line %d" % (str_keyword, int_total_lines - int_line_idx + 1)
                break
    print(msg)
    return int_total_lines - int_line_idx + 1 + 4


def get_orbital_charge(str_input, str_orbital):
    if str_orbital == 's':
        return float(str_input.split()[1])
    if str_orbital == 'p':
        return float(str_input.split()[2])
    if str_orbital == 'd':
        return float(str_input.split()[3])
    if str_orbital == 'f':
        return float(str_input.split()[4])


def main():
    # Variables
    str_path = "S:\\projects\\05_LLTO_2N_Ov_ISIF_3_U\\LLTO-2N-5-OV-groundstate-MAG\\OUTCAR"
    int_La_idx = 108
    int_Ti_idx = 128
    int_Li_idx = 164
    # Read OUTCAR
    f = open(str_path)
    f.close()
    int_line_idx = get_total_charge_first_line(str_path, "total charge")

    str_line = linecache.getline(str_path, int_line_idx + int_La_idx - 1)
    print(get_orbital_charge(str_line, 'd'))


if __name__ == '__main__':
    main()
