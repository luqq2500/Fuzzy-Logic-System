from application.dto.response import CreateVariableResponse
from domain.variable import Variable
from infra.engine.fuzzy_engine_interface import IFuzzyEnginePort
from infra.repository.repo_port import IVariableRepositoryPort
from transport.cli.dto.request import CreateVariableRequest


# This is 'create variable' business application code.
# Information required: name, variable type, and universe.
# 1. Get user input from dto: name, variable type, universe
# 2. Create fuzzy variable using engine method: createVariable
# 3. Add fuzzy variable in variable attribute fuzzy_variable
# 4. Add variable object in variable repository
# 5. Return response object of name, variable type, universe, and fuzzy_variable.


class CreateVariable:
    def __init__(self, engine:IFuzzyEnginePort, repo:IVariableRepositoryPort):
        self.engine = engine
        self.repo = repo

    def execute(self, req:CreateVariableRequest)->CreateVariableResponse:
        variable = Variable(req.name, req.var_type, req.universe, req.mf)
        name = variable.getName()
        var_type = variable.getType()
        universe = variable.getUniverse()
        fuzzy_var = self.engine.createVariable(name, var_type, universe)
        variable.setFuzzyVariable(fuzzy_var)
        self.repo.add(variable)
        return CreateVariableResponse(
            name=variable.getName(),
            type=variable.getType(),
            universe=variable.getUniverse(),
            mf=variable.getMf(),
            fuzzy_var=variable.getFuzzyVariable()
        )
