from application.dto.request import BuildVariableRequest, CreateVariableRequest, AddMembershipRequest
from infra.transport.transport_adapter_interface import ITransportAdapter

class CreateVariableCLIAdapter(ITransportAdapter):
    def __init__(self, interactor):
        self.interactor = interactor
    def execute(self, name, var_type, universe):
        req = CreateVariableRequest(name=name, var_type=var_type, universe=universe)
        res = self.interactor.execute(req)
        return res

class AddMembershipCLIAdapter(ITransportAdapter):
    def __init__(self,interactor):
        self.interactor = interactor
    def execute(self, var, mf, ordinals, universes):
        req = AddMembershipRequest(var=var, mf=mf, ordinals=ordinals, universes=universes)
        res = self.interactor.execute(req)
        return res