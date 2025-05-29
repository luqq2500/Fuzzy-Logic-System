from application.dto.request import CreateVariableRequest, AddMembershipRequest, CreateRuleRequest
from infra.transport.transport_adapter_interface import ICreateVariable, IAddMembership, ICreateRule

class CreateVariableCLIAdapter(ICreateVariable):
    def __init__(self, interactor):
        self.interactor = interactor
    def execute(self, name, var_type, universe):
        req = CreateVariableRequest(name=name, var_type=var_type, universe=universe)
        res = self.interactor.execute(req)
        return res

class AddMembershipCLIAdapter(IAddMembership):
    def __init__(self,interactor):
        self.interactor = interactor
    def execute(self, var_name, mf, ordinals, universes):
        req = AddMembershipRequest(var_name=var_name, mf=mf, ordinals=ordinals, universes=universes)
        res = self.interactor.execute(req)
        return res

class CreateRuleCLIAdapter(ICreateRule):
    def __init__(self, interactor):
        self.interactor = interactor
    def execute(self, var_set_seq, logic_seq, con_var):
        req = CreateRuleRequest(var_set_seq=var_set_seq, logic_seq=logic_seq, con_var=con_var)
        res = self.interactor.execute(req)
        return res
