from abc import ABC, abstractmethod
from transport.cli.components.get_existing_variable_name_cli import GetExistingVariableNameCLI
from transport.cli.components.add_membership_cli import AddMembershipCLI
from transport.cli.components.create_variable_cli import CreateVariableCLI
from transport.cli.components.get_variable_info_cli import GetVariableInfoCLI

class IUserStrategyCLI(ABC):
    @abstractmethod
    def execute(self):pass
    @abstractmethod
    def getDescription(self)->str:pass

class UserCreateVariableCLI(IUserStrategyCLI):
    def __init__(self, create_var_cli:CreateVariableCLI):
        self.create_var_cli = create_var_cli
        self.desc = "Create variable only"
        self.level = 0
    def execute(self):
        if not self.getNumberOfVariablesToCreate():
            print('User exited the mode.')
            return False
        for i in range(self.level):
            if self.create_var_cli.execute() is False:
                print('Variable creation canceled.')
                return False
        return True
    def getDescription(self):
        return self.desc
    def getNumberOfVariablesToCreate(self):
        while True:
            level = input("How many variables do you want to create? (q to quit): ").strip()
            if level.lower() == 'q':
                print(f"Quitting mode: {self.desc}")
                return False
            try:
                int_level = int(level)
                if int_level <= 0:
                    raise ValueError(f'Level must be digit that is greater than 0.')
                self.level = int_level
                return True
            except ValueError as e:
                print(f'Error: {e}')

class UserPutVariableNameAddMembershipCLI(IUserStrategyCLI):
    def __init__(self, get_exist_var_name_cli: GetExistingVariableNameCLI, get_var_cli:GetVariableInfoCLI,add_membership_cli:AddMembershipCLI):
        self.get_exist_var_name_cli = get_exist_var_name_cli
        self.get_var_cli = get_var_cli
        self.add_membership_cli = add_membership_cli
        self.desc = "Add/update membership to existing variables"
    def execute(self):
        res_existing_var_name = self.get_exist_var_name_cli.execute()
        if not res_existing_var_name:
            print(f'Not able to add/update membership.')
            return False
        self.get_var_cli.setElementToValidate(res_existing_var_name)
        res_get_var = self.get_var_cli.execute()
        if not res_get_var:
            print(f'Not able to add/update membership.')
            return False
        self.add_membership_cli.execute(res_get_var.name, res_get_var.mf)
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