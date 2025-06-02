from abc import abstractmethod

from transport.cli.adapter.cli_adapter import CreateVariableCLIAdapter
from transport.cli.validation.validate_create_variable_cli import isNameValid, isVariableTypeValid, isVariableUniverseValid, isMfValid

class CreateVariableCLI:
    def __init__(self, adapter:CreateVariableCLIAdapter):
        self.adapter = adapter
    def execute(self):
        name:str = self.getVariableName()
        if not name:
            print('User exits enter variable name.')
            return False
        var_type:str = self.getVariableType()
        if not var_type:
            print('User exits enter variable type.')
            return False
        universe:list[float] = self.getUniverse()
        if not universe:
            print('User exits enter universe.')
            return False
        mf:str = self.getMembershipFunction()
        if not mf:
            print('User exits enter membership function.')
            return False
        res = self.adapter.execute(name, var_type, universe, mf)
        print(f'Variable {res.name}: {res.type},{res.universe},{res.mf} successfully created.')
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
        while True:
            universe_string = input("Enter your universe [start, end, step] (q to quit): ")
            if universe_string == 'q':
                return False
            try:
                universe = self.parseStringUniverseReturnListFloat(universe_string)
                isVariableUniverseValid(universe)
                return universe
            except ValueError as e:
                print(f'Error: {e} Please try again.')

    @staticmethod
    def getMembershipFunction():
        while True:
            mf = input("Enter membership function type (q to quit): ")
            if mf == 'q':
                return False
            try:
                isMfValid(mf)
                return mf
            except ValueError as e:
                print(f'Error: {e} Please try again.')

    @staticmethod
    def parseStringUniverseReturnListFloat(string_universe:str)->list[float]:
        if not isinstance(string_universe,str) or not string_universe.strip():
            raise ValueError(f'Variable universe cannot be empty')
        try:
            elements = string_universe.split(',')
            if len(elements) != 3:
                raise ValueError
            return [float(value.strip()) for value in string_universe.split(',')]
        except ValueError:
            raise ValueError(f"Universe {string_universe} must be three numbers separated by commas (eg: 0,101,1).")
