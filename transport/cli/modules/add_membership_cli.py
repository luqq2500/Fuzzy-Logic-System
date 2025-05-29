class AddMembershipCLI:
    def __init__(self, adapter):
        self.adapter = adapter

    def execute(self, var_name):
        mf = self.get_mf_input()
        ordinals, universes = self.get_ordinal_universe_input()
        res = self.adapter.execute(var_name, mf, ordinals, universes)
        return res

    @staticmethod
    def get_mf_input():
        mf = input("Enter membership function type: ")
        if mf not in ['trimf', 'trapmf']:
            raise ValueError(f"Membership function must be either trimf or trapmf.")
        return mf

    def get_ordinal_universe_input(self):
        level = self.get_membership_level()
        ordinals = []
        universes = []
        for i in range(level):
            ordinal = input("Enter ordinal: ")
            universe = input("Enter universe [number, number,..., number]: ")
            parsed_universe = self.parse_membership_universe_input(universe)
            if not self.isOrdinalValid(ordinal, ordinals):
                raise ValueError(f'Duplicate {ordinal} is invalid.')
            if not self.isMembershipUniverseValid(parsed_universe):
                raise ValueError(f'Universe {universe} is invalid.')
            ordinals.append(ordinal)
            universes.append(parsed_universe)
        return ordinals, universes

    @staticmethod
    def get_membership_level():
        level = input("Enter membership level: ")
        try:
            return int(level)
        except ValueError:
            raise ValueError(f'Membership level must be an integer.')

    @staticmethod
    def parse_membership_universe_input(universe):
        try:
            return [float(value.strip()) for value in universe.split(',')]
        except ValueError:
            raise ValueError(f'Membership universe: {universe} must separated by commas.')

    @staticmethod
    def isOrdinalValid(ordinal, ordinals):
        return ordinal not in ordinals

    @staticmethod
    def isMembershipUniverseValid(universe):
        if not all(universe[i]<=universe[i+1] for i in range(len(universe)-1)):
            return False
        if len(universe)<3 or len(universe)>4:
            return False
        return True