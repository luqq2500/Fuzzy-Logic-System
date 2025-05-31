from abc import abstractmethod
from transport.cli.validation.validate_add_membership_cli import isLevelValid, isMfValid, isOrdinalValid, isUniverseValid

class AddMembershipCLI:
    def __init__(self, adapter):
        self.adapter = adapter

    def execute(self, var_name):
        mf = self.get_mf_input()
        level = self.get_membership_level()
        ordinals = []
        universes = []
        for i in range(level):
            ordinal = self.get_ordinal_input(ordinals)
            universe = self.get_universe_input(universes, mf)
            ordinals.append(ordinal)
            universes.append(universe)
        res = self.adapter.execute(var_name, mf, ordinals, universes)
        print(f'Membership added: {res.name},{res.memberships}')
        return res

    @staticmethod
    def get_membership_level():
        level = input("Enter membership level: ")
        if isLevelValid(level):
            return int(level)
        else:
            raise ValueError(f'Membership level is invalid.')

    @staticmethod
    def get_mf_input():
        mf = input("Enter membership function type: ")
        if isMfValid(mf):
            return mf
        else:
            raise ValueError(f'Membership function type is invalid.')

    @staticmethod
    def get_ordinal_input(ordinals):
        ordinal = input("Enter ordinal: ")
        if isOrdinalValid(ordinal, ordinals):
            return ordinal
        else:
            raise ValueError(f'Ordinal is invalid.')

    def get_universe_input(self,universes, mf):
        string_universe = input("Enter universe [number, number,..., number]: ")
        if isUniverseValid(string_universe, universes, mf):
            universe = self.parse_universe_input(string_universe)
            return universe
        else:
            raise ValueError(f'Universe is invalid.')

    @abstractmethod
    def parse_universe_input(self, universe:str):
        return [float(value.strip()) for value in universe.split(',')]



