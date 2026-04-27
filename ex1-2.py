from pyscipopt import Model

scip = Model()

x_1 = scip.addVar(vtype='C', lb=0, ub=None, name='x_1')
x_2 = scip.addVar(vtype='C', lb=0, ub=None, name='x_2')
x_3 = scip.addVar(vtype='C', lb=0, ub=None, name='x_3')
cons_1 = scip.addCons(0.2 * x_1 + 0.5 * x_2 + 0.4 * x_3 >= 0.3, name='cons_1')
cons_2 = scip.addCons(0.6 * x_1 + 0.4 * x_2 + 0.4 * x_3 >= 0.5, name='cons_2')
cons_3 = scip.addCons(x_1 + x_2 + x_3 == 1, name='cons_3')

scip.setObjective(0.56 * x_1 + 0.81 * x_2 + 0.46 * x_3, sense="minimize")

# Evita logs no terminal
scip.hideOutput()

scip.optimize()

if scip.getStatus() == "optimal":
    print(scip.getObjVal())