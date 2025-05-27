class CreateVariableRequest:
    def __init__(self, name:str, var_type: str, universe: list[float]):
        self.name = name
        self.var_type = var_type
        self.universe = universe

class AddMembershipRequest:
    def __init__(self, var_name: str, mf: str, ordinals: list[str], universes: list[list[float]]):
        self.var_name = var_name # variable name will be pass to interactor, and get it via repo.
        self.mf = mf
        self.ordinals = ordinals
        self.universes = universes

class CreateRuleRequest:
    def __init__(self, name: str, var_logic_seq: list, con_var:float):
        self.name = name
        self.var_logic_seq = var_logic_seq # antecedent sequence of variable[ordinal]: float
        self.con_var = con_var