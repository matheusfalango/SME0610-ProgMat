from pyscipopt import Model

scip = Model()

c = float(input())

x_1 = scip.addVar(vtype='C', lb=0, ub=20, name='x_1')
x_2 = scip.addVar(vtype='I', lb=0, ub=20, name='x_2')

cons_1 = scip.addCons(5 * x_1 + x_2 <= 100, name='cons_1')
cons_2 = scip.addCons(x_1 - x_2 <= 15, name='cons_2')
cons_3 = scip.addCons(-1 * x_1 + 12 * x_2 <= 225, name="cons_3")
cons_4 = scip.addCons(x_1 + x_2 >= 10, name="cons_4")

scip.setObjective(pow(c,2) * x_1 + c * x_2, sense="minimize")

# Evitar logs no terminal
scip.hideOutput()

# Otimizar
scip.optimize()

if scip.getStatus() == "optimal":
    print(f"{round(scip.getObjVal(),2)}")
    print(f"{round(scip.getVal(x_1),2)}")
    print(scip.getVal(x_2))