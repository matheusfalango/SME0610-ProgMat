from pyscipopt import Model

scip = Model()

b = list(map(float, input().split()))[:4]

#b = []
#entrada = input().split()
#for i in range(min(4, len(entrada))):
#    b.append(float(entrada[i]))

x_1 = scip.addVar(vtype='C', lb=0, ub=None, name='x_1')
x_2 = scip.addVar(vtype='I', lb=0, ub=None, name='x_2')

cons_1 = scip.addCons(-1 * x_1 + x_2 >= b[0], name='cons_1')
cons_2 = scip.addCons(x_1 + x_2 <= b[1], name="cons_2")
cons_3 = scip.addCons(x_1 >= b[2], name="cons_3")
cons_4 = scip.addCons(x_2 >= b[3], name="cons_4")

scip.setObjective(x_1 + 2 * x_2, sense="minimize")

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