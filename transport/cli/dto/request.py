from typing import Union, Callable
from dataclasses import dataclass

@dataclass
class CreateVariableRequest:
    name:str
    var_type:str
    universe:list[float]
    mf:str

@dataclass
class AddMembershipRequest:
    var_name:str # variable name will be pass to interactor, and get it via repo.
    mf:str
    ordinals:list[str]
    universes:list[list[float]]

@dataclass
class GetVariableInfoByNameRequest:
    name:str

@dataclass
class CreateRuleRequest:
    name:str
    var_logic_seq:list[Union[object,Callable]] # [var[ordinal],operator.logic_,...]
    con_var:object