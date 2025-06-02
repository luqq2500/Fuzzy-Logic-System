from application.dto.response import GetExistingVariableNameResponse

class GetExistingVariableName:
    def __init__(self, repo):
        self.repo = repo
    def execute(self) -> GetExistingVariableNameResponse:
        existing_variable_name:list = []
        variables = self.repo.getAll()
        for variable in variables:
            existing_variable_name.append(variable)
        return GetExistingVariableNameResponse(existing_variable_name=existing_variable_name)
