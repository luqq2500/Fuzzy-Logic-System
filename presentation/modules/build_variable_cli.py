def build_variable_cli(adapter):
    name, variable_type, variable_universe = get_create_variable_input()
    mf = get_mf_input()
    membership_ordinals, membership_universes = get_ordinal_universe_input()
    response = adapter.execute(name, variable_type, variable_universe, mf, membership_ordinals, membership_universes)
    return response

def get_create_variable_input():
    name = input("Enter variable name: ").lower()
    variable_type = input("Enter your variable type: ").lower()
    universe_string = input("Enter your universe (start, end, step): ")
    universe = parse_variable_universe_input(universe_string)
    if not isNameValid(name):
        raise ValueError(f"Name: {name} is invalid. Please try again. ")
    if not isVariableTypeValid(variable_type):
        raise ValueError(f"Variable type: {variable_type} is invalid. Please try again.")
    if not isVariableUniverseValid(universe):
        raise ValueError(f"Variable universe: {universe} is invalid. Please try again.")
    return name, variable_type, universe

def parse_variable_universe_input(universe):
    try:
        return [float(value.strip()) for value in universe.split(',')]
    except ValueError:
        raise ValueError(f"Universe {universe} must separated by commas.")

def isNameValid(name):
    for char in name:
        if char.isdigit():
            return False
    return True

def isVariableTypeValid(variable_type):
    if variable_type not in ['antecedent', 'consequent']:
        return False
    return True

def isVariableUniverseValid(variable_universe):
    start = variable_universe[0]
    end = variable_universe[1]
    step = variable_universe[2]
    if start<end or step>(end-start):
        raise ValueError(f"Variable universe: {variable_universe} must be incremental.")
    if len(variable_universe)!=3:
        raise ValueError(f"Variable universe: {variable_universe} must be have three digits of start, end, step.")
    return True

def get_mf_input():
    mf = input("Enter membership function type: ")
    if mf not in ['trimf', 'trapmf']:
        raise ValueError(f"Membership function must be either trimf or trapmf.")
    return mf

def get_ordinal_universe_input():
    level = get_membership_level()
    ordinals = []
    universes = []
    for i in range(level):
        ordinal = input("Enter ordinal: ")
        universe = input("Enter universe [number, number,..., number]: ")
        parsed_universe = parse_membership_universe_input(universe)
        if not isOrdinalValid(ordinal, ordinals):
            raise ValueError(f'Duplicate {ordinal} is invalid.')
        if not isMembershipUniverseValid(parsed_universe):
            raise ValueError(f'Universe {universe} is invalid.')
        ordinals.append(ordinal)
        universes.append(parsed_universe)
    return ordinals, universes

def get_membership_level():
    level = input("Enter membership level: ")
    try:
        return int(level)
    except ValueError:
        raise ValueError(f'Membership level must be an integer.')

def parse_membership_universe_input(universe):
    try:
        return [float(value.strip()) for value in universe.split(',')]
    except ValueError:
        raise ValueError(f'Membership universe: {universe} must separated by commas.')

def isOrdinalValid(ordinal, ordinals):
    return ordinal not in ordinals

def isMembershipUniverseValid(universe):
    if not all(universe[i]<=universe[i+1] for i in range(len(universe)-1)):
        return False
    if len(universe)<3 or len(universe)>4:
        return False
    return True