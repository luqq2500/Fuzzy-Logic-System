class VariableBuilder:
    def __init__(self, fuzzy_engine):
        self._fuzzy_engine = fuzzy_engine
        self._variable = None

    def createVariable(self, variable):
        self._variable = variable
        self._variable.fuzzy_variable = self._fuzzy_engine.buildVariable(self._variable)
        return self

    def addMembership(self, membership):
        for ordinal, universe in membership.membership.items():
            self._variable.fuzzy_variable[ordinal] = self._fuzzy_engine.addMembership(self._variable, membership.mf, universe)
            self._variable.memberships[ordinal] = self._variable.fuzzy_variable[ordinal]
        return self

    def setVariable(self, variable):
        self._variable = variable
        return self

    def build(self):
        return self._variable