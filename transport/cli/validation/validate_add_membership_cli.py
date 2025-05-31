def isMfValid(mf):
    if mf not in ['trimf','trapmf']:
        raise ValueError(f'Membership function must be either trimf or trapmf.')
    return True

def isLevelValid(level):
    if int(level)>0:
        return True
    else:
        raise ValueError('Level must be integer, cannot be negative nor zero.')

def isOrdinalValid(ordinal, ordinals):
    if ordinal in ordinals:
        raise ValueError('Ordinal cannot have duplicates.')
    if isinstance(ordinal, int):
        raise ValueError('Ordinal cannot be integer.')
    if ordinal == '' or ordinal == ' ':
        raise ValueError('Ordinal cannot be empty.')
    return True

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