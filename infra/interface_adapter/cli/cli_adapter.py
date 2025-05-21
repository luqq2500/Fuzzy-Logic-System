from application.dto.request import BuildVariableRequest

class BuildVariableCLIAdapter:
    def __init__(self, interactor):
        self.interactor = interactor
    def run(self, name, variable_type, variable_universe, mf, ordinals, membership_universes):
        request = BuildVariableRequest(name=name, variable_type=variable_type, variable_universe=variable_universe, mf=mf, ordinals=ordinals, membership_universes=membership_universes)
        self.interactor.execute(request)