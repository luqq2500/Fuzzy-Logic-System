import skfuzzy.control as controller
import skfuzzy as fuzzy
from infra.engine.fuzzy_engine_interface import FuzzyEngineInterface

class SkFuzzyEngine(FuzzyEngineInterface):
    def buildVariable(self, variable):
        if variable.type == 'antecedent':
            return controller.Antecedent(variable.universe, variable.name)
        elif variable.type == 'consequent':
            return controller.Consequent(variable.universe, variable.name)
        else:
            raise ValueError('Unknown variable type')

    def addMembership(self, variable, mf, membership):
        if mf.function == 'trimf':
            return fuzzy.trimf(variable.fuzzy_variable.universe, membership.universe)
        elif mf.function == 'trapmf':
            return fuzzy.trapmf(variable.fuzzy_variable.universe, membership.universe)
        else:
            raise ValueError('Unknown membership function')
