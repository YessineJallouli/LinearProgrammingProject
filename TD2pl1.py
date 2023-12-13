import tkinter as tk
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
    window.title("ChaussTous")
    window.config(background=bgColor)
    tk.Label(window, text="Donner le nomber de chambre",font=(myFont, FontSize),fg= "white" ,bg= bgColor).grid(row=0)
    window.mainloop()
gui()
    