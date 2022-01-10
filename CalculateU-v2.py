import linecache
import pandas as pd


# from pymatgen.core import Structure
# from prettytable import PrettyTable

# function getting the index of the first line for total charge
def get_total_charge_first_line(str_path, str_keyword):
    str_path_outcar = str_path + "OUTCAR"
    str_path_poscar = str_path + "POSCAR"
    int_total_lines = sum(map(int, linecache.getline(str_path_poscar, 6).split()))
    # int_total_lines = sum(1 for line in open(str_path_outcar))
    int_line_idx = 0
    msg = "[Error]: There is no result"
    with open(str_path_outcar, 'r') as file:
        for line in reversed(file.readlines()):
            int_line_idx = int_line_idx + 1
            if str_keyword in line.strip():
                int_first_line = int_total_lines - int_line_idx + 1 + 4
                msg = "'%s' string in line %d" % (str_keyword, int_first_line)
                break
    print(msg)
    return int_first_line


# function getting the value for the specific orbital of the specific atom
def get_orbital_charge(str_input, str_orbital):
    if str_orbital == 's':
        return float(str_input.split()[1])
    if str_orbital == 'p':
        return float(str_input.split()[2])
    if str_orbital == 'd':
        return float(str_input.split()[3])
    if str_orbital == 'f':
        return float(str_input.split()[4])


# function saving the total charge data into csv file
def save_total_charge(str_path):
    str_path_outcar = str_path + "OUTCAR"
    str_path_poscar = str_path + "POSCAR"
    int_total_lines = sum(map(int, linecache.getline(str_path_poscar, 6).split()))
    int_first_line = get_total_charge_first_line(str_path_outcar, "total charge")
    for idx in range(1, int_total_lines):
        str_line = linecache.getline(str_path_outcar, int_first_line + idx - 1)
        flt_d_charge = (get_orbital_charge(str_line, 'd'))
        flt_f_charge = (get_orbital_charge(str_line, 'f'))
        list_row = [idx, flt_d_charge, flt_f_charge];


def main():
    # Variables
    str_path_groundstate = "S:\\projects\\05_LLTO_2N_Ov_ISIF_3_U\\LLTO-2N-5-OV-groundstate-MAG\\"
    str_path_NSF = "S:\\projects\\05_LLTO_2N_Ov_ISIF_3_U\\LLTO-2N-5-OV-NSF\\"
    str_path_SF = "S:\\projects\\05_LLTO_2N_Ov_ISIF_3_U\\LLTO-2N-5-OV-SF\\"
    int_La_idx = 108
    int_Ti_idx = 128
    int_Li_idx = 164
    # Read OUTCAR
    # f = open(str_path_groundstate)
    # f.close()
    int_first_line = get_total_charge_first_line(str_path_groundstate, "total charge")
    for idx in range(int_La_idx, int_Ti_idx):
        str_line = linecache.getline(str_path_groundstate, int_first_line + idx - 1)
        print(get_orbital_charge(str_line, 'd'))
        print(get_orbital_charge(str_line, 'f'))


if __name__ == '__main__':
    main()
