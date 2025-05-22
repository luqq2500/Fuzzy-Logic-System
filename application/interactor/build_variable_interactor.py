from models.membership import Membership
from models.membership_function import MembershipFunction
from models.variable import Variable
from application.dto.response import CreateVariableResponse

class BuildVariableInteractor:
    def __init__(self, director, repo):
        self.director = director
        self.repo = repo

    def execute(self, request):
        variable_base = Variable(request.name, request.variable_type, request.variable_universe)
        variable = self.director.buildVariable(variable_base)
        mf = MembershipFunction(request.mf)
        for ordinal, universe in zip(request.ordinals, request.membership_universes):
            membership = Membership(ordinal, universe)
            variable = self.director.addMembership(variable, mf, membership)
            variable.memberships[ordinal] = variable.fuzzy_variable[ordinal]
        self.repo.add(variable)
        return CreateVariableResponse(variable)