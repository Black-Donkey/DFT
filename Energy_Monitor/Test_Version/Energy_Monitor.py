from tkinter import *
import linecache
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


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
                msg = "'%s' string found in ionic step %d" % (str_keyword, int_energy_line_idx)
                print(msg)
                lst_f.append(float(linecache.getline(str_path_vaspout, int_line_idx).split()[2].replace("=", "")))
                lst_e0.append(float(linecache.getline(str_path_vaspout, int_line_idx).split()[4].replace("=", "")))
                lst_de.append(float(linecache.getline(str_path_vaspout, int_line_idx).split()[7].replace("=", "")))
    dic_data = {'f': lst_f, 'e0': lst_e0, 'de': lst_de}
    output = pd.DataFrame(dic_data)
    output.to_csv(str_csv_file_name, index=False, encoding='utf8')


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.toolbar = None
        self.entry01 = None
        self.canvas = None
        self.btn01 = None
        self.label01 = None
        self.master = master
        self.pack()
        self.creat_widget()

    def creat_widget(self):
        # Label
        self.label01 = Label(self, text="Energy Monitor for Geometry Optimization", width=80, height=2, bg="black",
                             fg="white", font=("Arial", 15))
        self.label01.grid(row=0, column=0, columnspan=2)

        # Entry
        v1 = StringVar()
        self.entry01 = Entry(self, width=100, font=("Arial", 11), textvariable=v1)
        self.entry01.grid(row=1, column=0)
        v1.set("S:\\projects\\04_LLTO_2N_Ov_ISIF_3\\LLTO-2N-5-OV-ISIF3-2\\STEP2\\")

        # Button
        self.btn01 = Button(self, font=("Arial", 11), text="Plot", width=6, height=1, command=self.generate_canvas)
        self.btn01.grid(row=1, column=1)

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
        self.canvas = FigureCanvasTkAgg(fig, self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=20, y=80)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.master)
        self.toolbar.place(x=20, y=460)


def main():
    root = Tk()
    root.title("ENERGY MONITOR")
    root.geometry("900x500+300+200")
    Application(master=root)
    root.mainloop()


if __name__ == '__main__':
    main()
