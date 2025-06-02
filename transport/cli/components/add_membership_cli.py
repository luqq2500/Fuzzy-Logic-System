from abc import abstractmethod

from transport.cli.adapter.cli_adapter import AddMembershipCLIAdapter
from transport.cli.validation.validate_add_membership_cli import isLevelValid, isOrdinalValid, isUniverseValid

class AddMembershipCLI:
    def __init__(self, adapter:AddMembershipCLIAdapter):
        self.adapter = adapter

    def execute(self, var_name:str, mf:str):
        level = self.getMembershipLevel()
        ordinals = []
        universes = []
        for i in range(level):
            ordinal = self.getOrdinals(ordinals)
            universe = self.getUniverse(universes, mf)
            ordinals.append(ordinal)
            universes.append(universe)
        res = self.adapter.execute(var_name, mf, ordinals, universes)
        print(f'Membership added: {res.name},{res.memberships}')
        return res

    @staticmethod
    def getMembershipLevel():
        level = input("Enter membership level: ")
        if isLevelValid(level):
            return int(level)
        else:
            raise ValueError(f'Membership level is invalid.')

    @staticmethod
    def getOrdinals(ordinals):
        ordinal = input("Enter ordinal: ")
        if isOrdinalValid(ordinal, ordinals):
            return ordinal
        else:
            raise ValueError(f'Ordinal is invalid.')

    def getUniverse(self, universes, mf):
        string_universe = input("Enter universe [number, number,..., number]: ")
        if isUniverseValid(string_universe, universes, mf):
            universe = self.parseUniverseStringReturnListFloat(string_universe)
            return universe
        else:
            raise ValueError(f'Universe is invalid.')

    @abstractmethod
    def parseUniverseStringReturnListFloat(self, universe):
        return [float(value.strip()) for value in universe.split(',')]



