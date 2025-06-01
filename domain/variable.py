from dataclasses import dataclass

@dataclass
class Variable:
    def __init__(self, name:str, variable_type:str, universe:list[float], mf:str):
        self.name:str = name
        self.type:str = variable_type
        self.universe:list[float] = universe
        self.mf:str = mf
        self.fuzzy_variable:object = None
        self.memberships:dict[str:object] = {} # {ordinal:var.fuzzy_var[ordinal]}

    def setFuzzyVariable(self,fuzzy_var:object) -> None:
        self.fuzzy_variable = fuzzy_var
    def setMembership(self,ordinal:str, membership:object) -> None:
        self.memberships[ordinal] = membership

    def getName(self) -> str:
        return self.name
    def getType(self) -> str:
        return self.type
    def getUniverse(self) -> list[float]:
        return self.universe
    def getMf(self) -> str:
        return self.mf
    def getFuzzyVariable(self) -> object:
        return self.fuzzy_variable
    def getMemberships(self) -> dict[str:object]:
        return self.memberships