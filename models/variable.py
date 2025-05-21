class Variable:
    def __init__(self, name, variable_type, universe):
        self.name = name
        self.variable_type = variable_type
        self.universe = universe
        self.fuzzy_variable = None
        self.memberships = {}