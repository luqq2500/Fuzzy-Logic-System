from application.dto.request import CreateVariableRequest, AddMembershipRequest
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
    def execute(self, var_name, mf, ordinals, universes):
        req = AddMembershipRequest(var_name=var_name, mf=mf, ordinals=ordinals, universes=universes)
        res = self.interactor.execute(req)
        return res