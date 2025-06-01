from transport.cli.adapter.cli_adapter import FormatExistingAntecedentCLIAdapter

class DisplayExistingAntecedentCLI:
    def __init__(self, adapter:FormatExistingAntecedentCLIAdapter):
        self.adapter = adapter

    def execute(self):
        res = self.adapter.execute()
        for var_name, membership in res.formatted_antecedent.items():
            print(f'{var_name}: {membership}')