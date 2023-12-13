# importing tkinter for gui
import tkinter as tk
import pl3
bgColor = "#190f56"
purple = "#a400c3"
myFont = "consolas"
FontSize = 12
blue = "#27d8f2"
grey = "#DCD6D0"

def gui():
    # creating window
    window = tk.Tk()
    window.geometry("650x600")
    # setting attribute
    #window.attributes('-fullscreen', True)
    window.title("ChaussTous")
    window.config(background=bgColor)

    # creating text label to display on window screen

    tk.Label(window, text="Nombre d’employés minimuim requis pour Lundi :"   ,
    tk.Label(window, text="Nombre d’employés minimuim requis pour Mardi :"   ,
    tk.Label(window, text="Nombre d’employés minimuim requis pour Mercredi :",
    tk.Label(window, text="Nombre d’employés minimuim requis pour Jeudi :"   ,
    tk.Label(window, text="Nombre d’employés minimuim requis pour Vendredi :",
    tk.Label(window, text="Nombre d’employés minimuim requis pour Samedi :"  ,
    tk.Label(window, text="Nombre d’employés minimuim requis pour Dimanche :",
    e1 = tk.Entry(window)
    e2 = tk.Entry(window)
    e3 = tk.Entry(window)
    e4 = tk.Entry(window)
    e5 = tk.Entry(window)
    e6 = tk.Entry(window)
    e7 = tk.Entry(window)
    e1.grid(row=0, column=1, pady=10)
    e2.grid(row=1, column=1, pady=10)
    e3.grid(row=2, column=1, pady=10)
    e4.grid(row=3, column=1, pady=10)
    e5.grid(row=4, column=1, pady=10)
    e6.grid(row=5, column=1, pady=10)
    e7.grid(row=6, column=1, pady=10)
    def on_button_click():
        D1 = int(e1.get())
        D2 = int(e2.get())
        D3 = int(e3.get())
        D4 = int(e4.get())
        D5 = int(e5.get())
        D6 = int(e6.get())
        D7 = int(e7.get())
        solution = pl3.solve(D1,D2,D3,D4,D5,D6,D7)
        print(solution)
        label_message = tk.Label(window, text="", font=(myFont, FontSize), fg =blue, bg= bgColor)
        label_message.grid(row=13, column=0, columnspan=2, pady=10)
        label_message.config(text=solution)

    button = tk.Button(window, text="Montrer la stratégie optimale", font=(myFont, FontSize), bg= purple, fg= "white", command=on_button_click)
    button.grid(row=12, column=0, columnspan=2, pady=10)
    window.mainloop()

gui()
