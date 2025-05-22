class VariableMembership:
    def __init__(self, mf, ordinals, universes):
        self.mf = mf
        self.membership = {ordinal:universe for ordinal, universe in zip(ordinals, universes)}