from abc import ABC, abstractmethod
from typing import Union

from transport.cli.components.add_membership_cli import AddMembershipCLI
from transport.cli.components.create_variable_cli import CreateVariableCLI
from transport.cli.components.get_variable_cli import GetVariableInfoCLI

class IUserStrategyCLI(ABC):
    @abstractmethod
    def execute(self):pass
    @abstractmethod
    def getDescription(self)->str:pass

class UserCreateVariableCLI(IUserStrategyCLI):
    def __init__(self, create_var_cli:CreateVariableCLI):
        self.create_var_cli = create_var_cli
        self.desc = "Create variable only."
        self.level = 0
    def execute(self):
        if not self.getNumberOfVariablesToCreate():
            print('User exited the mode.')
            return False
        for i in range(self.level):
            self.create_var_cli.execute()
        return True
    def getDescription(self):
        return self.desc
    def getNumberOfVariablesToCreate(self):
        while True:
            level = input("How many variables do you want to create? (q to quit): ")
            if level.lower() == 'q':
                print(f"Quitting mode: {self.desc}")
                return False
            if not int(level):
                print("Input must be an integer. Try again.")
            if int(level) < 0:
                print("Input must be greater than 0. Try again.")
            if int(level) > 0:
                break
        self.level = int(level)
        return True

class UserPutVariableNameAddMembershipCLI(IUserStrategyCLI):
    def __init__(self, get_var_cli:GetVariableInfoCLI,add_membership_cli:AddMembershipCLI):
        self.get_var_cli = get_var_cli
        self.add_membership_cli = add_membership_cli
        self.desc = "Add membership to existing variables."
        self.zero_mem_vars:dict[str,list[Union[str,list[float]]]] = {}
    def execute(self):
        res = self.get_var_cli.execute()
        self.add_membership_cli.execute(res.name, res.mf)
        return True
    def getDescription(self):
        return self.desc

class UserCreateVariableAddMembershipCLI(IUserStrategyCLI):
    def __init__(self, create_var_cli:CreateVariableCLI, add_membership_cli:AddMembershipCLI):
        self.create_var_cli = create_var_cli
        self.add_membership_cli = add_membership_cli
        self.desc = "Create variable and add membership."
    def execute(self):
        res = self.create_var_cli.execute()
        self.add_membership_cli.execute(res.name, res.mf)
        return True
    def getDescription(self):
        return self.desc