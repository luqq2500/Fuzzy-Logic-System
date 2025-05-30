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
        return res

    def get_membership_level(self):
        level = input("Enter membership level: ")
        if self.isLevelValid(level):
            return int(level)
        else:
            raise ValueError(f'Membership level is invalid.')

    def get_mf_input(self):
        mf = input("Enter membership function type: ")
        if self.isMfValid(mf):
            return mf
        else:
            raise ValueError(f'Membership function type is invalid.')

    def get_ordinal_input(self, ordinals):
        ordinal = input("Enter ordinal: ")
        if self.isOrdinalValid(ordinal, ordinals):
            return ordinal
        else:
            raise ValueError(f'Ordinal is invalid.')

    def get_universe_input(self, universes, mf):
        string_universe = input("Enter universe [number, number,..., number]: ")
        if self.isUniverseValid(string_universe, universes, mf):
            universe = self.parse_universe_input(string_universe)
            return universe
        else:
            raise ValueError(f'Universe is invalid.')

    @staticmethod
    def isMfValid(mf):
        if mf not in ['trimf','trapmf']:
            raise ValueError(f'Membership function must be either trimf or trapmf.')
        return True

    @staticmethod
    def isLevelValid(level):
        if level>0:
            return True
        else:
            raise ValueError('Level cannot be negative nor zero.')

    @staticmethod
    def isOrdinalValid(ordinal, ordinals):
        if ordinal in ordinals:
            raise ValueError('Ordinal cannot have duplicates.')
        if int(ordinal):
            raise ValueError('Ordinal cannot be integer.')
        if ordinal == '' or ordinal == ' ':
            raise ValueError('Ordinal cannot be empty.')
        return True

    @staticmethod
    def isUniverseValid(universe_string, universes, mf):
        if not [float(value.strip()) for value in universe_string.split(',')]:
            raise ValueError('Universe value must only have digits, and divided by (,).')
        universe = [float(value.strip()) for value in universe_string.split(',')]
        if not all(universe[i]<=universe[i+1] for i in range(len(universe)-1)):
            raise ValueError('Universe must be incremental.')
        if all(universe[i]==universe[i+1] for i in range(len(universe)-1)):
            raise ValueError('Universe must have width.')
        if any(value<0 for value in universe):
            raise ValueError('Universe value cannot have negative value.')
        if universe in universes:
            raise ValueError('Universe value cannot have duplicates.')
        mf_len = {'trimf':3,'trapmf':4}
        if not len(universe) == mf_len[mf]:
            raise ValueError('Universe value does not have the expected length. Trimf = 3, Trapmf = 4.')
        return True

    @staticmethod
    def parse_universe_input(universe:str):
        return [float(value.strip()) for value in universe.split(',')]


