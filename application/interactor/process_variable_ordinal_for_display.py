from application.dto.response import ProcessVariableOrdinalsForDisplayResponse
from application.interactor.get_all_antecedent_variable import GetAllExistingVariable

class ProcessAntecedentVariablesForDisplay:
    def __init__(self, repo):
        self.repo = repo
        self.variableOrdinalForDisplay = {}

    def execute(self):
        req = GetAllExistingVariable(self.repo).execute()
        variables = req.variables
        self.find_antecedent_and_fills_dictionary(variables)
        return ProcessVariableOrdinalsForDisplayResponse(self.variableOrdinalForDisplay)

    def find_antecedent_and_fills_dictionary(self, variables):
        for name, variable in variables.items():
            if variable.type == 'antecedent':
                self.variableOrdinalForDisplay[name] = [ordinal for ordinal in variable.memberships.keys()]