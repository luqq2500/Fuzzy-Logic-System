from abc import abstractmethod

from transport.cli.adapter.cli_adapter import CreateVariableCLIAdapter
from transport.cli.validation.validate_create_variable_cli import isNameValid, isVariableTypeValid, isVariableUniverseValid, isMfValid

class CreateVariableCLI:
    def __init__(self, adapter:CreateVariableCLIAdapter):
        self.adapter = adapter

    def execute(self):
        name:str = self.getVariableName()
        var_type:str = self.getVariableType()
        universe:list[float] = self.getUniverse()
        mf:str = self.getMembershipFunction()
        res = self.adapter.execute(name, var_type, universe, mf)
        print(f'Variable created: {res.name},{res.type},{res.mf},{res.universe},{res.fuzzy_var}')
        return res

    @abstractmethod
    def getVariableName(self):
        name = input("Enter variable name: ").lower()
        if not isNameValid(name):
            raise ValueError(f"Name: {name} is invalid. Please try again. ")
        return name

    @abstractmethod
    def getVariableType(self):
        variable_type = input("Enter your variable type: ").lower()
        if not isVariableTypeValid(variable_type):
            raise ValueError(f"Variable type: {variable_type} is invalid. Please try again.")
        return variable_type

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
