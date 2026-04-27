from pyscipopt import Model

scip = Model()

x_1 = scip.addVar(vtype='C', lb=0, ub=2, name='x_1')
x_2 = scip.addVar(vtype='C', lb=0, ub=3, name='x_2')
cons = scip.addCons(x_1 + x_2 <= 4, name='cons')

scip.setObjective(x_1 + 2 * x_2, sense="maximize")

# Evita logs no terminal
scip.hideOutput()

scip.optimize()

if scip.getStatus() == "optimal":
    print(scip.getObjVal())