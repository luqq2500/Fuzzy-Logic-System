from typing import Union, Callable
from application.interactor.add_membership import AddMembership
from application.interactor.create_rule import CreateRule
from application.interactor.create_variable import CreateVariable
from application.interactor.format_existing_antecedent import FormatExistingAntecedent
from application.interactor.get_variable_info_by_name import GetVariableInfoByName
from transport.cli.dto.request import CreateVariableRequest, AddMembershipRequest, CreateRuleRequest, GetVariableInfoByNameRequest
from application.port.application_port import ICreateVariablePort, IAddMembershipPort, ICreateRulePort, IFormatExistingAntecedentPort, IGetVariableInfoByName


class CreateVariableCLIAdapter(ICreateVariablePort):
    def __init__(self, interactor:CreateVariable):
        self.interactor = interactor
    def execute(self, name:str, var_type:str, universe:list[float], mf:str):
        req = CreateVariableRequest(name=name, var_type=var_type, universe=universe, mf=mf)
        res = self.interactor.execute(req)
        return res

class AddMembershipCLIAdapter(IAddMembershipPort):
    def __init__(self,interactor:AddMembership):
        self.interactor = interactor
    def execute(self, var_name:str, mf:str, ordinals:list[str], universes:list[list[float]]):
        req = AddMembershipRequest(var_name=var_name, mf=mf, ordinals=ordinals, universes=universes)
        res = self.interactor.execute(req)
        return res

class CreateRuleCLIAdapter(ICreateRulePort):
    def __init__(self, interactor:CreateRule):
        self.interactor = interactor
    def execute(self, name:str, var_logic_seq:list[Union[str,Callable]], con_var):
        req = CreateRuleRequest(name=name, var_logic_seq=var_logic_seq, con_var=con_var)
        res = self.interactor.execute(req)
        return res

class FormatExistingAntecedentCLIAdapter(IFormatExistingAntecedentPort):
    def __init__(self, interactor:FormatExistingAntecedent):
        self.interactor = interactor
    def execute(self):
        res = self.interactor.execute()
        return res

class GetVariableInfoByNameCLIAdapter(IGetVariableInfoByName):
    def __init__(self, interactor:GetVariableInfoByName):
        self.interactor = interactor
    def execute(self, name):
        req = GetVariableInfoByNameRequest(name=name)
        res = self.interactor.execute(req)
        return res