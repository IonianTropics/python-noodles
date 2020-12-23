"""
Python Calculator
9/6/2020 - 5:09 pm
(Not really functional, just practice with tkinter)
"""

import math
import tkinter as tk

window = tk.Tk()
window.geometry('320x360')
window.title("Calcu-later")

scrn = tk.Label(window, font=("Segoe UI", 20), text=":)",
                width=0, anchor=tk.E, padx=1, pady=1,
                fg='black', bg='grey'
                ).grid(column=0, row=0, columnspan=6)

btnneg = tk.Button(window, text="-/+").grid(column=0, row=1)
btnsqrt = tk.Button(window, text="√‾").grid(column=1, row=1)
btnmod = tk.Button(window, text="%").grid(column=2, row=1)

btnmrc = tk.Button(window, text="MRC").grid(column=0, row=2)
btnmn = tk.Button(window, text="M-").grid(column=1, row=2)
btnmp = tk.Button(window, text="M+").grid(column=2, row=2)


def btn(n):
    c = abs(n-1) % 3
    r = math.floor(6 - 1 / 3 * n)
    tk.Button(window, text=str(n)).grid(column=c, row=r, ipady=12, ipadx=12)
    return 0


for i in range(10):
    btn(i)

btndiv = tk.Button(window, text="÷").grid(column=3, row=1, ipady=12, ipadx=12)
btnmp = tk.Button(window, text="×").grid(column=3, row=2, ipady=12, ipadx=12)
btnmns = tk.Button(window, text="-").grid(column=3, row=3, ipady=12, ipadx=12)
btnpls = tk.Button(window, text="+").grid(column=3, row=4, ipady=12, ipadx=12)
btneql = tk.Button(window, text="=").grid(column=3, row=5, rowspan=2, ipady=32, ipadx=12)

btnce = tk.Button(window, text="C").grid(column=0, row=6, ipady=12, ipadx=12)
btnfl = tk.Button(window, text=".").grid(column=2, row=6, ipady=12, ipadx=12)

window.mainloop()
