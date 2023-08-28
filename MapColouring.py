print("revanth")
print("192111393")
class MapColoringCSP:
    def __init__(self, variables, domains, neighbors):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.assignment = {}

    def is_consistent(self, variable, color):
        for neighbor in self.neighbors[variable]:
            if neighbor in self.assignment and self.assignment[neighbor] == color:
                return False
        return True

    def backtracking_search(self):
        return self.backtrack({})

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        unassigned_vars = [var for var in self.variables if var not in assignment]
        var = unassigned_vars[0]

        for color in self.domains[var]:
            if self.is_consistent(var, color):
                assignment[var] = color
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                assignment.pop(var, None)

        return None

variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
domains = {var: ['R', 'G', 'B'] for var in variables}
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

csp = MapColoringCSP(variables, domains, neighbors)
solution = csp.backtracking_search()

if solution:
    print("Solution found:")
    for var, color in solution.items():
        print(f"{var}: {color}")
else:
    print("No solution found.")
