import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

ROOT = tk.Tk()
ROOT.withdraw()  # hide naff extra window
ROOT.title('Please choose a date')


def pick_date_dialog():

    def print_sel():
        selected_date = (cal.get_date())
        print(selected_date)

    top = tk.Toplevel(ROOT)

    cal = Calendar(top,
                   font="Arial 10", background='silver',
                   foreground='white', selectmode='day')

    cal.grid()
    ttk.Button(top, text="OK", command=print_sel).grid()


pick_date_dialog()

ROOT.mainloop()
