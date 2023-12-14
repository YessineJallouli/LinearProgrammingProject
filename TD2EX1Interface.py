import tkinter as tk
from time import sleep
from string import ascii_uppercase
from Implimentation_agence import solve as solvepl2
# import positionennemnt
bgColor = "#190f56"
purple = "#a400c3"
myFont = "consolas"
FontSize = 12
blue = "#27d8f2"
grey = "#DCD6D0"

def gui():
    n=0
    # creating window
    window = tk.Tk()
    window.geometry("850x800")
    # setting attribute
    #window.attributes('-fullscreen', True)
    window.title("Positionnement")
    window.config(background=bgColor)
    
    tk.Label(window, text="Donner Nbre de region,a,b,c,K,D,B separe par vergule",font=(myFont, FontSize),fg= "white" ,bg= bgColor).grid(row=0)
    e=tk.Entry(window)
    e.grid(row=0, column=1, pady=10)
    def get_n():
        data=[int(i) for i in e.get().split(",")]
        n,a,b,cc,K,D,B=data[0],data[1],data[2],data[3],data[4],data[5],data[6]
        tk.Label(window, text="Donner le poulation de chaque region en millers les régions voisine ",font=(myFont, FontSize),fg= "white" ,bg= bgColor).grid(row=2)
        ei=[]
        for i in range(1,n+1):
             tk.Label(window, text=f"Pour le Region{i}: ",font=(myFont, FontSize),fg= "white" ,bg= bgColor).grid(row=3+i)
             ee=tk.Entry(window)
             ee.grid(row=i+3, column=1, pady=10)
             ei.append(ee)
        def get_solver():
            A=[[0]*n for i in range(n)]
            data=[[int(i) for i in j.get().split(",")] for j in ei]

            population=[i[0] for i in data]
            for i,c in enumerate(data):
                c=c[1:]
                for j in c:
                    A[i][j-1]=1
            result=solvepl2(a,b,cc,A,K,D,B,population,n)
            
            final_message="Les plus efficasse  model est atteint avec un nombre de client  " +result
            tk.Label(window, text=final_message,font=(myFont, FontSize),fg= "white" ,bg= bgColor).grid(row=n+5)
        
        button2 = tk.Button(window, text="Montrer la position optimale", font=(myFont, FontSize), bg= purple, fg= "white",command=get_solver)
        button2.grid(row=n+4, column=0, columnspan=2, pady=10)

            


    button = tk.Button(window, text="confirmer", font=(myFont, FontSize), bg= purple, fg= "white", command=get_n)
    button.grid(row=1, column=0, columnspan=2, pady=10)
            
    # n=int(e.get())
    window.mainloop()

if __name__ == "__main__":
    gui()
