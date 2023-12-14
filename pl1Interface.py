# importing tkinter for gui
import tkinter as tk
import pl1

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
    window.geometry("700x700")
    # setting attribute
    #window.attributes('-fullscreen', True)
    window.title("ChaussTous")
    window.config(background=bgColor)


    messages = ["ouvrierBle, tempsMachineBle, eauBle :", "ouvrierOrge, tempsMachineOrge, eauOrge :", "ouvrierMais, tempsMachineMais, eauMais :",
"ouvrierBetSucre, tempsMachineBetSucre, eauBetSucre :", "ouvrierTournesol, tempsMachineTournesol, eauTournesol :", "beneficeBle :",
"beneficeOrge :", "beneficeMais :", "beneficeBetSucre :", "beneficeTournesol :"]
    
    for i,c in enumerate(messages):
        tk.Label(window, text=c,              font=(myFont, FontSize),fg= "white" ,bg= bgColor).grid(row=i)                      
    
    ei=[]
    for i in range(0,10):
        e=tk.Entry(window)
        e.grid(row=i, column=1, pady=10, columnspan= 20)
        ei.append(e)

    def on_button_click():
        ouvrierBle, tempsMachineBle, eauBle = map(int, ei[0].get().split())
        ouvrierOrge, tempsMachineOrge, eauOrge = map(int, ei[1].get().split())              
        ouvrierMais, tempsMachineMais, eauMais = map(int, ei[2].get().split()) 
        ouvrierBetSucre, tempsMachineBetSucre, eauBetSucre = map(int, ei[3].get().split())         
        ouvrierTournesol, tempsMachineTournesol, eauTournesol = map(int, ei[4].get().split())          
        beneficeBle = int(ei[5].get())
        beneficeOrge = int(ei[6].get())          
        beneficeMais = int(ei[7].get())          
        beneficeBetSucre = int(ei[8].get())      
        beneficeTournesol = int(ei[9].get())     

        solution = pl1.solve(ouvrierBle, tempsMachineBle, eauBle, ouvrierOrge, tempsMachineOrge, eauOrge, ouvrierMais, 
                             tempsMachineMais, eauMais, ouvrierBetSucre, tempsMachineBetSucre, eauBetSucre, ouvrierTournesol, 
                             tempsMachineTournesol, eauTournesol, beneficeBle, beneficeOrge, beneficeMais, beneficeBetSucre, 
                             beneficeTournesol)
        print(solution)
        label_message = tk.Label(window, text="", font=(myFont, FontSize), fg =blue, bg= bgColor)
        label_message.grid(row=13, column=0, columnspan=2, pady=10)
        label_message.config(text=solution)

    button = tk.Button(window, text="Montrer la stratégie optimale", font=(myFont, FontSize), bg= purple, fg= "white", command=on_button_click)
    
    button.grid(row=13, column=0, columnspan=2, pady=10)
    window.mainloop()

if __name__ == "__main__":
    gui()
