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

class BuildRuleRequest:
    def __init__(self, var_seq: list[object], log_seq: list, con:object):
        self.var_seq = var_seq
        self.log_seq = log_seq
        self.con = con