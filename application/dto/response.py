class CreateVariableResponse:
    def __init__(self, variable):
        self.name = variable.name
        self.fuzzy_variable = variable.fuzzy_variable
        self.type = variable.type
        self.universe = variable.universe
        self.memberships = variable.memberships
