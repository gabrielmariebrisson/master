from wumpusWorld import WumpusWorld
from pycsp3 import *

class WumpusSolver:

    def __init__(self, wumpus_world):
        self.size = wumpus_world._size
        self.wumpus_world = wumpus_world

    def solve(self):
        # Create CSP
        problem = Problem()
        positions = [(x, y) for x in range(self.size) for y in range(self.size)]

        # Variables
        agent_positions = VarArray(size=self.size, dom=positions)

        # Constraints
        for i in range(1, self.size):
            problem.add(agent_positions[i] - agent_positions[i - 1] in [(-1, 0), (0, -1), (1, 0), (0, 1)])

        def wumpus_location(x, y):
            return self.wumpus_world._grid[x][y]

        def breeze(x, y):
            return "B" in wumpus_location(x, y)

        def stench(x, y):
            return "M" in wumpus_location(x, y)

        def pit(x, y):
            return "H" in wumpus_location(x, y)

        def safe(x, y):
            return not pit(x, y) and not stench(x, y)

        for x, y in positions:
            # If breeze or stench, then there is a pit or wumpus nearby
            if breeze(x, y) or stench(x, y):
                problem.add(And(Or(pit(x + dx, y + dy) for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]),
                                Or(stench(x + dx, y + dy) for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)])))

            # If safe, then no pit or wumpus nearby
            if safe(x, y):
                problem.add(Not(Or(pit(x + dx, y + dy) for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]),
                                 Or(stench(x + dx, y + dy) for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)])))

        # Solve the CSP
        solution = problem.solve()
        if solution:
            print("Solution found:")
            for pos in solution[agent_positions]:
                print(pos)
        else:
            print("No solution found.")

# Example usage
wumpus_world = WumpusWorld()
solver = WumpusSolver(wumpus_world)
solver.solve()
