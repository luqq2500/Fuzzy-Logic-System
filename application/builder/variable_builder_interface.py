from abc import ABC, abstractmethod

class VariableBuilderInterface(ABC):
    @abstractmethod
    def buildVariable(self, variable):...
    @abstractmethod
    def addMembership(self, variable, mf, membership):...
