from pyscipopt import Model

scip = Model()

c = int(input())

x_1 = scip.addVar(vtype='C', lb=0, ub=None, name='x_1')
x_2 = scip.addVar(vtype='I', lb=0, ub=None, name='x_2')

cons_1 = scip.addCons(10 * x_1 + 18 * x_2 <= 52, name='cons_1')
cons_2 = scip.addCons(-1 * x_1 + x_2 <= 2, name='cons_2')

scip.setObjective(c * x_1 + (c + 4) * x_2, sense="maximize")

# Evitar logs no terminal
scip.hideOutput()

# Otimizar
scip.optimize()

if scip.getStatus() == "optimal":
    print(f"{round(scip.getObjVal(),2)}")
    print(f"{round(scip.getVal(x_1),2)}")
    print(scip.getVal(x_2))