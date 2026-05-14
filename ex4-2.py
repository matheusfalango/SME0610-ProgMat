from pyscipopt import Model

scip = Model()

b = float(input())

x_1 = scip.addVar(vtype='C', lb=0, ub=10, name='x_1')
x_2 = scip.addVar(vtype='I', lb=0, ub=b, name='x_2')

cons_1 = scip.addCons(x_1 + x_2 <= 15, name='cons_1')

scip.setObjective(x_1 + 2 * x_2, sense="maximize")

# Evitar logs no terminal
scip.hideOutput()

# Otimizar
scip.optimize()

if scip.getStatus() == "optimal":
    print(f"{round(scip.getObjVal(),2)}")
    print(f"{round(scip.getVal(x_1),2)}")
    print(scip.getVal(x_2))

if scip.getStatus() == "unbounded":
    print("ILIMITADO")

if scip.getStatus() == "infeasible":
    print("INFACTÍVEL")