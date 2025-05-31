class DisplayVariableOrdinalCLI:
    def __init__(self, adapter):
        self.adapter = adapter

    def execute(self):
        res = self.adapter.execute()
        for var_name, membership in res.variableOrdinalForDisplay.items():
            print(f'Variable name: {var_name}\nMembership: ')
            for ordinal, value in membership.items():
                print(f'{ordinal}: {value}')