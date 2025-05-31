from application.dto.response import FormatExistingAntecedentForDisplayResponse

class FormatExistingAntecedentForDisplay:
    def __init__(self, repo):
        self.repo = repo
        self.formatted_antecedent = {}

    def execute(self):
        variables = self.repo.getAll()
        for name, variable in variables.items():
            if variable.type == 'antecedent':
                self.formatted_antecedent[name] = [ordinal for ordinal in variable.memberships.keys()]
        return FormatExistingAntecedentForDisplayResponse(self.formatted_antecedent)
