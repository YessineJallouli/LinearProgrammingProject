import gurobipy as gp
from gurobipy import GRB


def solve(d1, d2, d3, d4, d5, d6, d7):
    # Create a Gurobi model
    model = gp.Model("linear_program")

    # Create variables
    x1 = model.addVar(lb=0, vtype=GRB.INTEGER, name="x1")
    x2 = model.addVar(lb=0, vtype=GRB.INTEGER, name="x2")
    x3 = model.addVar(lb=0, vtype=GRB.INTEGER, name="x3")
    x4 = model.addVar(lb=0, vtype=GRB.INTEGER, name="x4")
    x5 = model.addVar(lb=0, vtype=GRB.INTEGER, name="x5")
    x6 = model.addVar(lb=0, vtype=GRB.INTEGER, name="x6")
    x7 = model.addVar(lb=0, vtype=GRB.INTEGER, name="x7")

    # Set objective function
    model.setObjective(x1 + x2 + x3 + x4 + x5 + x6 + x7, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x1 + x4 + x5 + x6 + x7 >= d1, "c1")
    model.addConstr(x1 + x2 + x5 + x6 + x7 >= d2, "c2")
    model.addConstr(x1 + x2 + x3 + x6 + x7 >= d3, "c3")
    model.addConstr(x1 + x2 + x3 + x4 + x7 >= d4, "c4")
    model.addConstr(x1 + x2 + x3 + x4 + x5 >= d5, "c5")
    model.addConstr(x2 + x3 + x4 + x5 + x6 >= d6, "c6")
    model.addConstr(x3 + x4 + x5 + x6 + x7 >= d7, "c7")

    # Optimize the model
    model.optimize()

    # Return the results
    solution = {var.varName: int(var.x) for var in model.getVars()}
    return solution


D1, D2, D3, D4, D5, D6, D7 = 17, 13, 15, 19, 14, 16, 11
print(solve(D1, D2, D3, D4, D5, D6, D7))
