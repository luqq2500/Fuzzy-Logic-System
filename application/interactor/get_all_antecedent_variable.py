from application.dto.response import GetAllExistingVariableResponse

# Business application interactor: 'get existing variable objects'
# Used for: display existing variables, etc.
# Information required: None
# 1. Invoke repository method: getAll()
# 2. Pass to response dto.

class GetAllExistingVariable:
    def __init__(self, repo):
        self.repo = repo
    def execute(self):
        variables = self.repo.getAll()
        if variables == {}:
            raise ValueError('No variables found.')
        return GetAllExistingVariableResponse(variables)