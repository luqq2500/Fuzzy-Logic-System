class VariableBuilderDirector:
    def __init__(self, builder):
        self.builder = builder

    def buildVariable(self, variable, membership):
        return (self.builder.
                createVariable(variable).
                addMembership(membership).
                build())

    def createVariable(self, variable):
        return (self.builder.
               createVariable(variable).
               build())

    def addMembershipExistingVariable(self, variable, membership):
        return (self.builder.
                setVariable(variable).
                addMembership(membership).
                build())