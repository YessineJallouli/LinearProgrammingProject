import gurobipy as gp
from gurobipy import GRB

def solve(ouvrierBle, tempsMachineBle, eauBle, ouvrierOrge, tempsMachineOrge, eauOrge, ouvrierMais, 
        tempsMachineMais, eauMais, ouvrierBetSucre, tempsMachineBetSucre, eauBetSucre, ouvrierTournesol, 
        tempsMachineTournesol, eauTournesol, beneficeBle, beneficeOrge, beneficeMais, beneficeBetSucre, beneficeTournesol):
    # Create a Gurobi model
    model = gp.Model("linear_program")

    # Create variables
    x1 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x1")
    x2 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x2")
    x3 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x3")
    x4 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x4")
    x5 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x5")    

    # Set objective function
    model.setObjective(beneficeBle*x1 + beneficeOrge*x2 + beneficeMais*x3 + beneficeBetSucre*x4 + beneficeTournesol*x5, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(ouvrierBle*x1 + ouvrierOrge*x2 + ouvrierMais*x3 + ouvrierBetSucre*x4 + ouvrierTournesol*x5 <= 3000, "c1")
    model.addConstr(eauBle*x1 + eauOrge*x2 + eauMais*x3 + eauBetSucre*x4 + eauTournesol*x5 <= 25000000, "c2")
    model.addConstr(tempsMachineBle*x1 + tempsMachineOrge*x2 + tempsMachineMais*x3 + tempsMachineBetSucre*x4 + tempsMachineTournesol*x5 <= 24000, "c3")
    model.addConstr(x1 + x2 + x3 + x4 + x5 <= 1000, "c4")

    # Optimize the model
    model.optimize()

    solution = ""
    myList = ["Quantité blé", "Quantité orge", "Quantite mais", "Quantité bet-sucré", "Quantité tournesol"]
    i = 0
    print("\nOptimal solution:")
    for var in model.getVars():
        solution+=f"{myList[i]} est {var.x}\n"
        i+=1
    solution+= f"Optimal objective value: {model.objVal}"
    return solution 