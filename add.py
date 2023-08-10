import tkinter

class TestAvg:
    def __init__(self):
        self.window= tkinter.Tk()

        self.frame1 = tkinter.Frame(self.window)
        self.frame2 = tkinter.Frame(self.window)
        self.done = tkinter.Frame(self.window)
        self.button_frame = tkinter.Frame(self.window)

        self.frame1_label = tkinter.Label(self.frame1, text="number here ")
        self.frame1_entry = tkinter.Entry(self.frame1, width=10)
        self.frame1_label.pack(side="left")
        self.frame1_entry.pack(side="left")

        self.frame2_label = tkinter.Label(self.frame2, text="number here ")
        self.frame2_entry = tkinter.Entry(self.frame2, width=10)
        self.frame2_label.pack(side="left")
        self.frame2_entry.pack(side="left")

        self.result_label = tkinter.Label(self.done, text="total ")
        self.avg = tkinter.StringVar()
        self.done_label =tkinter.Label(self.done, textvariable=self.avg)
        self.result_label.pack(side="left")
        self.done_label.pack(side="left")

        self.calc_b = tkinter.Button(self.button_frame,text="average",command=self.calc2)
        self.quit_button = tkinter.Button(self.button_frame,text="quit",command=self.window.destroy)
        self.calc_b.pack(side="left")
        self.quit_button.pack(side="left")

        self.frame1.pack()
        self.frame2.pack()
        self.done.pack()
        self.button_frame.pack()
        tkinter.mainloop()
    def calc2(self):
        self.frame1 =float(self.frame1_entry.get())
        self.frame2 =float(self.frame2_entry.get())
        self.average= (self.frame1 + self.frame2)
        self.avg.set(self.average)

test_avg = TestAvg()
