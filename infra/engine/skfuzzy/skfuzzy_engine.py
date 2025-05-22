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

    def addMembership(self, variable, mf, universe):
        if mf == 'trimf':
            return fuzzy.trimf(variable.fuzzy_variable.universe, universe)
        elif mf == 'trapmf':
            return fuzzy.trapmf(variable.fuzzy_variable.universe, universe)
        else:
            raise ValueError('Unknown membership function')
