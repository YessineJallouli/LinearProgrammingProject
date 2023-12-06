import gurobipy as gp
from gurobipy import GRB

# Create a Gurobi model
model = gp.Model("linear_program")

# Create variables
x1 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x1")
x2 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x2")
x3 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x3")
x4 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x4")
x5 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x5")
x6 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x6")
x7 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x7")

# Set objective function
model.setObjective(x1 + x2 + x3 + x4 + x5 + x6 + x7, sense=GRB.MINIMIZE)

# Add constraints
model.addConstr(x1 + x4 + x5 + x6 + x7 >= 17, "c1")
model.addConstr(x1 + x2 + x5 + x6 + x7 >= 13, "c2")
model.addConstr(x1 + x2 + x3 + x6 + x7 >= 15, "c3")
model.addConstr(x1 + x2 + x3 + x4 + x7 >= 19, "c4")
model.addConstr(x1 + x2 + x3 + x4 + x5 >= 14, "c5")
model.addConstr(x2 + x3 + x4 + x5 + x6 >= 16, "c6")
model.addConstr(x3 + x4 + x5 + x6 + x7 >= 11, "c7")

# Optimize the model
model.optimize()

# Print the results
print("\nOptimal solution:")
for var in model.getVars():
    print(f"{var.varName}: {var.x}")

print(f"\nOptimal objective value: {model.objVal}")