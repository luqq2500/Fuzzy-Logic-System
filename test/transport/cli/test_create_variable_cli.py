import pytest
from transport.cli.validation.create_variable_cli_validation import isNameValid, isVariableTypeValid, isVariableUniverseValid

class TestCreateVariableCLIValidator:
    def test_nameIsEmpty(self):
        name = ''
        assert isNameValid(name) is False

    def test_nameIsOnlyWhiteSpace(self):
        name = " "
        assert isNameValid(name) is False

    def test_nameHasDigit(self):
        name = "name778"
        assert isNameValid(name) is False

    def test_nameIsValid(self):
        name = 'temperature'
        assert isNameValid(name) is True

    def test_varTypeIsNull(self):
        var_type = None
        assert isVariableTypeValid(var_type) is False

    def test_varTypeIsNotAntecedentNorConsequent(self):
        var_type = 'idk'
        assert isVariableTypeValid(var_type) is False

    def test_varTypeIsValid(self):
        var_type_list = ['antecedent', 'consequent']
        for var_type in var_type_list:
            assert isVariableTypeValid(var_type) is True

    def test_universeIsNull(self):
        universe = []
        with pytest.raises(ValueError):
            isVariableUniverseValid(universe)

    def test_universeIsAList(self):
        universe = ('0', '101','1')
        with pytest.raises(ValueError):
            isVariableUniverseValid(universe)

    def test_universeValueIsNotNumber(self):
        universe = ['a','b','c']
        with pytest.raises(ValueError):
            isVariableUniverseValid(universe)

    def test_universeValueSequenceIsNotValid(self):
        universes = [[0,100,100],[0,40,100],[40,1,50]]
        for universe in universes:
            with pytest.raises(ValueError):
                isVariableUniverseValid(universe)
