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
    window.geometry("750x550")
    # setting attribute
    #window.attributes('-fullscreen', True)
    window.title("Planification des besoins en ressources humaines")
    window.config(background=bgColor)

    # creating text label to display on window screen
    messages=["Nombre d’employés minimuim requis pour Lundi :"   ,"Nombre d’employés minimuim requis pour Mardi :"   ,"Nombre d’employés minimuim requis pour Mercredi :","Nombre d’employés minimuim requis pour Jeudi :"   ,"Nombre d’employés minimuim requis pour Vendredi :","Nombre d’employés minimuim requis pour Samedi :"  ,"Nombre d’employés minimuim requis pour Dimanche :"]
    ei=[]
    for i,c in enumerate(messages):
        tk.Label(window, text=c,              font=(myFont, FontSize),fg= "white" ,bg= bgColor).grid(row=i)                      
    ei=[]
    for i in range(0,7):
        e=tk.Entry(window)
        e.grid(row=i, column=1, pady=10)
        ei.append(e)
    label_message = tk.Label(window, text="", font=(myFont, FontSize), fg =blue, bg= bgColor)
    label_message.grid(row=13, column=0, columnspan=2, pady=10)
    
    def on_button_click():
        D1 = int(ei[0].get())
        D2 = int(ei[1].get())
        D3 = int(ei[2].get())
        D4 = int(ei[3].get())
        D5 = int(ei[4].get())
        D6 = int(ei[5].get())
        D7 = int(ei[6].get())
        solution = pl3.solve(D1,D2,D3,D4,D5,D6,D7)
        print(solution)
        label_message.config(text=solution)

    button = tk.Button(window, text="Montrer la stratégie optimale", font=(myFont, FontSize), bg= purple, fg= "white", command=on_button_click)
    button.grid(row=12, column=0, columnspan=2, pady=10)
    window.mainloop()
if __name__ == "__main__":
    gui()
