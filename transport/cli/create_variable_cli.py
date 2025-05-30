class CreateVariableCLI:
    def __init__(self, adapter):
        self.adapter = adapter

    def execute(self):
        name = self.get_variable_name()
        var_type = self.get_variable_type()
        universe = self.get_variable_universe()
        res = self.adapter.execute(name, var_type, universe)
        return res

    def get_variable_name(self):
        name = input("Enter variable name: ").lower()
        if not self.isNameValid(name):
            raise ValueError(f"Name: {name} is invalid. Please try again. ")
        return name

    def get_variable_type(self):
        variable_type = input("Enter your variable type: ").lower()
        if not self.isVariableTypeValid(variable_type):
            raise ValueError(f"Variable type: {variable_type} is invalid. Please try again.")
        return variable_type

    def get_variable_universe(self):
        universe_string = input("Enter your universe (start, end, step): ")
        universe = self.parse_variable_universe_input(universe_string)
        if not self.isVariableUniverseValid(universe):
            raise ValueError(f"Variable universe: {universe} is invalid. Please try again.")
        return universe

    @staticmethod
    def parse_variable_universe_input(universe):
        try:
            return [float(value.strip()) for value in universe.split(',')]
        except ValueError:
            raise ValueError(f"Universe {universe} must separated by commas.")

    @staticmethod
    def isNameValid(name):
        for char in name:
            if char.isdigit():
                return False
        if not name or name == " " or name is None:
            return False
        return True

    @staticmethod
    def isVariableTypeValid(variable_type):
        if variable_type not in ['antecedent', 'consequent']:
            return False
        return True

    @staticmethod
    def isVariableUniverseValid(variable_universe):
        if not variable_universe:
            raise ValueError(f"Variable universe: {variable_universe} is invalid.")
        if not isinstance(variable_universe, list):
            raise ValueError(f"Variable universe: {variable_universe} must be a list.")
        for value in variable_universe:
            if not isinstance(value, int) or not isinstance(value, float):
                raise ValueError(f"Variable universe: {variable_universe} must be a list of numbers.")
        start = variable_universe[0]
        end = variable_universe[1]
        step = variable_universe[2]
        if start>end or step>(end-start):
            raise ValueError(f"Variable universe: {variable_universe} must be incremental.")
        if len(variable_universe)!=3:
            raise ValueError(f"Variable universe: {variable_universe} must be have three digits of start, end, step.")
        return True