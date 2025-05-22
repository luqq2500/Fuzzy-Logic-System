class VariableBuilderDirector:
    def __init__(self, builder):
        self.builder = builder

    def buildVariable(self, variable):
        return (self.builder.
                buildVariable(variable))

    def addMembership(self, variable, mf, membership):
        return (self.builder.
                addMembership(variable, mf, membership))