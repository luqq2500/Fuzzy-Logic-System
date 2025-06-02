from transport.cli.strategy.get_variable_info_strategy import IGetVariableInfoStrategy

class GetVariableInfoCLI:
    def __init__(self, strategy:IGetVariableInfoStrategy):
        self.strategy = strategy
        self.elementToValidate = None
    def execute(self):
        self.strategy.setup()
        print(self.strategy.getTitle())
        finder = input(self.strategy.getInputHolder()).strip().lower()
        if finder in self.elementToValidate:
            print(f'Variable {finder} does not exist.')
            return False
        else:
            response = self.strategy.get(finder)
            print(f'Variable found: {response.name}, {response.type}, {response.universe}, {response.mf}')
            return response
    def setElementToValidate(self, elementToValidate:list[str]):
        self.elementToValidate = elementToValidate