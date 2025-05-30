import pytest

from transport.cli.create_variable_cli import CreateVariableCLI

class MockAdapter:
    @staticmethod
    def execute(name, var_type, universe):
        return f"Created: {name} {var_type} {universe}"

class TestCreateVariable:
    def setup_method(self):
        self.cli = CreateVariableCLI(MockAdapter())

    def test_nameIsEmpty(self):
        name = None
        assert self.cli.isNameValid(name) is False

    def test_nameIsOnlyWhiteSpace(self):
        name = " "
        assert self.cli.isNameValid(name) is False

    def test_nameHasDigit(self):
        name = "name778"
        assert self.cli.isNameValid(name) is False

    def test_nameIsValid(self):
        name = 'temperature'
        assert self.cli.isNameValid(name) is True

    def test_varTypeIsNull(self):
        var_type = None
        assert self.cli.isVariableTypeValid(var_type) is False

    def test_varTypeIsNotAntecedentNorConsequent(self):
        var_type = 'idk'
        assert self.cli.isVariableTypeValid(var_type) is False

    def test_varTypeIsValid(self):
        var_type_list = ['antecedent', 'consequent']
        for var_type in var_type_list:
            assert self.cli.isVariableTypeValid(var_type) is True

    def test_universeIsNull(self):
        universe = []
        with pytest.raises(ValueError):
            self.cli.isVariableUniverseValid(universe)

    def test_universeIsAList(self):
        universe = ('0', '101','1')
        with pytest.raises(ValueError):
            self.cli.isVariableUniverseValid(universe)

    def test_universeValueIsNotNumber(self):
        universe = ['a','b','c']
        with pytest.raises(ValueError):
            self.cli.isVariableUniverseValid(universe)

    def test_universeValueSequenceIsNotValid(self):
        universes = [[0,100,100],[0,40,100],[40,1,50]]
        for universe in universes:
            with pytest.raises(ValueError):
                self.cli.isVariableUniverseValid(universe)