from application.dto.response import AddMembershipResponse
from domain.membership import Membership


# This is 'add membership' business application code.
# Information required: variable name, membership function, list of ordinals, list of universes.
# 1. Get user input via dto.
# 2. Get variable object from variable name.
# 3. Get fuzzy variable universe.
# 3. Create membership object.
# 5. Update fuzzy_variable membership using engine method: addMembership.
# 7. Add membership ordinal:universe in variable memberships.
# 8. Update variable object via variable repo.


class AddMembership:
    def __init__(self, engine, repo):
        self.engine = engine
        self.repo = repo
    def execute(self, req):
        var = self.repo.get(req.var_name)
        fuzzy_var_universe = var.fuzzy_variable.universe
        mem = Membership(req.mf, req.ordinals, req.universes)
        for ordinal, universe in mem.membership.items():
            mem_set = self.engine.addMembership(fuzzy_var_universe, mem.mf, universe)
            var.fuzzy_variable[ordinal] = mem_set
            var.memberships[ordinal] = var.fuzzy_variable[ordinal]
        self.repo.update(var)
        return AddMembershipResponse(var)
