from models.variable_membership import VariableMembership
from models.variable import Variable
from application.dto.response import CreateVariableResponse

class BuildVariableInteractor:
    def __init__(self, director, repo):
        self.director = director
        self.repo = repo

    def execute(self, request):
        variable_base = Variable(request.name, request.variable_type, request.variable_universe)
        variable_membership_base = VariableMembership(request.mf, request.membership_ordinals, request.membership_universes)
        variable = self.director.buildVariable(variable_base, variable_membership_base)
        self.repo.add(variable)
        return CreateVariableResponse(variable)