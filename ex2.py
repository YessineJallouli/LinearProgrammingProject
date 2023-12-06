import gurobipy as gp
from gurobipy import GRB
import numpy as np


def concatenate(*args):
    xt = []
    for a in args:
        for j in a:
            xt.append(j)

    xt = np.array(xt)
    return xt


"""
c_i : demande de ième mois
nbOuv : nombre d'ouvrier disposé
salaire : salaire d'un ouvrier
nbH : nombre d'heure travaillé par un ouvrier pendant un mois
nbSp : nombre d'heures supplementaire par mois
prixSup : prix d'une heure supplementaire
tmpCh  : temps pour faire une paire de chaussure
rec : Frais du recrutement
lic  : Frais du licenciement
"""


def solve(c1, c2, c3, c4, nbOuv, salaire, nbH, nbSp, prixSup, tmpCh, rec, lic):
    model = gp.Model("ex2")
    n = 12
    variables = model.addMVar(shape=n, vtype=GRB.INTEGER, name="x")
    ctr1 = np.array([nbSp, 0, 0, 0, -nbSp, 0, 0, 0, -1, 0, 0, 0])
    ctr2 = np.array([nbSp, nbSp, 0, 0, -nbSp, -nbSp, 0, 0, 0, -1, 0, 0])
    ctr3 = np.array([nbSp, nbSp, nbSp, 0, -nbSp, -nbSp, -nbSp, 0, 0, 0, -1, 0])
    ctr4 = np.array([nbSp, nbSp, nbSp, nbSp, -nbSp, -nbSp, -nbSp, -nbSp, 0, 0, 0, -1])

    ctr5 = np.array([nbH, 0, 0, 0, -nbH, 0, 0, 0, 1, 0, 0, 0])
    ctr6 = np.array([nbH, nbH, 0, 0, -nbH, -nbH, 0, 0, 0, 1, 0, 0])
    ctr7 = np.array([nbH, nbH, nbH, 0, -nbH, -nbH, -nbH, 0, 0, 0, 1, 0])
    ctr8 = np.array([nbH, nbH, nbH, nbH, -nbH, -nbH, -nbH, -nbH, 0, 0, 0, 1])

    allCtr = concatenate(ctr1, ctr2, ctr3, ctr4, ctr5, ctr6, ctr7, ctr8).reshape(8, n)

    rhs = np.array([-nbOuv * nbSp, -nbOuv * nbSp, -nbOuv * nbSp, -nbOuv * nbSp, -nbOuv * nbH + c1 * tmpCh,
                    -nbOuv * nbH + c2 * tmpCh, -nbOuv * nbH + c3 * tmpCh, -nbOuv * nbH + c4 * tmpCh])

    model.addConstr(allCtr @ variables >= rhs, name="c")
    # objective function
    obj = np.array(
        [rec + 4 * salaire, rec + 3 * salaire, rec + 2 * salaire, rec + salaire, lic - 4 * salaire, lic - 3 * salaire,
         lic - 2 * salaire, lic - salaire, prixSup, prixSup, prixSup, prixSup])

    model.setObjective(obj @ variables, GRB.MINIMIZE)
    model.optimize()

    print("The model has an optimal solution.")
    solution = {var.varName: var.x for var in model.getVars()}
    return solution


C1, C2, C3, C4 = 3000, 5000, 4000, 1000
NbOuv = 100
Salaire, NbH, SbSp, PrixSup = 1500, 160, 20, 13
TmpCh = 4
Rec, Lic = 1600, 2000

ans = solve(C1, C2, C3, C4, NbOuv, Salaire, NbH, SbSp, PrixSup, TmpCh, Rec, Lic)
print(ans)
