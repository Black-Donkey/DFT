import linecache
import pandas as pd


# from pymatgen.core import Structure
# from prettytable import PrettyTable

# function getting the index of the first line for total charge
def get_total_charge_first_line(str_path, str_keyword):
    str_path_outcar = str_path + "OUTCAR"
    str_path_poscar = str_path + "POSCAR"
    int_total_lines = sum(1 for line in open(str_path_outcar))
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
    int_total_atoms = sum(map(int, linecache.getline(str_path_poscar, 6).split()))
    int_first_line = get_total_charge_first_line(str_path, "total charge")

    lst_s_charge = []
    lst_p_charge = []
    lst_d_charge = []
    lst_f_charge = []

    for idx in range(1, int_total_atoms):
        str_line = linecache.getline(str_path_outcar, int_first_line + idx - 1)
        flt_s_charge = (get_orbital_charge(str_line, 's'))
        flt_p_charge = (get_orbital_charge(str_line, 'p'))
        flt_d_charge = (get_orbital_charge(str_line, 'd'))
        flt_f_charge = (get_orbital_charge(str_line, 'f'))
        lst_s_charge.append(flt_s_charge)
        lst_p_charge.append(flt_p_charge)
        lst_d_charge.append(flt_d_charge)
        lst_f_charge.append(flt_f_charge)
    dic_data = {'s': lst_s_charge, 'p': lst_p_charge, 'd': lst_d_charge, 'f': lst_f_charge}
    output = pd.DataFrame(dic_data)
    output.to_csv("data.csv", index=False, encoding='utf8')


def main():
    # Variables
    str_path_groundstate = "S:\\projects\\05_LLTO_2N_Ov_ISIF_3_U\\LLTO-2N-5-OV-groundstate-MAG\\"
    #
    # int_La_idx = 108
    # int_Ti_idx = 128
    # int_Li_idx = 164
    # Read OUTCAR
    # f = open(str_path_groundstate)
    # f.close()
    # int_first_line = get_total_charge_first_line(str_path_groundstate, "total charge")
    # for idx in range(int_La_idx, int_Ti_idx):
    #     str_line = linecache.getline(str_path_groundstate, int_first_line + idx - 1)
    #     print(get_orbital_charge(str_line, 'd'))
    #     print(get_orbital_charge(str_line, 'f'))
    save_total_charge(str_path_groundstate)


if __name__ == '__main__':
    main()
