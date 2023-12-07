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

# Set objective function
model.setObjective(2050*x1 + 1400*x2 + 1060*x3 + 1870*x4 + 1110*x5, sense=GRB.MAXIMIZE)

# Add constraints
model.addConstr(2*x1 + x2 + 2*x3 + 3*x4 + 2*x5 <= 3000, "c1")
model.addConstr(3000*x1 + 2000*x2 + 2500*x3 + 3800*x4 + 3200*x5 <= 25000000, "c2")
model.addConstr(30*x1 + 24*x2 + 20*x3 + 20*x4 + 28*x5 <= 24000, "c3")
model.addConstr(x1 + x2 + x3 + x4 + x5 <= 1000, "c4")

# Optimize the model
model.optimize()

# Print the results
print("\nOptimal solution:")
for var in model.getVars():
    print(f"{var.varName}: {var.x}")

print(f"\nOptimal objective value: {model.objVal}")