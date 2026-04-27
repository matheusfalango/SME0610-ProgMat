from pyscipopt import Model

scip = Model()

x_1 = scip.addVar(vtype='I', lb=0, ub=None, name='x_1')
x_2 = scip.addVar(vtype='I', lb=0, ub=None, name='x_2')

cons_1 = scip.addCons(9 * x_1 + 5 * x_2 <= 45, name='cons_1')
cons_2 = scip.addCons(-4 * x_1 + 5 * x_2 <= 5, name='cons_2')

scip.setObjective(10 * x_1 + 6 * x_2, sense="maximize")

# Evitar logs no terminal
scip.hideOutput()

# Otimizar
scip.optimize()

if scip.getStatus() == "optimal":
    print(scip.getObjVal())