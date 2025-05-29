from application.dto.response import CreateVariableResponse
from domain.variable import Variable


# This is 'create variable' business application code.
# Information required: name, variable type, and universe.
# 1. Get user input from dto: name, variable type, universe
# 2. Create fuzzy variable using engine method: createVariable
# 3. Add fuzzy variable in variable attribute fuzzy_variable
# 4. Add variable object in variable repository
# 5. Return response object of name, variable type, universe, and fuzzy_variable.


class CreateVariable:
    def __init__(self, engine, repo):
        self.engine = engine
        self.repo = repo

    def execute(self, req):
        var = Variable(req.name, req.var_type, req.universe)
        fuzzy_var = self.engine.createVariable(var.name, var.type, var.universe)
        var.fuzzy_variable = fuzzy_var
        self.repo.add(var)
        return CreateVariableResponse(var)
