import tkinter as tk


CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

root = tk.Tk()

bouton_1 = tk.Button(root, text = "1", font = ("helvetica", "10"), command = , bg = "red", relief = "groove")
bouton_1.grid(column = 0, row = 0)
bouton_2 = tk.Button(root, text = "2", font = ("helvetica", "10"), command = , bg = "red", relief = "groove")
bouton_2.grid(column = 0, row = 1)
bouton_3 = tk.Button(root, text = "3", font = ("helvetica", "10"), command = , bg = "red", relief = "groove")
bouton_3.grid(column = 0, row = 2)
bouton_4 = tk.Button(root, text = "4", font = ("helvetica", "10"), command = , bg = "red", relief = "groove")
bouton_4.grid(column = 0, row = 3)
bouton_5 = tk.Button(root, text = "5", font = ("helvetica", "10"), command = , bg = "red", relief = "groove")
bouton_5.grid(column = 0, row = 0)
bouton_6 = tk.Button(root, text = "6", font = ("helvetica", "10"), command = , bg = "red", relief = "groove")
bouton_6.grid(column = 0, row = 1)
bouton_7 = tk.Button(root, text = "7", font = ("helvetica", "10"), command = , bg = "red", relief = "groove")
bouton_7.grid(column = 0, row = 2)
bouton_8 = tk.Button(root, text = "8", font = ("helvetica", "10"), command = , bg = "red", relief = "groove")
bouton_8.grid(column = 0, row = 3)
bouton_9 = tk.Button(root, text = "9", font = ("helvetica", "10"), command = , bg = "red", relief = "groove")
bouton_9.grid(column = 0, row = 3)
bouton_0 = tk.Button(root, text = "0", font = ("helvetica", "10"), command = , bg = "red", relief = "groove")
bouton_0.grid(column = 0, row = 3)

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "white", relief = "raised", borderwidth = 5)
canvas.grid(column = 3, row = 5, rowspan = 5)

root.mainloop()