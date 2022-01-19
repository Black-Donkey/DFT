import linecache
import pandas as pd


# function getting the line index of the total charge string existing last time
def save_energy(str_path, str_keyword, str_csv_file_name):
    str_path_vaspout = str_path + "vaspout"
    int_line_idx = 0
    int_energy_line_idx = 0
    lst_f = []
    lst_e0 = []
    lst_de = []
    with open(str_path_vaspout, 'r') as file:
        for line in file.readlines():
            int_line_idx = int_line_idx + 1
            if str_keyword in line.strip():
                int_energy_line_idx = int_energy_line_idx + 1
                msg = "'%s' last string found in ionic step %d" % (str_keyword, int_energy_line_idx)
                print(msg)
                lst_f.append(float(linecache.getline(str_path_vaspout, int_line_idx).split()[2].replace("=", "")))
                lst_e0.append(float(linecache.getline(str_path_vaspout, int_line_idx).split()[4].replace("=", "")))
                lst_de.append(float(linecache.getline(str_path_vaspout, int_line_idx).split()[7].replace("=", "")))
    dic_data = {'f': lst_f, 'e0': lst_e0, 'de': lst_de}
    output = pd.DataFrame(dic_data)
    output.to_csv(str_csv_file_name, index=False, encoding='utf8')


def main():
    # Variables
    str_path = "S:\\projects\\04_LLTO_2N_Ov_ISIF_3\\LLTO-2N-5-OV-ISIF3-2\\STEP2\\"
    str_keyword = "F="
    str_csv_file_name = "FE0dEdata.csv"
    # Save the total free energy into csv
    save_energy(str_path, str_keyword, str_csv_file_name)
    # Load the total free energy and plot
    flt_charge_groundstate = pd.read_csv('groundstate_total_charge.csv')

if __name__ == '__main__':
    main()
