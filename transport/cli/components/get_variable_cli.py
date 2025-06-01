from transport.cli.strategy.get_variable_info_strategy import IGetVariableInfoStrategy

class GetVariableInfoCLI:
    def __init__(self, strategy:IGetVariableInfoStrategy):
        self.strategy = strategy
    def execute(self):
        self.strategy.setup()
        print(self.strategy.getTitle())
        finder = input(self.strategy.getInputHolder()).strip().lower()
        response = self.strategy.get(finder)
        print(f'Variable found: {response.name}, {response.type}, {response.universe}, {response.mf}')
        return response