class VariableBuilderDirector:
    def __init__(self, builder):
        self.builder = builder

    def createVariable(self, variable):
        return (self.builder.
                buildVariable(variable).
                getFuzzyVariable())

    def addMembership(self, variable, mf, membership):
        return (self.builder.
                addMembership(variable, mf, membership))