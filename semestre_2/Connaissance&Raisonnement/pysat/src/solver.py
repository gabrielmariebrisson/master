from wumpusWorld import WumpusWorld
from pysat import *
import copy


gridToken={"M":1,"O":2, "H":3,"B":4, "G": 5, "S": 6}
class Joueur:
    def __init__(self, wumpus_world):
        self.size = wumpus_world._size
        self.wumpus_world = wumpus_world
        self.grid=wumpus_world._grid
        self.solver = Solver()

    def encode(self,x,y,z):
     return x*100 + y*10 + z

    def decode(self,n):
        x = n // 100
        n = n % 100 
        y = n // 10
        z = n % 10
        return x, y, z

    def generateConstraints(self):
        for x in range(1,self.size):
            for y in range(1,self.size):
                tokens = self.grid[x][y]
                for token in tokens:
                    clause=self.encode(x, y, gridToken[token])
                    print(clause)
                    self.solver.addClause([clause])


    def solve(self):
        self.generateConstraints()
        self.solver.buildDataStructure()

        (x, y) = self.wumpus_world.getPosition()
        result = self.solver.solve()     
        if result == self.solver._cst.lit_False: ## UNSAT
            return False
        elif result != self.solver._cst.lit_True: # Any error
            return False
        assert result == self.solver._cst.lit_True # on a une solution
        pile=[]
        pile.append([x, y])
        premier=False
        nb=0
        while (len(pile)>0):
            nb+=1
            (x, y)= pile.pop()
            print( " (x, y)", (x, y))
            print("move1")
            if nb>1:
                self.wumpus_world.moveHero(x, y)
                print(self.wumpus_world.__str__())
                premier=True
                print
            print("move2")
            for token in self.wumpus_world.observe():
                        if (token ==  "G"):
                            print("Gold found !")
                            return
            for (dx,dy) in [(-1,0), (0,1), (1,0), (0,-1)]:
                if x+dx >= 0 and y+dy >= 0 and x+dx < self.size and y+dy < self.size:
                    new_x = x+dx 
                    new_y = y+dy 
                    self.solver.finalModel
                    for token in self.solver.finalModel:
                        if token >= 100:
                            xtoken, ytoken, ztoken = self.decode(token)
                            if (xtoken != new_x and ytoken != new_y and ztoken != 1) and (ztoken != 3 and xtoken != new_x and ytoken != new_y) and not self.wumpus_world._visited[new_x][new_y]:
                                print("token",self.decode(token))
                                pile.append([new_x, new_y])
                        



# Test your Joueur class
wumpus_world = WumpusWorld()
joueur = Joueur(wumpus_world)
joueur.solve()