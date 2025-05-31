from application.dto.response import ProcessVariableOrdinalsForDisplayResponse
from application.interactor.get_all_existing_variable import GetAllExistingVariable

# Display var_name: {str(ordinal):var[ordinal]}

class ProcessVariableOrdinalForDisplay:
    def __init__(self, repo):
        self.repo = repo
        self.variableOrdinalForDisplay = {}

    def execute(self):
        req = GetAllExistingVariable(self.repo).execute()
        variables = req.variables
        self.create_dictionary_for_display(variables)
        return ProcessVariableOrdinalsForDisplayResponse(self.variableOrdinalForDisplay)

    def create_dictionary_for_display(self, variables):
        for name, variable in variables.items():
            self.variableOrdinalForDisplay[name] = {ordinal:fuzzy_ordinal for ordinal, fuzzy_ordinal in variable.memberships.items()}