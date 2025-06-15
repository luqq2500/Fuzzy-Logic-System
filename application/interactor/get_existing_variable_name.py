from application.dto.response import GetExistingVariableNameResponse
from infra.repository.repo_port import IRepository


class GetExistingVariableName:
    def __init__(self, repo:IRepository):
        self.repo = repo
    def execute(self) -> GetExistingVariableNameResponse:
        existing_variable_name:list = []
        variables = self.repo.getAll()
        for variable in variables:
            existing_variable_name.append(variable)
        return GetExistingVariableNameResponse(existing_variable_name=existing_variable_name)
