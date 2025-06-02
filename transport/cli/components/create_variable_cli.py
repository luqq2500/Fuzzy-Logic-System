from abc import abstractmethod

from transport.cli.adapter.cli_adapter import CreateVariableCLIAdapter
from transport.cli.validation.validate_create_variable_cli import isNameValid, isVariableTypeValid, isVariableUniverseValid, isMfValid

class CreateVariableCLI:
    def __init__(self, adapter:CreateVariableCLIAdapter):
        self.adapter = adapter

    def execute(self):
        name:str = self.getVariableName()
        if not name:
            return False
        var_type:str = self.getVariableType()
        if not var_type:
            return False
        universe:list[float] = self.getUniverse()
        mf:str = self.getMembershipFunction()
        res = self.adapter.execute(name, var_type, universe, mf)
        print(f'Variable created: {res.name},{res.type},{res.mf},{res.universe},{res.fuzzy_var}')
        return res

    @abstractmethod
    def getVariableName(self):
        while True:
            name = input("Enter variable name (q to quit): ").lower()
            if name == 'q':
                return False
            try:
                isNameValid(name)
                return name
            except ValueError as e:
                print(f'Error: {e} Please try again.')

    @abstractmethod
    def getVariableType(self):
        while True:
            variable_type = input("Enter your variable type (q to quit): ").lower()
            if variable_type == 'q':
                return False
            try:
                isVariableTypeValid(variable_type)
                return variable_type
            except ValueError as e:
                print(f'Error: {e} Please try again.')

    def getUniverse(self):
        universe_string = input("Enter your universe (start, end, step): ")
        universe = self.parseStringUniverseReturnListFloat(universe_string)
        if not isVariableUniverseValid(universe):
            raise ValueError(f"Variable universe: {universe} is invalid. Please try again.")
        return universe

    @staticmethod
    def getMembershipFunction():
        mf = input("Enter membership function type: ")
        if isMfValid(mf):
            return mf
        else:
            raise ValueError(f'Membership function type is invalid.')

    @staticmethod
    def parseStringUniverseReturnListFloat(universe):
        try:
            return [float(value.strip()) for value in universe.split(',')]
        except ValueError:
            raise ValueError(f"Universe {universe} must separated by commas.")
