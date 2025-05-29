from abc import ABC, abstractmethod

class ICreateVariable(ABC):
    @abstractmethod
    def execute(self, name, var_type, universe):...

class IAddMembership(ABC):
    @abstractmethod
    def execute(self, name: str, mf: str, ordinals: list[str], universes: list[list[float]]):...

class ICreateRule(ABC):
    @abstractmethod
    def execute(self, name: str, var_logic_seq: list, con_var: float):...