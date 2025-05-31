class DisplayVariableOrdinalCLI:
    def __init__(self, adapter):
        self.adapter = adapter

    def execute(self):
        res = self.adapter.execute()
        for var_name, membership in res.variableOrdinalForDisplay.items():
            print(f'{var_name}: {membership}')