import gurobipy as gp
from gurobipy import GRB


def solve(coff1, coff2, coff3, coff4, coff5, coff6, coff7, coff8, coff9, coff10, coff11):
    # Créer un modèle
    model = gp.Model("Optimization_Model")

    # Variables
    xAB = model.addVar(vtype=GRB.BINARY, name="xAB")
    xAC = model.addVar(vtype=GRB.BINARY, name="xAC")
    xBD = model.addVar(vtype=GRB.BINARY, name="xBD")
    xBE = model.addVar(vtype=GRB.BINARY, name="xBE")
    xCB = model.addVar(vtype=GRB.BINARY, name="xCB")
    xCE = model.addVar(vtype=GRB.BINARY, name="xCE")
    xCF = model.addVar(vtype=GRB.BINARY, name="xCF")
    xDE = model.addVar(vtype=GRB.BINARY, name="xDE")
    xDG = model.addVar(vtype=GRB.BINARY, name="xDG")
    xEG = model.addVar(vtype=GRB.BINARY, name="xEG")
    xFE = model.addVar(vtype=GRB.BINARY, name="xFE")

    #
    # coff1=input("donner la coeff de AB")
    # coff2=input("donner la coeff de AC")
    # coff3=input("donner la coeff de BD")
    # coff4=input("donner la coeff de BE")
    # coff5=input("donner la coeff de CB")
    # coff6=input("donner la coeff de CE")
    # coff7=input("donner la coeff de CF")
    # coff8=input("donner la coeff de DE")
    # coff9=input("donner la coeff de DG")
    # coff10=input("donner la coeff de EG")
    # coff11=input("donner la coeff de FE")

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

    # Affichage des résultats
    if model.status == GRB.OPTIMAL:
        print("Solution optimale trouvée:")
        for v in model.getVars():
            print(f"{v.varName} = {v.x}")
        print(f"Valeur de l'objectif: {model.objVal}")
    else:
        print("Aucune solution optimale trouvée.")

AB,AC,BD,BE,CB,CE,CF,DE,DG,EG,FE = 4,3,6,5,3,4,6,2,1,3,6
solve(AB,AC,BD,BE,CB,CE,CF,DE,DG,EG,FE)

