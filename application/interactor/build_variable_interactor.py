from models.membership import Membership
from models.membership_function import MembershipFunction
from models.variable import Variable

class BuildVariableInteractor:
    def __init__(self, director, repo):
        self.director = director
        self.repo = repo

    def execute(self, request):
        variable_object = Variable(request.name, request.variable_type, request.variable_universe)
        fuzzy_variable = self.director.createVariable(variable_object)
        mf = MembershipFunction(request.mf)
        for ordinal, universe in zip(request.ordinals, request.membership_universes):
            membership = Membership(ordinal, universe)
            self.director.addMembership(fuzzy_variable, mf, membership)
        self.repo.add(fuzzy_variable)