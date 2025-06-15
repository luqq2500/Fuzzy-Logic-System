from application.dto.response import FormatExistingAntecedentResponse
from infra.repository.repo_port import IRepository


class FormatExistingAntecedent:
    def __init__(self, repo:IRepository):
        self.repo = repo
        self.formatted_antecedent = {}
    def execute(self)->FormatExistingAntecedentResponse:
        variables = self.repo.getAll()
        for name, variable in variables.items():
            if variable.type == 'antecedent':
                self.formatted_antecedent[name] = [ordinal for ordinal in variable.memberships.keys()]
        return FormatExistingAntecedentResponse(formatted_antecedent=self.formatted_antecedent)