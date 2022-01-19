from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
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
        v1.set("S:\\projects\\04_LLTO_2N_Ov_ISIF_3\\LLTO-2N-5-OV-ISIF3-2\\STEP2\\vaspout")

        # Button
        self.btn01 = Button(self, font=("Arial", 11), text="ok", width=6, height=1, command=self.generate_canvas())
        self.btn01.grid(row=1, column=1)

        # Canvas
        self.canvas = Canvas(self, width=888, height=280, bg="green")
        self.canvas.grid(row=2, column=0, columnspan=2)
        # btn01.bind("<Button-1>", get_energy)

    def generate_canvas(self):
        path = self.entry01.get()
        print("get" + self.entry01.get())
        int_total_lines = sum(1 for _ in open(path))
        int_line_idx = 0
        str_keyword = "Energy"
        msg = "[Error]: There is no result"
        with open(path, 'r') as file:
            for line in reversed(file.readlines()):
                int_line_idx = int_line_idx + 1
                if str_keyword in line.strip():
                    int_first_line = int_total_lines - int_line_idx + 1 + 4
                    msg = "'%s' last string found in line %d" % (str_keyword, int_first_line)
                    break
        print(msg)


def main():
    root = Tk()
    root.title("ENERGY MONITOR")
    root.geometry("1000x400+300+300")
    Application(master=root)
    root.mainloop()


if __name__ == '__main__':
    main()
