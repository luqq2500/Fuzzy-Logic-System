class CLIStrategy:
    def __init__(self, create_variable_cli, add_membership_cli, display_variable_ordinal_cli):
        self.create_variable = create_variable_cli
        self.add_membership = add_membership_cli
        self.display_variable_ordinal = display_variable_ordinal_cli

    def createVariableAlone(self):
        self.create_variable.execute()

    def createVariableAndAddMembership(self):
        res = self.create_variable.execute()
        self.add_membership.execute(res.name)
        self.display_variable_ordinal.execute()