from abc import ABC, abstractmethod
from typing import Union, Callable


class ICreateVariablePort(ABC):
    @abstractmethod
    def execute(self, name: str, var_type: str, universe: list[float], mf:str):...

class IAddMembershipPort(ABC):
    @abstractmethod
    def execute(self, name: str, mf: str, ordinals: list[str], universes: list[list[float]]):...

class ICreateRulePort(ABC):
    @abstractmethod
    def execute(self, name: str, var_logic_seq: list[Union[object,Callable]], con_var: float):...

class IFormatExistingAntecedentPort(ABC):
    @abstractmethod
    def execute(self):...

class IGetVariableInfoByName(ABC):
    @abstractmethod
    def execute(self, name: str):...

class IGetAllZeroMembershipVariable(ABC):
    @abstractmethod
    def execute(self):...

class IGetExistingVariableName(ABC):
    @abstractmethod
    def execute(self):...