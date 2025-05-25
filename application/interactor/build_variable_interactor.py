from models.variable_membership import VariableMembership
from models.variable import Variable
from application.dto.response import CreateVariableResponse

class BuildVariableInteractor:
    def __init__(self, engine, repo):
        self.engine = engine
        self.repo = repo

    def execute(self, request):
        var =  Variable(request.name, request.variable_type, request.variable_universe)
        mem = VariableMembership(request.mf, request.membership_ordinals, request.membership_universes)
        var.fuzzy_variable = self.engine.buildVariable(var.name, var.type, var.universe)
        for ordinal, universe in mem.membership.items():
            var.fuzzy_variable[ordinal] = self.engine.addMembership(var.fuzzy_variable.universe, mem.mf, universe)
            var.memberships[ordinal] = var.fuzzy_variable[ordinal]
        self.repo.add(var)
        return CreateVariableResponse(var)