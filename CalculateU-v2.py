import linecache
import pandas as pd
# from prettytable import PrettyTable


# function getting the line index of the total charge string existing last time
def get_total_charge_first_line(str_path, str_keyword):
    str_path_outcar = str_path + "OUTCAR"
    int_total_lines = sum(1 for _ in open(str_path_outcar))
    int_line_idx = 0
    msg = "[Error]: There is no result"
    with open(str_path_outcar, 'r') as file:
        for line in reversed(file.readlines()):
            int_line_idx = int_line_idx + 1
            if str_keyword in line.strip():
                int_first_line = int_total_lines - int_line_idx + 1 + 4
                msg = "'%s' last string found in line %d" % (str_keyword, int_first_line)
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
def save_total_charge(str_path, str_csv_file_name):
    str_path_outcar = str_path + "OUTCAR"
    str_path_poscar = str_path + "POSCAR"
    # return dictionary
    lst_element = []
    lst_element_num = []
    int_element_num = 0
    int_atom_types = len(linecache.getline(str_path_poscar, 1).split())
    for idx in range(0, int_atom_types):
        lst_element.append(linecache.getline(str_path_poscar, 1).split()[idx])
        int_element_num = int_element_num + int(linecache.getline(str_path_poscar, 6).split()[idx])
        lst_element_num.append(int_element_num)
    print(lst_element)
    print(lst_element_num)
    int_total_atoms = sum(map(int, linecache.getline(str_path_poscar, 6).split()))
    dic_element = dict(zip(lst_element, lst_element_num))
    # save csv file
    int_first_line = get_total_charge_first_line(str_path, "total charge")
    lst_s_charge = []
    lst_p_charge = []
    lst_d_charge = []
    lst_f_charge = []
    for idx in range(0, int_total_atoms):
        str_line = linecache.getline(str_path_outcar, int_first_line + idx)
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
    output.to_csv(str_csv_file_name, index=False, encoding='utf8')
    return dic_element


def main():
    # Variables
    str_path_groundstate = "S:\\projects\\05_LLTO_2N_Ov_ISIF_3_U\\LLTO-2N-5-OV-groundstate-MAG\\"
    str_path_nsf = "S:\\projects\\05_LLTO_2N_Ov_ISIF_3_U\\LLTO-2N-5-OV-NSF\\"
    str_path_sf = "S:\\projects\\05_LLTO_2N_Ov_ISIF_3_U\\LLTO-2N-5-OV-SF\\"
    # Save csv files
    dic_element = save_total_charge(str_path_groundstate, "groundstate_total_charge.csv")
    save_total_charge(str_path_nsf, "NSCF_total_charge.csv")
    save_total_charge(str_path_sf, "SCF_total_charge.csv")
    # Load csv files
    flt_charge_groundstate = pd.read_csv('groundstate_total_charge.csv')
    flt_charge_nsf = pd.read_csv('NSCF_total_charge.csv')
    flt_charge_sf = pd.read_csv('SCF_total_charge.csv')
    # Calculate La
    u_la_d = []
    u_la_f = []
    for idx in range(dic_element['N'], dic_element['La']):
        # d orbital
        flt_delta_nsf = flt_charge_nsf.iloc[idx]["d"] - flt_charge_groundstate.iloc[idx]["d"]
        flt_delta_sf = flt_charge_sf.iloc[idx]["d"] - flt_charge_groundstate.iloc[idx]["d"]
        u_la_d.append(1 / flt_delta_sf - 1 / flt_delta_nsf)
        # f orbital
        flt_delta_nsf = flt_charge_nsf.iloc[idx]["f"] - flt_charge_groundstate.iloc[idx]["f"]
        flt_delta_sf = flt_charge_sf.iloc[idx]["f"] - flt_charge_groundstate.iloc[idx]["f"]
        u_la_f.append(1 / flt_delta_sf - 1 / flt_delta_nsf)
    dic_u_la = {'d': u_la_d, 'f': u_la_f}
    output = pd.DataFrame(dic_u_la)
    print(output)
    # Calculate Ti
    u_ti_d = []
    for idx in range(dic_element['La'], dic_element['Ti']):
        # d orbital
        flt_delta_nsf = flt_charge_nsf.iloc[idx]["d"] - flt_charge_groundstate.iloc[idx]["d"]
        flt_delta_sf = flt_charge_sf.iloc[idx]["d"] - flt_charge_groundstate.iloc[idx]["d"]
        u_ti_d.append(1 / flt_delta_sf - 1 / flt_delta_nsf)
    dic_u_ti = {'d': u_ti_d}
    output = pd.DataFrame(dic_u_ti)
    print(output)


if __name__ == '__main__':
    main()
