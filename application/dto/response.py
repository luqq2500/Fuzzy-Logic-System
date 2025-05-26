class CreateVariableResponse:
    def __init__(self, var):
        self.name = var.name
        self.type = var.type
        self.universe = var.universe
        self.fuzzy_var = var.fuzzy_variable
        self.base = var

class AddMembershipResponse:
    def __init__(self, var):
        self.name = var.name
        self.memberships = var.memberships



