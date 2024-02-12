from pysat import *
import numpy as np
import random

# First we need to print clauses
def printClause(clause):
    print(" ".join([str(v) for v in clause]) + " 0")

def equals1a(arrayOfVars, callback=printClause):
    callback(arrayOfVars) 
    for i,x in enumerate(arrayOfVars):
        for y in arrayOfVars[i+1:]:
            callback([-x, -y])

def encode(x,y,z):
     return x*100 + y*10 + z

def decode(n):
    x = n // 100
    n = n % 100 
    y = n // 10
    z = n % 10
    return x, y, z

def generateConstraints(callback=printClause):
    for x in range(1,10):
        for y in range(1,10):
            # Case (x,y) ne contient qu'un nombre dans 1..9
                equals1a([encode(x,y,z) for z in range(1,10)], callback)

    for x in range(1,10):
        for z in range(1,10):
            # 
                equals1a([encode(x,y,z) for y in range(1,10)], callback)

    for y in range(1,10):
        for z in range(1,10):
            # 
                equals1a([encode(x,y,z) for x in range(1,10)], callback)

    for z in range(1,10):
        for x in range(3):
            for y in range(3):
                # carre (x,y) et z 
                equals1a([encode(x * 3 + xx,y * 3 + yy, z) for xx in range(1,4) for yy in range(1,4)], callback)

 
def getHints(hintsFile = "examples/hints.cnf"):
    hints = []
    for line in open(hintsFile):
        ll = line.split(" ")
        if len(ll) > 1:
            hints.append(int(ll[0])) 
    return hints

def getSolverWithHints(hints): # hints: liste de hints
    satSolver = Solver()
    satSolver._config.verbosity= 0
    generateConstraints(satSolver.addClause)
    for h in hints:
         satSolver.addClause([h])
    return satSolver

def hasOnlyOneSolution(hints):
    satSolver = getSolverWithHints(hints)
    satSolver.buildDataStructure()
    result = satSolver.solve()     
    if result == satSolver._cst.lit_False: ## UNSAT
        return False
    elif result != satSolver._cst.lit_True: # Any error
        return False
    assert result == satSolver._cst.lit_True # on a une solution

    nouvelleClause = []
    for v in satSolver.finalModel:
          if v > 0: # Variable positive dans la solution
            x,y,z = decode(v)
            if x > 0 and x < 10 and y > 0 and y < 10 and z > 0 and z < 10:
                nouvelleClause.append(-v)
    
    satSolver = getSolverWithHints(getHints())
    satSolver.addClause(nouvelleClause)
    satSolver.buildDataStructure()
    result = satSolver.solve()     
    if result == satSolver._cst.lit_False: ## UNSAT
        return True
    return False 
    
print(hasOnlyOneSolution(getHints()))


def generateRandomSudoku():
    hints=[]  
    for x in range(1, 10):
        for y in range(1, 10):
            result = False
            satSolver = getSolverWithHints(hints)
            
            while result != satSolver._cst.lit_True:
                randomValue = random.randint(1, 9)
                code = encode(x, y, randomValue)
                hints.append(code)
                
                satSolver = getSolverWithHints(hints)
                satSolver.buildDataStructure()
                result = satSolver.solve()
                
                if result == satSolver._cst.lit_False:
                    hints.pop()

    return hints

def createSudoku(hints, nbTentative):
    nbTry = nbTentative
    deleteHints = hints.copy() 

    while True:
        randomDelete = random.choice(deleteHints) 
        deleteHints.remove(randomDelete)  

        if hasOnlyOneSolution(deleteHints): 
            hints = deleteHints.copy()
            nbTry = nbTentative
            print(hints)
        else:
            deleteHints = hints.copy()
            nbTry -= 1
            #print(nbTry)
    return hints


hints=[112, 126, 138, 144, 151, 165, 173, 187, 199, 215, 224, 237, 248, 259, 263, 271, 286, 292, 311, 323, 339, 346, 357, 362, 375, 388, 394, 417, 425, 431, 449, 452, 466, 474, 483, 498, 513, 529, 536, 547, 558, 564, 572, 581, 595, 618, 622, 634, 643, 655, 661, 676, 689, 697, 719, 721, 733, 745, 754, 767, 778, 782, 796, 814, 827, 832, 841, 856, 868, 879, 885, 893, 916, 928, 935, 942, 953, 969, 977, 984, 991]
print (createSudoku(hints, 30))

'''
elif result == satSolver._cst.lit_True: # SAT was claimed
    solution = np.zeros((9,9), dtype=int) 
    for v in satSolver.finalModel:
          if v > 0: # Variable positive dans la solution
            x,y,z = decode(v)
            if x > 0 and x < 10 and y > 0 and y < 10 and z > 0 and z < 10:
                solution[x-1, y-1] = z #print(v," ", end="")
    print(solution)
'''