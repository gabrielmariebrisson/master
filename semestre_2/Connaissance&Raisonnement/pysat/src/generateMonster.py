
__GRIDSIZE__ = 4

def inBound(x):
   if x < 0 or x >= __GRIDSIZE__: return False
   return True

def around(coord):
   (x,y) = coord
   toret = []
   for (dx,dy) in [(-1,0), (0,1), (1,0), (0,-1)]:
      if inBound(dx+x) and inBound(dy+y):
         toret.append((dx+x, dy+y))
   return toret

def varToStr(symbol, coord):
   encodage = {"M":1,"O":2,"T":3,"V":4,"G":5}

   return str(encodage[symbol]*100+coord[0]*10+coord[1])
   #return symbol+str(coord)

def printConstraint(symbol1, symbol2, coord):
   for (x,y) in around(coord):
      print("-" +varToStr(symbol1,coord)+" "+varToStr(symbol2,(x,y)), "0")
      #print(varToStr(symbol1, coord)+" -> "+varToStr(symbol2,(x,y)))

def printConstraintNeg(symbol1, symbol2, coord):
   for (x,y) in around(coord):
      print(varToStr(symbol1,coord)+" "+"-" +varToStr(symbol2,(x,y)), "0")
      #print("not " + varToStr(symbol1, coord)+" -> not "+varToStr(symbol2,(x,y)))

def printExclusionConstraint(symbol1, symbol2, coord):
   print("-" +varToStr(symbol1,coord)+" "+"-" +varToStr(symbol2,coord), "0")
   print("-" +varToStr(symbol2,coord)+" "+"-" +varToStr(symbol1,coord), "0")
   #print(varToStr(symbol1,coord) + "-> not " + varToStr(symbol2,coord))
   #print(varToStr(symbol2,coord) + "-> not " + varToStr(symbol1,coord))

def printAllConstraints(coord):
   printConstraint("T", "V", coord) # A Hole implies wind all around
   printConstraint("M", "O", coord) # A Monster implies odors all around
   printConstraintNeg("O", "M", coord) # No Odor means no monster all around
   printConstraintNeg("V", "T", coord) # No wind implies no hole all around
   printExclusionConstraint("M","T",coord) # A cell cannot contain a Monster and a Hole
   printExclusionConstraint("G","T",coord) # A cell cannot contain a Gold and a Hole
   printExclusionConstraint("G","M",coord) # A cell cannot contain a Gold and a Monster

def calcul(coord):
   return coord.x

## Now prints all the constaints

for x in range(__GRIDSIZE__):
  for y in range(__GRIDSIZE__):
    printAllConstraints((x,y))

print("-" + varToStr("M",(0,0)), "0")
print("-" + varToStr("O",(0,0)), "0")
print("-" + varToStr("G",(0,0)), "0")
print("-" + varToStr("V",(0,0)), "0")


def hasPath(hints):
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

