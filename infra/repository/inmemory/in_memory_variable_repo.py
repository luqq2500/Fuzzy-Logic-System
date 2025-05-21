from infra.repository.variable_repo_interface import VariableRepositoryInterface

class InMemoryVariableRepository(VariableRepositoryInterface):
    def __init__(self):
        self.memory = {}

    def add(self, variable):
        print(f'{variable.name} has successfully added!')
        self.memory[variable.name] = variable

    def update(self, variable):
        for name in self.memory:
            if variable.name == name:
                self.memory[name] = variable

    def delete(self, name):
        del self.memory[name]

    def get(self, name):
        return self.memory[name]

    def isExist(self, name) -> bool:
        return name in self.memory

    def getAll(self):
        return self.memory