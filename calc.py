import tkinter as tk 

window = tk.Tk()

label_calc_result = tk.Label(master=window, text=0, width=30, height=3)

label_calc_result.grid(row=0, column=0)

window.mainloop()
