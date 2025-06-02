from application.dto.response import GetExistingVariableNameResponse

class GetExistingVariableName:
    def __init__(self, repo):
        self.repo = repo
        self.existingVariableName:list[str] = []
    def execute(self) -> GetExistingVariableNameResponse:
        variables = self.repo.getAll()
        for variable in variables:
            self.existingVariableName.append(variable)
        return GetExistingVariableNameResponse(existing_variable_name=self.existingVariableName)
