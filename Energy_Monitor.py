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
        self.label01 = Label(self, text="Please enter directory", width=100, height=2, bg="black", fg="white",
                             font=("Arial", 15))
        self.label01.pack()

        # Entry
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()
        v1.set("please enter directory")
        print(self.entry01.get())

        # Button
        self.btn01 = Button(self, font=("Arial", 10), text="ok", width=6, height=3, command=self.generate_canvas)
        self.btn01.pack()

        # Canvas
        self.canvas = Canvas(self, width=300, height=200, bg="green")
        self.canvas.pack()
        # btn01.bind("<Button-1>", get_energy)

    def generate_canvas(self):
        print("get" + self.entry01.get())


def get_energy(self):
    self.canvas = Canvas(self, width=300, height=200, bg="green")


def main():
    root = Tk()
    root.title("ENERGY MONITOR")
    root.geometry("1000x400+300+300")
    Application(master=root)
    root.mainloop()


if __name__ == '__main__':
    main()
