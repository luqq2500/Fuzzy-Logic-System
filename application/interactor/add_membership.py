from application.dto.response import AddMembershipResponse
from infra.engine.fuzzy_engine_interface import IFuzzyEnginePort
from infra.repository.repo_port import IRepository
from transport.cli.dto.request import AddMembershipRequest


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
    def __init__(self, engine:IFuzzyEnginePort, repo:IRepository):
        self.engine = engine
        self.repo = repo
    def execute(self, req:AddMembershipRequest)->AddMembershipResponse:
        variable = self.repo.get(req.var_name)
        fuzzy_var_universe = variable.fuzzy_variable.universe
        mf = req.mf
        for ordinal, universe in zip(req.ordinals, req.universes):
            mem_set = self.engine.addMembership(fuzzy_var_universe, mf, universe)
            variable.fuzzy_variable[ordinal] = mem_set
            variable.memberships[ordinal] = variable.fuzzy_variable[ordinal]
        self.repo.update(variable)
        return AddMembershipResponse(
            name=variable.getName(),
            memberships=variable.getMemberships()
        )

