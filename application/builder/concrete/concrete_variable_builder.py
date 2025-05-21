from application.builder.variable_builder_interface import VariableBuilderInterface

class VariableBuilder(VariableBuilderInterface):
    def __init__(self, fuzzy_engine):
        self._fuzzy_engine = fuzzy_engine
        self._fuzzy_variable = None

    def buildVariable(self, variable):
        self.reset()
        variable.fuzzy_variable = self._fuzzy_engine.buildVariable(variable)
        self._fuzzy_variable = variable
        return self

    def addMembership(self, variable, mf, membership):
        self._fuzzy_variable = self._fuzzy_engine.addMembership(variable, mf, membership)
        return self

    def reset(self):
        self._fuzzy_variable = None

    def getFuzzyVariable(self):
        return self._fuzzy_variable