import linecache
import pandas as pd
# from prettytable import PrettyTable


# function getting the line index of the total charge string existing last time
def save_energy(str_path, str_keyword):
    str_path_vaspout = str_path + "vaspout"
    int_total_lines = sum(1 for _ in open(str_path_vaspout))
    int_line_idx = 0
    msg = "[Error]: There is no result"
    with open(str_path_vaspout, 'r') as file:
        for line in reversed(file.readlines()):
            int_line_idx = int_line_idx + 1
            if str_keyword in line.strip():
                int_first_line = int_total_lines - int_line_idx + 1 + 4
                msg = "'%s' last string found in line %d" % (str_keyword, int_first_line)
                break
    print(msg)
    return int_first_line


def main():
    # Variables
    str_path_groundstate = "S:\\projects\\05_LLTO_2N_Ov_ISIF_3_U\\LLTO-2N-5-OV-groundstate-MAG\\"
    str_path_nsf = "S:\\projects\\05_LLTO_2N_Ov_ISIF_3_U\\LLTO-2N-5-OV-NSF\\"
    str_path_sf = "S:\\projects\\05_LLTO_2N_Ov_ISIF_3_U\\LLTO-2N-5-OV-SF\\"
    save_energy()


if __name__ == '__main__':
    main()
