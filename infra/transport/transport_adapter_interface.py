from abc import ABC, abstractmethod

class ITransportAdapter(ABC):
    @abstractmethod
    def execute(self, **kwargs):...