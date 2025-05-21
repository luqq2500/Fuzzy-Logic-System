import skfuzzy.control as controller
import skfuzzy as fuzzy
from infra.engine_adapter.fuzzy_engine_interface import FuzzyEngineInterface

class SkFuzzyEngine(FuzzyEngineInterface):
    def buildVariable(self, variable):
        if variable.variable_type == 'antecedent':
            fuzzy_variable = controller.Antecedent(variable.universe, variable.name)
        elif variable.variable_type == 'consequent':
            fuzzy_variable = controller.Consequent(variable.universe, variable.name)
        else:
            raise ValueError('Unknown variable type')
        return fuzzy_variable

    def addMembership(self, variable, mf, membership):
        if mf.membership_function == 'trimf':
            variable.fuzzy_variable[membership.ordinal] = fuzzy.trimf(variable.fuzzy_variable.universe, membership.universe)
        elif mf.membership_function == 'trapmf':
            variable.fuzzy_variable[membership.ordinal] = fuzzy.trapmf(variable.fuzzy_variable.universe, membership.universe)
        return variable

