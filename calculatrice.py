import tkinter as tk


CANVAS_WIDTH, CANVAS_HEIGHT = 900, 900

operande1 = 0

def rien():
    pass

def push_1():
    global operande1
    operande1 += 1
    return operande1



root = tk.Tk()

bouton_1 = tk.Button(root, text = "1", font = ("helvetica", "10"), width = 11, height = 7, command = push_1, bg = "red", relief = "groove")
bouton_1.grid(column = 0, row = 1)
bouton_2 = tk.Button(root, text = "2", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_2.grid(column = 1, row = 1)
bouton_3 = tk.Button(root, text = "3", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_3.grid(column = 2, row = 1)
bouton_4 = tk.Button(root, text = "4", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_4.grid(column = 0, row = 2)
bouton_5 = tk.Button(root, text = "5", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_5.grid(column = 1, row = 2)
bouton_6 = tk.Button(root, text = "6", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_6.grid(column = 2, row = 2)
bouton_7 = tk.Button(root, text = "7", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_7.grid(column = 0, row = 3)
bouton_8 = tk.Button(root, text = "8", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_8.grid(column = 1, row = 3)
bouton_9 = tk.Button(root, text = "9", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_9.grid(column = 2, row = 3)
bouton_0 = tk.Button(root, text = "0", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_0.grid(column = 1, row = 4)
bouton_plus = tk.Button(root, text = "+", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_plus.grid(column = 3, row = 1)
bouton_moins = tk.Button(root, text = "-", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_moins.grid(column = 3, row = 2)
bouton_fois = tk.Button(root, text = "x", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_fois.grid(column = 3, row = 3)
bouton_divise = tk.Button(root, text = "/", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_divise.grid(column = 3, row = 4)
bouton_virgule = tk.Button(root, text = ",", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_virgule.grid(column = 2, row = 4)
Ecran =tk.Label(root, text= "", font = ("helvetica", "10"), width = 48, height = 7,  bg = "black")
Ecran.grid(column = 0, row = 0, columnspan = 4)



root.mainloop()
