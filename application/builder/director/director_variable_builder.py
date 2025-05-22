class VariableBuilderDirector:
    def __init__(self, builder):
        self.builder = builder

    def buildVariable(self, variable, membership):
        return (self.builder.
                createVariable(variable).
                addMembership(membership).
                build())