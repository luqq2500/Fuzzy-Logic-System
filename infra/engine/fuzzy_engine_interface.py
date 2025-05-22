from abc import ABC, abstractmethod

class FuzzyEngineInterface(ABC):
    @abstractmethod
    def buildVariable(self, variable):...
    @abstractmethod
    def addMembership(self, variable, mf, membership):...
