import tkinter as tk


CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

root = tk.Tk()

def Affichage():

    pass

bouton_1 = tk.Button(root, text = "1", font = ("helvetica", "10"), padx = 20, pady = 20,   bg = "red", relief = "groove")
bouton_1.grid(column = 0, row = 1)
bouton_2 = tk.Button(root, text = "2", font = ("helvetica", "10"), padx = 20, pady = 20,  bg = "red", relief = "groove")
bouton_2.grid(column = 1, row = 1)
bouton_3 = tk.Button(root, text = "3", font = ("helvetica", "10"), padx = 20, pady = 20,   bg = "red", relief = "groove")
bouton_3.grid(column = 2, row = 1)
bouton_4 = tk.Button(root, text = "4", font = ("helvetica", "10"), padx = 20, pady = 20,   bg = "red", relief = "groove")
bouton_4.grid(column = 0, row = 2)
bouton_5 = tk.Button(root, text = "5", font = ("helvetica", "10"), padx = 20, pady = 20,  bg = "red", relief = "groove")
bouton_5.grid(column = 1, row = 2)
bouton_6 = tk.Button(root, text = "6", font = ("helvetica", "10"), padx = 20, pady = 20, bg = "red", relief = "groove")
bouton_6.grid(column = 2, row = 2)
bouton_7 = tk.Button(root, text = "7", font = ("helvetica", "10"), padx = 20, pady = 20, bg = "red", relief = "groove")
bouton_7.grid(column = 0, row = 3)
bouton_8 = tk.Button(root, text = "8", font = ("helvetica", "10"), padx = 20, pady = 20,  bg = "red", relief = "groove")
bouton_8.grid(column = 1, row = 3)
bouton_9 = tk.Button(root, text = "9", font = ("helvetica", "10"), padx = 20, pady = 20,  bg = "red", relief = "groove")
bouton_9.grid(column = 2, row = 3)
bouton_0 = tk.Button(root, text = "0", font = ("helvetica", "10"), padx = 20, pady = 20,  bg = "red", relief = "groove")
bouton_0.grid(column = 1, row = 4)
Ecran =tk.Label(root, text= "", font = ("helvetica", "10"), padx = 85, pady = 20,   bg = "black", relief = "groove" )
Ecran.grid(column = 0, row = 0, columnspan = 3)
root.mainloop()
