# importing tkinter for gui
import tkinter as tk
import TD2EX3

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
    window.geometry("800x700")
    # setting attribute
    # window.attributes('-fullscreen', True)
    window.title("Réseau")
    window.config(background=bgColor)

    # creating text label to display on window screen
    messages = ["Donner la distance AB",
                "Donner la distance AC",
                "Donner la distance BD","Donner la distance BE",
                "Donner la distance CB", "Donner la distance CE",
                "Donner la distance CF", "Donner la distance DE",
                "Donner la distance DG", "Donner la distance EG",
                "Donner la distance FE"]

    for i, c in enumerate(messages):
        tk.Label(window, text=c, font=(myFont, FontSize), fg="white", bg=bgColor).grid(row=i)

    ei = []
    for i in range(0, 11):
        e = tk.Entry(window)
        e.grid(row=i, column=1, pady=10)
        ei.append(e)

    def on_button_click():
        AB = float(ei[0].get())
        AC = float(ei[1].get())
        BD = float(ei[2].get())
        BE = float(ei[3].get())
        CB = float(ei[4].get())
        CE = float(ei[5].get())
        CF = float(ei[6].get())
        DE = float(ei[7].get())
        DG = float(ei[8].get())
        EG = float(ei[9].get())
        FE = float(ei[10].get())
        solution = TD2EX3.solve(AB,AC,BD,BE,CB,CE,CF,DE,DG,EG,FE)
        print(solution)
        label_message = tk.Label(window, text="", font=(myFont, FontSize), fg=blue, bg=bgColor)
        label_message.grid(row=12, column=0, columnspan=2, pady=10)
        label_message.config(text=solution)

    button = tk.Button(window, text="Donner la distance du chemin le plus rapide de A vers G", font=(myFont, FontSize), bg=purple, fg="white",
                       command=on_button_click)

    button.grid(row=11, column=0, columnspan=2, pady=10)
    window.mainloop()


if __name__ == "__main__":
    gui()
