from application.dto.request import BuildVariableRequest
from infra.interface_adapter.interface_adapter_interface import InterfaceAdapterInterface

class BuildVariableCLIAdapter(InterfaceAdapterInterface):
    def __init__(self, interactor):
        self.interactor = interactor
    def execute(self, name, variable_type, variable_universe, mf, ordinals, membership_universes):
        request = BuildVariableRequest(name=name, variable_type=variable_type, variable_universe=variable_universe, mf=mf, ordinals=ordinals, membership_universes=membership_universes)
        response = self.interactor.execute(request)
        return response