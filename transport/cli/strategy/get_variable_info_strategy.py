from abc import ABC, abstractmethod
from transport.cli.adapter.cli_adapter import GetVariableInfoByNameCLIAdapter
from application.dto.response import GetVariableInfoByNameResponse

class IGetVariableInfoStrategy(ABC):
    @abstractmethod
    def setup(self):
        self.title:str
        self.input_holder:str
    @abstractmethod
    def get(self,finder):pass
    @abstractmethod
    def getTitle(self)->str:pass
    @abstractmethod
    def getInputHolder(self)->str:pass

class GetVariableInfoByNameStrategy(IGetVariableInfoStrategy):
    def __init__(self, adapter:GetVariableInfoByNameCLIAdapter):
        self.adapter = adapter
        self.title = None
        self.input_holder = None
    def setup(self):
        self.title = 'Mode: Retrieve variable by name.'
        self.input_holder = 'Enter variable name for retrieval'
    def get(self,name:str) -> GetVariableInfoByNameResponse:
        response = self.adapter.execute(name)
        return response
    def getTitle(self)->str:
        return self.title
    def getInputHolder(self)->str:
        return self.input_holder