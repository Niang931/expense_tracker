import tkinter as tk
from tkinter import ttk

root = tk.Tk()
categories = ['Food', 'Transport', 'Social', 'Gym', 'Other']
label = tk.Label(root, text='Expense Tracker')
label.grid(row=0, columnspan=2)

# Setting the user input for expense
tk.Label(root, text='Amount').grid(row=1, column=0)
tk.Label(root, text='Description').grid(row=2, column=0)

amount = tk.Entry(root)
description = tk.Entry(root)
amount.grid(row=1, column=1)
description.grid(row=2, column=1)

tk.Label(root, text='Category').grid(row=3, column=0)
category = ttk.Combobox(
    root, values=categories, state='readonly'
)
category.grid(row=3, column=1)

button = tk.Button(root, text='Add Expense',
                   width=25)
button.grid(row=4, columnspan=2)

root.mainloop()
