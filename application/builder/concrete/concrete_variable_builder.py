from application.builder.variable_builder_interface import VariableBuilderInterface

class VariableBuilder(VariableBuilderInterface):
    def __init__(self, fuzzy_engine):
        self._fuzzy_engine = fuzzy_engine

    def buildVariable(self, variable):
        variable.fuzzy_variable = self._fuzzy_engine.buildVariable(variable)
        return variable

    def addMembership(self, variable, mf, membership):
        variable.fuzzy_variable[membership.ordinal] = self._fuzzy_engine.addMembership(variable, mf, membership)
        return variable
