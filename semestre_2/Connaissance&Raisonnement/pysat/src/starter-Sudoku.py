import numpy as np

from pysat import Solver
# First we need to print clauses
def printClause(clause):
    print(" ".join([str(v) for v in clause]) + " 0")

def equals1a(arrayOfVars):
    printClause(arrayOfVars) 
    for i,x in enumerate(arrayOfVars):
        for y in arrayOfVars[i+1:]:
            printClause([-x, -y])

def encode(x,y,z):
    return x*100+y*10+z

def decode (n):
    x= n//100
    n= n %100
    y = n //10
    z = n %10

    return x,y,z

def generateConstraints(printClause):
    for x in range(1, 10):
        for y in range( 1, 10):
            equals1a([encode(x,y,z) for z in range (1,10)])

    for y in range(1, 10):
        for z in range( 1, 10):
            equals1a([encode(x,y,z) for x in range (1,10)])

    for x in range(1, 10):
        for z in range( 1, 10):
            equals1a([encode(x,y,z) for y in range (1,10)])

    for z in range (1,10):
        for x in range(3):
            for y in range(3):
                equals1a([encode(x*3+xx,y*3+yy,z) for xx in range (1, 4) for yy in range (1,4)])

satSolver = Solver()
satSolver._config.verbosity = 0
generateConstraints(satSolver.addClause)
for line in open ("examples/hints.cnf"):
    ll = line.split(" ")
    if len(ll) > 1:
        satSolver.add_clause([int(ll[0])]) #clause avec 1 seul litéral


def getSolverWithHints(hints):
    satSolver = Solver()
    satSolver._config.verbosity =0
    generateConstraints(satSolver.addClause)

    return satSolver

def getHints(hintsFile = "hints.cnf"):
    hints = []
    for line in open(hintsFile):
        ll = line.split(" ")
        if len(ll)> :
            hints.append(int( ll[0]))
        return hints

satSolver.buildDataStructure()
result = satSolver.solve()
if result == satSolver._cst.lit_False: #UNSAT
    
    pass
if result == satSolver._cst.lit_True: #SAT claimed
    print("v ", end="")
    solution = np.zeros((9,9), dtype=int)
    for v in satSolver.finalModel:
        if v > 0:
            x,y,z = decode(v)
            if x > 0 and y > 0 and z > 0 and x < 10 and y < 10 and z < 10:
                solution[x-1,y-1] = z
    print(solution)

tmp = list(range(1,5))
print("c Constraints forcing just on true variable in", tmp)
print("c we don't print any 'p cnf X Y' line, sorry")
equals1a(tmp)
