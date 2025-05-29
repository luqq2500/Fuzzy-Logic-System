from abc import ABC, abstractmethod

class ICreateVariablePort(ABC):
    @abstractmethod
    def execute(self, name: str, var_type: str, universe: list[float]):...

class IAddMembershipPort(ABC):
    @abstractmethod
    def execute(self, name: str, mf: str, ordinals: list[str], universes: list[list[float]]):...

class ICreateRulePort(ABC):
    @abstractmethod
    def execute(self, name: str, var_logic_seq: list, con_var: float):...