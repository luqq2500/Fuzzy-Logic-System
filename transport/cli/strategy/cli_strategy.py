class CLIStrategy:
    def __init__(self, create_variable_cli, add_membership_cli, display_existing_antecedent_cli):
        self.create_variable = create_variable_cli
        self.add_membership = add_membership_cli
        self.display_existing_antecedent = display_existing_antecedent_cli

    def createVariableAlone(self):
        self.create_variable.execute()

    def createVariableAndAddMembership(self):
        i = int(input("Number of variables to create: "))
        for _ in range(i):
            res = self.create_variable.execute()
            self.add_membership.execute(res.name)
        self.display_existing_antecedent.execute()