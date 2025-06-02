from transport.cli.strategy.get_variable_info_strategy import IGetVariableInfoStrategy

class GetVariableInfoCLI:
    def __init__(self, strategy:IGetVariableInfoStrategy):
        self.strategy = strategy
        self.elementToValidate = set()
    def execute(self):
        self.strategy.setup()
        print(self.strategy.getTitle())
        finder = self.getVariableFinder()
        if not finder:
            print(f'User exits find variable name.')
            return False
        response = self.strategy.get(finder)
        print(f'Variable found: {response.name}, {response.type}, {response.universe}, {response.mf}')
        return response
    def getVariableFinder(self):
        while True:
            finder = input(self.strategy.getInputHolder() + ' (q to quit): ').strip().lower()
            if finder == 'q':
                return False
            if finder in self.elementToValidate:
                return finder
            else:
                print(f'Cannot retrieve {finder}. Please try again.')
    def setElementToValidate(self, elementToValidate:set):
        self.elementToValidate = elementToValidate