# importing tkinter for gui
import tkinter as tk
import pl2
bgColor = "#190f56"
purple = "#a400c3"
myFont = "consolas"
FontSize = 12
blue = "#27d8f2"
grey = "#DCD6D0"

def gui():
    global ei
    # creating window
    window = tk.Tk()
    window.geometry("720x700")
    # setting attribute
    #window.attributes('-fullscreen', True)
    window.title("ChaussTous")
    window.config(background=bgColor)

    # creating text label to display on window screen
    messages=["Nombre de chaussure demandé pour le premier mois :","Nombre de chaussure demandé pour le second mois :","Nombre de chaussure demandé pour le second mois :""Nombre de chaussure demandé pour le troisième mois :","Nombre de chaussure demandé pour le quatrième mois :","Nombre d’ouvrier disposé :","Salaire d’un ouvrier en dinars :","Nombre d’heures travaillé par un ouvrier pendant un mois :","Nombre d’heures supplémentaire maximale pendant un mois :","Prix d’une heure supplémentaire :","Temps pour faire une paire de chaussure : ","Frais de recrutement :","Frais de licenciement :" ]
    
    for i,c in enumerate(messages):
        tk.Label(window, text=c,              font=(myFont, FontSize),fg= "white" ,bg= bgColor).grid(row=i)                      
    
    ei=[]
    for i in range(0,12):
        e=tk.Entry(window)
        e.grid(row=i, column=1, pady=10)
        ei.append(e)

    def on_button_click():
        c1 =      int(ei[0].get())
        c2 =      int(ei[1].get())
        c3 =      int(ei[2].get())
        c4 =      int(ei[3].get())
        nbOuv =  int(ei[4].get())
        salaire =int(ei[5].get())
        nbH =    int(ei[6].get())
        nbSp =   int(ei[7].get())
        prixSup =int(ei[8].get())
        tmpCh =  int(ei[9].get())
        rec =    int(ei[10].get())
        lic =    int(ei[11].get())
        solution = pl2.solve(c1, c2, c3, c4, nbOuv, salaire, nbH, nbSp, prixSup, tmpCh, rec, lic)
        print(solution)
        label_message = tk.Label(window, text="", font=(myFont, FontSize), fg =blue, bg= bgColor)
        label_message.grid(row=13, column=0, columnspan=2, pady=10)
        label_message.config(text=solution)

    button = tk.Button(window, text="Montrer la stratégie optimale", font=(myFont, FontSize), bg= purple, fg= "white", command=on_button_click)
    
    button.grid(row=12, column=0, columnspan=2, pady=10)
    window.mainloop()

if __name__ == "__main__":
    gui()
