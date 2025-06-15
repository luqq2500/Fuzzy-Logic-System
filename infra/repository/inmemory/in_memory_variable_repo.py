from infra.repository.repo_port import IRepository

class InMemoryVariableRepository(IRepository):
    def __init__(self):
        self.memory = {}

    def add(self, variable):
        self.memory[variable.name] = variable

    def update(self, variable):
        for name in self.memory:
            if variable.name == name:
                self.memory[name] = variable

    def delete(self, name):
        del self.memory[name]

    def get(self, name):
        if name not in self.memory:
            return None
        return self.memory[name]

    def isExist(self, name) -> bool:
        return name in self.memory

    def getAll(self):
        return self.memory