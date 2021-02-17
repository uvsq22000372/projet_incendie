#########################################
# groupe MPCI 3
# Lalasoa RATOVONDRANTO
# Ahmadou Bamba SOIM
# Maxime DANEVILLE
# Elias SAUVAGE
# https://github.com/uvsq22000372/projet_incendie
#########################################


import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500







root = tk.Tk()
root.title("Simulation incendie")

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black", relief = "raised", borderwidth = 5)
canvas.grid(column = 1, row = 1, rowspan = 3, columnspan = 2)

root.mainloop()