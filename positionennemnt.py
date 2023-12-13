import gurobipy as gp
from gurobipy import GRB
model = gp.Model("linear_program")
place_antene=[model.addVar(lb=0, vtype=GRB.BINARY, name=f"{i}") for i in "ABCDEFG"]
place_antene_acces=[[1,2],[1,3],[1,4],[3,4],[2,4],[2,5],[4,5]]
model.setObjective(sum(place_antene), sense=GRB.MINIMIZE)
contraint=[1,1,1,2,1]
for i in range(1,5):
    Z=0
    for j in range(7):
        if i in place_antene_acces[j]:
            Z+=place_antene[j]

    model.addConstr(Z>=contraint[i])
model.optimize()
# Print the results
print("\nOptimal solution:")
for var in model.getVars():
    print(f"{var.varName}: {var.x}")

print(f"\nOptimal objective value: {model.objVal}")