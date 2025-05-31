import pytest
from transport.cli.validation.validate_add_membership_cli import isMfValid, isLevelValid, isOrdinalValid, isUniverseValid

class TestAddMembershipCLIValidator:
    def test_mfNotTrimfNorTrapmf(self):
        mf = 'idk'
        with pytest.raises(ValueError):
            isMfValid(mf)

    def test_mfIsNullOrWhitespace(self):
        mfs = ['', ' ']
        for mf in mfs:
            with pytest.raises(ValueError):
                isMfValid(mf)

    def test_mfIsValid(self):
        mfs = ['trimf', 'trapmf']
        for mf in mfs:
            assert isMfValid(mf) is True

    def test_levelIsNegativeOrZero(self):
        levels = [-1,0]
        for level in levels:
            with pytest.raises(ValueError):
                isLevelValid(level)

    def test_ordinalDuplicated(self):
        ordinals = ['temperature']
        ordinal = 'temperature'
        with pytest.raises(ValueError):
            isOrdinalValid(ordinal, ordinals)

    def test_ordinalIsANumber(self):
        ordinals = []
        ordinal = '99'
        with pytest.raises(ValueError):
            isOrdinalValid(ordinal, ordinals)

    def test_ordinalIsWhitespace(self):
        ordinals = []
        ordinal_list = ['',' ']
        for ordinal in ordinal_list:
            with pytest.raises(ValueError):
                isOrdinalValid(ordinal, ordinals)

    def test_universeHasNonDigitValue(self):
        universes = ['@, ..., #','a,b,c','0,10,c']
        for universe in universes:
            with pytest.raises(ValueError):
                isUniverseValid(universe, universes=None, mf=None)

    def test_universeIsNotIncremental(self):
        universes = []
        universe_list = ['0, 8, 2','3, 0, 0', '0,0,0']
        for universe in universe_list:
            with pytest.raises(ValueError):
                isUniverseValid(universe, universes, mf=None)

    def test_universeHasNegativeValue(self):
        universe = '-1,9,10'
        with pytest.raises(ValueError):
            isUniverseValid(universe, universes=None, mf=None)

    def test_universeHasDuplicates(self):
        universes = [[0,5,10]]
        universe = '0,5,10'
        with pytest.raises(ValueError):
            isUniverseValid(universe, universes=universes, mf=None)

    def test_universeLengthNotFollowsMembershipFunction(self):
        universes = []
        universe = '0,5,10,15'
        mf = 'trimf'
        with pytest.raises(ValueError):
            isUniverseValid(universe, universes=universes, mf=mf)

    def test_universeIsValid(self):
        universes = []
        mf = 'trimf'
        universe = '0,5,10'
        assert isUniverseValid(universe, universes, mf) is True







