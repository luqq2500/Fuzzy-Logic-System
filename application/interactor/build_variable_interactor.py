import numpy as np
from models.variable_membership import VariableMembership
from models.variable import Variable
from application.dto.response import CreateVariableResponse

class BuildVariableInteractor:
    def __init__(self, engine, repo):
        self.engine = engine
        self.repo = repo

    def execute(self, request):
        start, end, step = request.variable_universe
        var =  Variable(request.name, request.variable_type, np.arange(start, end, step))
        mem = VariableMembership(request.mf, request.membership_ordinals, request.membership_universes)
        fuzzy_var = self.engine.buildVariable(var.name, var.type, var.universe)
        var.fuzzy_variable = fuzzy_var
        for ordinal, universe in mem.membership.items():
            mem_set = self.engine.addMembership(var.fuzzy_variable.universe, mem.mf, universe)
            var.fuzzy_variable[ordinal] = mem_set
            var.memberships[ordinal] = var.fuzzy_variable[ordinal]
        self.repo.add(var)
        return CreateVariableResponse(var)