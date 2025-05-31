from application.dto.request import CreateVariableRequest, AddMembershipRequest, CreateRuleRequest
from transport.port import ICreateVariablePort, IAddMembershipPort, ICreateRulePort, IDisplayVariableOrdinalPort


class CreateVariableCLIAdapter(ICreateVariablePort):
    def __init__(self, interactor):
        self.interactor = interactor
    def execute(self, name, var_type, universe):
        req = CreateVariableRequest(name=name, var_type=var_type, universe=universe)
        res = self.interactor.execute(req)
        return res

class AddMembershipCLIAdapter(IAddMembershipPort):
    def __init__(self,interactor):
        self.interactor = interactor
    def execute(self, var_name, mf, ordinals, universes):
        req = AddMembershipRequest(var_name=var_name, mf=mf, ordinals=ordinals, universes=universes)
        res = self.interactor.execute(req)
        return res

class CreateRuleCLIAdapter(ICreateRulePort):
    def __init__(self, interactor):
        self.interactor = interactor
    def execute(self, name, var_logic_seq, con_var):
        req = CreateRuleRequest(name=name, var_logic_seq=var_logic_seq, con_var=con_var)
        res = self.interactor.execute(req)
        return res

class DisplayVariableOrdinalCLIAdapter(IDisplayVariableOrdinalPort):
    def __init__(self, interactor):
        self.interactor = interactor
    def execute(self):
        res = self.interactor.execute()
        return res