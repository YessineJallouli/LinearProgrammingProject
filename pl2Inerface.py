# importing tkinter for gui
import tkinter as tk
import pl2


def strategy(r, l, s):
    res = ""
    if r > 0:
        if r == 1:
            res += "Il faut recruter une personne"
        else:
            res += "Il faut recruter " + str(r) + " personnes"
    elif l > 0:
        if l == 1:
            res += "Il faut licencier une personne"
        else:
            res += "Il faut licencier " + str(l) + " personnes"

    if s > 0:
        if len(res):
            res += ". "
        if s == 1:
            res += "Une personne doit faire des heures supplémentaires"
        else:
            res += str(s) + " personnes doivent faire des heures supplémentaires"
    if r == 0 and l == 0 and s == 0:
        res += "Rien à faire"
    res += '\n'
    return res


def on_button_click():
    c1 = int(e1.get())
    c2 = int(e2.get())
    c3 = int(e3.get())
    c4 = int(e4.get())
    nbOuv = int(e5.get())
    salaire = int(e6.get())
    nbH = int(e7.get())
    nbSp = int(e8.get())
    prixSup = int(e9.get())
    tmpCh = int(e10.get())
    rec = int(e11.get())
    lic = int(e12.get())
    solution = pl2.solve(c1, c2, c3, c4, nbOuv, salaire, nbH, nbSp, prixSup, tmpCh, rec, lic)
    # print(solution)
    s = "Stratégie du premier mois :\n" + strategy(solution['x[0]'], solution['x[4]'],
                                                   (solution['x[8]'] + nbH - 1) // nbH)
    s += "Stratégie du second mois :\n" + strategy(solution['x[1]'], solution['x[5]'],
                                                   (solution['x[9]'] + nbH - 1) // nbH)
    s += "Stratégie du troisième mois :\n" + strategy(solution['x[2]'], solution['x[6]'],
                                                      (solution['x[10]'] + nbH - 1) // nbH)
    s += "Stratégie du quatrième mois :\n" + strategy(solution['x[3]'], solution['x[7]'],
                                                      (solution['x[11]'] + nbH - 1) // nbH)

    label_message.config(text=s)


# creating window
window = tk.Tk()

# setting attribute
window.attributes('-fullscreen', True)
window.title("ChaussTous")

# creating text label to display on window screen

tk.Label(window, text="Nombre de chaussure demandé pour le premier mois :", font=("Arial", 24)).grid(row=0)
tk.Label(window, text="Nombre de chaussure demandé pour le second mois :", font=("Arial", 24)).grid(row=1)
tk.Label(window, text="Nombre de chaussure demandé pour le troisième mois :", font=("Arial", 24)).grid(row=2)
tk.Label(window, text="Nombre de chaussure demandé pour le quatrième mois :", font=("Arial", 24)).grid(row=3)
tk.Label(window, text="Nombre d’ouvrier disposé :", font=("Arial", 24)).grid(row=4)
tk.Label(window, text="Salaire d’un ouvrier en dinars :", font=("Arial", 24)).grid(row=5)
tk.Label(window, text="Nombre d’heures travaillé par un ouvrier pendant un mois :", font=("Arial", 24)).grid(row=6)
tk.Label(window, text="Nombre d’heures supplémentaire maximale pendant un mois :", font=("Arial", 24)).grid(row=7)
tk.Label(window, text="Prix d’une heure supplémentaire :", font=("Arial", 24)).grid(row=8)
tk.Label(window, text="Temps pour faire une paire de chaussure : ", font=("Arial", 24)).grid(row=9)
tk.Label(window, text="Frais de recrutement :", font=("Arial", 24)).grid(row=10)
tk.Label(window, text="Frais de licenciement :", font=("Arial", 24)).grid(row=11)

e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)
e4 = tk.Entry(window)
e5 = tk.Entry(window)
e6 = tk.Entry(window)
e7 = tk.Entry(window)
e8 = tk.Entry(window)
e9 = tk.Entry(window)
e10 = tk.Entry(window)
e11 = tk.Entry(window)
e12 = tk.Entry(window)

e1.grid(row=0, column=1, pady=10)
e2.grid(row=1, column=1, pady=10)
e3.grid(row=2, column=1, pady=10)
e4.grid(row=3, column=1, pady=10)
e5.grid(row=4, column=1, pady=10)
e6.grid(row=5, column=1, pady=10)
e7.grid(row=6, column=1, pady=10)
e8.grid(row=7, column=1, pady=10)
e9.grid(row=8, column=1, pady=10)
e10.grid(row=9, column=1, pady=10)
e11.grid(row=10, column=1, pady=10)
e12.grid(row=11, column=1, pady=10)

button = tk.Button(window, text="Montrer la stratégie optimale", font=("Arial", 18), command=on_button_click)
button.grid(row=12, column=0, columnspan=2, pady=10)

label_message = tk.Label(window, text="", font=("Arial", 18))
label_message.grid(row=13, column=0, columnspan=2, pady=10)

window.mainloop()
