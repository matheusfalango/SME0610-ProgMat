from pyscipopt import Model

scip = Model()

x_1 = scip.addVar(vtype='B', name='x_1')
x_2 = scip.addVar(vtype='B', name='x_2')

cons = scip.addCons(6 * x_1 + 8 * x_2 <= 10, name='cons')

scip.setObjective(2 * x_1 + 3 * x_2, sense="maximize")

# Evitar logs no terminal
scip.hideOutput()

# Otimizar
scip.optimize()

if scip.getStatus() == "optimal":
    print(scip.getObjVal())
    print(scip.getVal(x_1))
    print(scip.getVal(x_2))