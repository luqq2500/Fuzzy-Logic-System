def isNameValid(name):
    for char in name:
        if char.isdigit():
            return False
    if not name or name == " " or name is None:
        return False
    return True

def isVariableTypeValid(variable_type):
    if variable_type not in ['antecedent', 'consequent']:
        return False
    return True

def isVariableUniverseValid(variable_universe):
    if not variable_universe:
        raise ValueError(f"Variable universe: {variable_universe} is invalid.")
    if not isinstance(variable_universe, list):
        raise ValueError(f"Variable universe: {variable_universe} must be a list.")
    for value in variable_universe:
        if not isinstance(value, (int, float)):
            raise ValueError(f"Variable universe: {variable_universe} must be a list of numbers.")
    if len(variable_universe) != 3:
        raise ValueError(f"Variable universe: {variable_universe} must be a list of 3 numbers.")
    start = variable_universe[0]
    end = variable_universe[1]
    step = variable_universe[2]
    if start>end or step>(end-start):
        raise ValueError(f"Variable universe: {variable_universe} must be incremental.")
    if len(variable_universe)!=3:
        raise ValueError(f"Variable universe: {variable_universe} must be have three digits of start, end, step.")
    return True

def isMfValid(mf):
    if mf not in ['trimf','trapmf']:
        raise ValueError(f'Membership function must be either trimf or trapmf.')
    return True