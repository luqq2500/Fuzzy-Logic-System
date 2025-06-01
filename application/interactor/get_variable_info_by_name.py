from application.dto.response import GetVariableInfoByNameResponse

class GetVariableInfoByName:
    def __init__(self, repo):
        self.repo = repo
    def execute(self, req)->GetVariableInfoByNameResponse:
        name = req.name
        variable = self.repo.get(name)
        if variable is None:
            raise ValueError(f'Variable {name} does not exist.')
        return GetVariableInfoByNameResponse(
            name=variable.getName(),
            type=variable.getType(),
            universe=variable.getUniverse(),
            mf=variable.getMf(),
            fuzzy_var=variable.getFuzzyVariable()
        )



