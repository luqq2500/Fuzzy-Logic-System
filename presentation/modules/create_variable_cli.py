class CreateVariableCLI:
    def __init__(self, adapter):
        self.adapter = adapter

    def execute(self):
        name, var_type, universe = self.get_create_variable_input()
        res = self.adapter.execute(name, var_type, universe)
        return res

    def get_create_variable_input(self):
        name = input("Enter variable name: ").lower()
        variable_type = input("Enter your variable type: ").lower()
        universe_string = input("Enter your universe (start, end, step): ")
        universe = self.parse_variable_universe_input(universe_string)
        if not self.isNameValid(name):
            raise ValueError(f"Name: {name} is invalid. Please try again. ")
        if not self.isVariableTypeValid(variable_type):
            raise ValueError(f"Variable type: {variable_type} is invalid. Please try again.")
        if not self.isVariableUniverseValid(universe):
            raise ValueError(f"Variable universe: {universe} is invalid. Please try again.")
        return name, variable_type, universe

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
        return True

    @staticmethod
    def isVariableTypeValid(variable_type):
        if variable_type not in ['antecedent', 'consequent']:
            return False
        return True

    @staticmethod
    def isVariableUniverseValid(variable_universe):
        start = variable_universe[0]
        end = variable_universe[1]
        step = variable_universe[2]
        if start>end or step>(end-start):
            raise ValueError(f"Variable universe: {variable_universe} must be incremental.")
        if len(variable_universe)!=3:
            raise ValueError(f"Variable universe: {variable_universe} must be have three digits of start, end, step.")
        return True