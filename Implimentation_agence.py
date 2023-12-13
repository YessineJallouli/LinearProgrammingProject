import gurobipy as gp
from gurobipy import GRB

# a,b,c=(model.addVar(lb=0, vtype=GRB.INTEGER, name=f"popul_var{i+1}") for i in range(3))
# K,B,D=(model.addVar(lb=0, vtype=GRB.INTEGER, name=f"budget{i+1}") for i in range(3))
# A=[[model.addVar(lb=0, vtype=GRB.BINARY, name=f"a{i}_{j}") for i in range(9)] for j in range(9)]
# # Create a Gurobi model
# population=[model.addVar(lb=0, vtype=GRB.BINARY, name=f"populationR{i}") for i in range(9)]
population=[2,3,4,5,6,7,8,9,10]

A=[
    [1,1,0,0,1,0,0,0,0],
    [1,1,1,1,1,0,0,0,0],
    [0,1,1,1,0,0,0,0,0],
    [0,1,1,1,1,0,1,0,0],
    [1,1,0,1,1,0,1,0,0],
    [0,0,0,0,0,1,1,0,1],
    [0,0,0,1,1,1,1,1,0],
    [0,0,0,0,0,0,1,1,1],
    [0,0,0,0,0,1,0,1,1]
    ]
K=500000
D=20000
B=2000000
a=5
b=1
c=2
def solve(a,b,c,A,K,D,B,population):
    population=[i*10 for i in population]
    model = gp.Model("linear_program")
    agencies=[model.addVar(lb=0, vtype=GRB.BINARY, name=f"ag{i+1}") for i in range(9)]
    Server_DAB=[model.addVar(lb=0, vtype=GRB.BINARY, name=f"DAB{i+1}") for i in range(9)]
    Z=0
    for i,(Ag,Se) in enumerate(zip(agencies,Server_DAB)):
        population_voisine=sum([j*pop for j,pop in zip(A[i],population)])-A[i][i]*population[i]
        Z+=population[i]*(a*Ag+c*Se)+population_voisine*(Ag*b)

    model.setObjective(Z, sense=GRB.MAXIMIZE)
    for i in range(9):
        for j in range(i+1,9):
            model.addConstr(agencies[i]+agencies[j]<=1)
    model.addConstr(sum(agencies)*K+sum(Server_DAB)*D <=B)
    model.optimize()
    print("\nOptimal solution:")
    for var in model.getVars():
        print(f"{var.varName}: {var.x}")
    print(f"\nOptimal objective value: {model.objVal}")
    return 
solve(a,b,c,A,K,D,B,population)