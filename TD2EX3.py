import gurobipy as gp
from gurobipy import GRB


def solve(coff1, coff2, coff3, coff4, coff5, coff6, coff7, coff8, coff9, coff10, coff11):
    # Créer un modèle
    model = gp.Model("Reseau")

    # Variables
    xAB = model.addVar(vtype=GRB.BINARY, name="AB")
    xAC = model.addVar(vtype=GRB.BINARY, name="AC")
    xBD = model.addVar(vtype=GRB.BINARY, name="BD")
    xBE = model.addVar(vtype=GRB.BINARY, name="BE")
    xCB = model.addVar(vtype=GRB.BINARY, name="CB")
    xCE = model.addVar(vtype=GRB.BINARY, name="CE")
    xCF = model.addVar(vtype=GRB.BINARY, name="CF")
    xDE = model.addVar(vtype=GRB.BINARY, name="DE")
    xDG = model.addVar(vtype=GRB.BINARY, name="DG")
    xEG = model.addVar(vtype=GRB.BINARY, name="EG")
    xFE = model.addVar(vtype=GRB.BINARY, name="FE")


    # Objectif
    model.setObjective(coff1*xAB + coff2*xAC + coff3*xBD + coff4*xBE + coff5*xCB + coff6*xCE + coff7*xCF + coff8*xDE + coff9*xDG + coff10*xEG + coff11*xFE, GRB.MINIMIZE)

    # Contraintes
    model.addConstr(xAB + xAC == 1, "c1")
    model.addConstr(xDG + xEG == 1, "c2")
    model.addConstr(xAB + xCB + xBD + xBE == 0, "c3")
    model.addConstr(xAC - xCB - xCE - xCF == 0, "c4")
    model.addConstr(xBD - xDE - xDG == 0, "c5")
    model.addConstr(xBE + xCE + xDE + xFE - xEG == 0, "c6")
    model.addConstr(xCF - xFE == 0, "c7")

    # Optimisation
    model.optimize()
    res = "La distance minimale entre A et G est : " + str(model.objVal) + ". Il faut traverser : "

    l = []
    for v in model.getVars():
        if v.x == 1:
            if len(str(v.varName)) != 2:
                continue
            l.append(str(v.varName))

    for i in range(0, len(l)):
        if len(l[i]) == 1:
            continue
        for j in range(i+1, len(l)):
            if l[i][1] == l[j][0]:
                l[i+1],l[j] = l[j],l[i+1]

    for i in l:
        res = res + str(i) + ","
    return res[:-1]


AB,AC,BD,BE,CB,CE,CF,DE,DG,EG,FE = 4,3,6,5,3,4,6,2,1,3,6
solve(AB,AC,BD,BE,CB,CE,CF,DE,DG,EG,FE)

