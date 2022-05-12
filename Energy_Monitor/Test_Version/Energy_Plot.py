import linecache
import pandas as pd
import matplotlib.pyplot as plt
import os


# function getting the line index of the total charge string existing last time
def save_energy(str_path, str_keyword, str_csv_file_name):
    lst_f = []
    lst_e0 = []
    lst_de = []
    for idx in range(1, 3):
        if os.path.exists(str_path + "RUN" + str(idx)):
            str_path_vaspout = str_path + "RUN" + str(idx) + "\\vaspout"
            int_line_idx = 0
            int_energy_line_idx = 0
            with open(str_path_vaspout, 'r') as file:
                for line in file.readlines():
                    int_line_idx = int_line_idx + 1
                    if str_keyword in line.strip():
                        int_energy_line_idx = int_energy_line_idx + 1
                        msg = "'%s' string found in ionic step %d" % (str_keyword, int_energy_line_idx)
                        print(msg)
                        lst_f.append(float(linecache.getline(str_path_vaspout, int_line_idx).split()[2].replace("=", "")))
                        lst_e0.append(float(linecache.getline(str_path_vaspout, int_line_idx).split()[4].replace("=", "")))
                        lst_de.append(float(linecache.getline(str_path_vaspout, int_line_idx).split()[7].replace("=", "")))
            print(idx)
        else:
            break
    dic_data = {'f': lst_f, 'e0': lst_e0, 'de': lst_de}
    output = pd.DataFrame(dic_data)
    output.to_csv(str_csv_file_name, index=False, encoding='utf8')


def main():
    # Variables
    str_path = "S:\\projects\\04_LLTO_2N_Ov_ISIF_3\\LLTO-2N-5-OV-ISIF0-5-2\\STEP2\\"
    str_keyword = "F="
    str_csv_file_name = "../FE0dEdata.csv"
    # Save the total free energy into csv
    save_energy(str_path, str_keyword, str_csv_file_name)
    # Load the total free energy and plot
    lst_f = pd.read_csv(str_csv_file_name, usecols=["f"])
    int_ionic_steps = len(lst_f)
    plt.plot(range(0, int_ionic_steps), lst_f)
    plt.xlabel('ionic steps')
    plt.ylabel('total free energy (eV)')
    plt.show()


if __name__ == '__main__':
    main()
