import skfuzzy.control as controller
import skfuzzy as fuzzy
from infra.engine.fuzzy_engine_interface import FuzzyEngineInterface

class SkFuzzyEngine(FuzzyEngineInterface):

    def createVariable(self, name, var_type, universe):
        if var_type == 'antecedent':
            return controller.Antecedent(universe, name)
        elif var_type == 'consequent':
            return controller.Consequent(universe, name)
        else:
            raise ValueError(f'Invalid type: {var_type}.')

    def addMembership(self, fuzzy_var_universe, mf, universe):
        if mf == 'trimf':
            return fuzzy.trimf(fuzzy_var_universe, universe)
        elif mf == 'trapmf':
            return fuzzy.trapmf(fuzzy_var_universe, universe)
        else:
            raise ValueError(f'Invalid function: {mf}')

    def createRule(self, ant, con):
        return controller.Rule(ant, con)
