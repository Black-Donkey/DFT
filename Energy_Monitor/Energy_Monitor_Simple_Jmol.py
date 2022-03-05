from tkinter import *
from tkinter import filedialog
import linecache
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import paramiko


# function getting the line index of the total charge string existing last time
def save_energy(str_path, str_keyword, str_csv_file_name):
    str_path_vaspout = str_path + "\\vaspout"
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
                msg = "'%s' string found in ionic step %d" % (str_keyword, int_energy_line_idx)
                print(msg)
                lst_f.append(float(linecache.getline(str_path_vaspout, int_line_idx).split()[2].replace("=", "")))
                lst_e0.append(float(linecache.getline(str_path_vaspout, int_line_idx).split()[4].replace("=", "")))
                lst_de.append(float(linecache.getline(str_path_vaspout, int_line_idx).split()[7].replace("=", "")))
    dic_data = {'f': lst_f, 'e0': lst_e0, 'de': lst_de}
    output = pd.DataFrame(dic_data)
    output.to_csv(str_csv_file_name, index=False, encoding='utf8')


def browse(self):
    filename = filedialog.askdirectory().replace('/', '\\')
    v1 = StringVar()
    self.entry01 = Entry(self, font=("Arial", 11), textvariable=v1)
    self.entry01.place(x=20, y=60, width=600, height=30)
    v1.set(filename)


def generate_canvas(self):
    str_path = self.entry01.get()
    print("get" + self.entry01.get())
    str_keyword = "F="
    str_csv_file_name = "../FE0dEdata.csv"
    # Save the total free energy into csv
    save_energy(str_path, str_keyword, str_csv_file_name)
    # Load the total free energy and plot
    lst_f = pd.read_csv(str_csv_file_name, usecols=["f"])
    int_ionic_steps = len(lst_f)

    fig = plt.figure(figsize=(6, 3.8))
    fig.add_subplot().plot(range(1, int_ionic_steps + 1), lst_f)
    plt.xlabel('ionic steps')
    plt.ylabel('total free energy (eV)')
    plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.15)
    canvas = FigureCanvasTkAgg(fig, self.master)
    canvas.draw()
    canvas.get_tk_widget().place(x=20, y=95)
    toolbar = NavigationToolbar2Tk(canvas, self.master)
    toolbar.place(x=18, y=480)


def check_this(self):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname='baigroup.duckdns.org', username='', password='')
    str_wsl_path = self.entry01.get().replace('S:', '~').replace('\\STEP2\\', '').replace('\\', '/')
    str_command = 'cd ' + str_wsl_path + ';shotgun check-this -s'
    print(str_command)
    stdin, stdout, stderr = client.exec_command(str_command)
    print(stdout.read().decode('utf-8'))
    client.close()


def main():
    root = Tk()
    root.title("ENERGY MONITOR")
    root.geometry("900x522+300+200")
    # Label
    root.label01 = Label(root, text="Energy Monitor for Geometry Optimization", width=78, height=2, bg="black",
                         fg="white", font=("Arial", 15))
    root.label01.place(x=20, y=5)

    # Entry
    v1 = StringVar()
    root.entry01 = Entry(root, font=("Arial", 11), textvariable=v1)
    root.entry01.place(x=20, y=60, width=600, height=30)
    v1.set("S:\\projects\\04_LLTO_2N_Ov_ISIF_3\\LLTO-2N-5-OV-ISIF3-2\\STEP2")

    # Canvas and Toolbar
    fig = plt.figure(figsize=(6, 3.8))
    plt.xlabel('ionic steps')
    plt.ylabel('total free energy (eV)')
    plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.15)
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.draw()
    canvas.get_tk_widget().place(x=20, y=95)
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.place(x=18, y=480)

    # Button Browse
    root.btn01 = Button(root, font=("Arial", 11), text="Browse", command=lambda: browse(root))
    root.btn01.place(x=630, y=60, width=85, height=30)
    # root.pathlabel = Label(root)

    # Button Check-this
    root.btn02 = Button(root, font=("Arial", 11), text="Check-this", command=lambda: check_this(root))
    root.btn02.place(x=720, y=60, width=100, height=30)

    # Button Plot
    root.btn03 = Button(root, font=("Arial", 11), text="Plot", command=lambda: generate_canvas(root))
    root.btn03.place(x=825, y=60, width=60, height=30)

    root.mainloop()


if __name__ == '__main__':
    main()
