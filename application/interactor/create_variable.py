from application.dto.response import CreateVariableResponse
from models.variable import Variable

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
