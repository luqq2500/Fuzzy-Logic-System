class BuildVariableRequest:
    def __init__(self, name: str, variable_type: str, variable_universe: list[float], mf: str, membership_ordinals: list[str], membership_universes: list[list[float]]):
        self.name = name
        self.variable_type = variable_type
        self.variable_universe = variable_universe
        self.mf = mf
        self.membership_ordinals = membership_ordinals
        self.membership_universes = membership_universes