from application.dto.response import AddMembershipResponse
from models.membership import Membership

class AddMembership:
    def __init__(self, engine, repo):
        self.engine = engine
        self.repo = repo
    def execute(self, req):
        var = req.var
        mem = Membership(req.mf, req.ordinals, req.universes)
        fuzzy_var_universe = var.fuzzy_variable.universe
        for ordinal, universe in mem.membership.items():
            mem_set = self.engine.addMembership(fuzzy_var_universe, mem.mf, universe)
            var.fuzzy_variable[ordinal] = mem_set
            var.memberships[ordinal] = var.fuzzy_variable[ordinal]
        self.repo.update(var)
        return AddMembershipResponse(var)
