import tkinter as tk
from time import sleep
from string import ascii_uppercase
from positionennemnt import solve as solvepl3
# import positionennemnt
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
    window.title("positionnement")
    window.config(background=bgColor)
    
    tk.Label(window, text="Donner le nomber de chambre et les nmbre de zone et le constraint de chaque chambre separe par vergule",font=(myFont, FontSize),fg= "white" ,bg= bgColor).grid(row=0)
    e=tk.Entry(window)
    e.grid(row=0, column=1, pady=10)
    def get_n():
        data=[int(i) for i in e.get().split(",")]
        n,nbrezone,constraint=data[0],data[1],data[2:]
        points=ascii_uppercase[:nbrezone]
        tk.Label(window, text="Donner les zones dont la frotiere commune abrite de chaque site  separee par vergule 1,2",font=(myFont, FontSize),fg= "white" ,bg= bgColor).grid(row=2)
        ei=[]
        for i,c in enumerate(points):
             tk.Label(window, text=f"Pour l'Antenne {c}: ",font=(myFont, FontSize),fg= "white" ,bg= bgColor).grid(row=3+i)
             ee=tk.Entry(window)
             ee.grid(row=i+3, column=1, pady=10)
             ei.append(ee)
        def get_solver():
            place_antene_acces=[[int(i) for i in j.get().split(",")] for j in ei]

            print(points,place_antene_acces,constraint,n)
            model=solvepl3(points,place_antene_acces,constraint,n)
            minim=model.objVal
            res=[]
            for var in model.getVars():
                if int(var.x)!=0:
                    res.append(var.VarName)
            final_message=f"Les plus efficasse est de positioner {minim} antenne en le position suivant :{','.join(res)}"
            tk.Label(window, text=final_message,font=(myFont, FontSize),fg= "white" ,bg= bgColor).grid(row=nbrezone+i)
        button2 = tk.Button(window, text="Montrer la position optimale", font=(myFont, FontSize), bg= purple, fg= "white",command=get_solver)
        button2.grid(row=nbrezone+4, column=0, columnspan=2, pady=10)

            


    button = tk.Button(window, text="confirmer", font=(myFont, FontSize), bg= purple, fg= "white", command=get_n)
    button.grid(row=1, column=0, columnspan=2, pady=10)
            
    # n=int(e.get())
    window.mainloop()




