from abc import abstractmethod
from transport.cli.validation.validate_create_variable_cli import isNameValid, isVariableTypeValid,isVariableUniverseValid

class CreateVariableCLI:
    def __init__(self, adapter):
        self.adapter = adapter

    def execute(self):
        name = self.get_variable_name()
        var_type = self.get_variable_type()
        universe = self.get_variable_universe()
        res = self.adapter.execute(name, var_type, universe)
        print(f'Variable created: {res.name},{res.type},{res.universe},{res.fuzzy_var}')
        return res

    @abstractmethod
    def get_variable_name(self):
        name = input("Enter variable name: ").lower()
        if not isNameValid(name):
            raise ValueError(f"Name: {name} is invalid. Please try again. ")
        return name

    @abstractmethod
    def get_variable_type(self):
        variable_type = input("Enter your variable type: ").lower()
        if not isVariableTypeValid(variable_type):
            raise ValueError(f"Variable type: {variable_type} is invalid. Please try again.")
        return variable_type

    def get_variable_universe(self):
        universe_string = input("Enter your universe (start, end, step): ")
        universe = self.parse_variable_universe_input(universe_string)
        if not isVariableUniverseValid(universe):
            raise ValueError(f"Variable universe: {universe} is invalid. Please try again.")
        return universe

    @staticmethod
    def parse_variable_universe_input(universe):
        try:
            return [float(value.strip()) for value in universe.split(',')]
        except ValueError:
            raise ValueError(f"Universe {universe} must separated by commas.")
