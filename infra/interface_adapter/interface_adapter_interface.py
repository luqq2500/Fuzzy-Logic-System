from abc import ABC, abstractmethod

class InterfaceAdapterInterface(ABC):
    @abstractmethod
    def execute(self, name, variable_type, variable_universe, mf, ordinals, membership_universes):...
