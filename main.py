import tkinter as tk
import pl2Inerface
import pl3Interface

bgColor = "#190f56"
purple = "#a400c3"
myFont = "consolas"
blue = "#27d8f2"

window = tk.Tk()

window.geometry("700x600")


window.config(background=bgColor)

label = tk.Label(window, text="Linear Problems Solver", font=(myFont, 30), fg=blue, bg= bgColor)
label.pack(pady=20)

problems = ["gestion optimale d'une zone agricole", 
            "gestion de la production", 
            "planification des besoins en ressources humaines",
            "choix d'implantation d'agences bancaires",
            "problème de positionnement",
            "problème de réseau"
            ]

# Define the button frame before using it
button_frame = tk.Frame(window, bg=bgColor)

# Pack the button frame with padding
button_frame.pack(pady=20)



buttons = []
for i in range(6):
    button = tk.Button(button_frame, text=problems[i], font=(myFont, 15), bg=purple, fg="white", width = 50)
    button.pack(pady=10) 
    buttons.append(button)

widest_button_width = max(button.winfo_reqwidth() for button in buttons)
    
# Center buttons horizontally
for button in buttons:
    button.pack_configure(side="top")

buttons[1]["command"] = pl2Inerface.gui
buttons[2]["command"] = pl3Interface.gui

window.mainloop()