from dataclasses import dataclass

@dataclass
class CreateVariableResponse:
    name:str
    type:str
    universe:list[float]
    mf:str
    fuzzy_var:object

@dataclass
class AddMembershipResponse:
    name:str
    memberships:dict[str:object]

@dataclass
class CreateRuleResponse:
    name:str
    ant:object #rule.Antecedent
    con:object #rule.Consequent

@dataclass
class FormatExistingAntecedentResponse:
    formatted_antecedent:dict[str:list[str]]

@dataclass
class GetVariableInfoByNameResponse:
    name:str
    type:str
    universe:list[float]
    mf:str
    fuzzy_var:object

@dataclass
class GetExistingVariableNameResponse:
    existing_variable_name:list


