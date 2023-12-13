import gurobipy as gp
from gurobipy import GRB
# point="ABCDEFG"
# contraint=[1,1,1,2,1]
# place_antene_acces=[[1,2],[1,3],[1,4],[3,4],[2,4],[2,5],[4,5]]


def solve(Point,place_antene_acces,contraint,number_room):
    model = gp.Model("linear_program")
    place_antene=[model.addVar(lb=0, vtype=GRB.BINARY, name=f"{i}") for i in Point]
    model.setObjective(sum(place_antene), sense=GRB.MINIMIZE)
    
    for i in range(1,number_room+1):
        Z=0
        for j in range(len(Point)):
            if i in place_antene_acces[j]:
                Z+=place_antene[j]

        model.addConstr(Z>=contraint[i-1])
    model.optimize()
    # Print the results
    print("\nOptimal solution:")
    sol={}
    for var in model.getVars():
        print(type(var.VarName))
        print(f"{var.varName}: {var.x}")

    print(f"\nOptimal objective value: {model.objVal}")
    return model
