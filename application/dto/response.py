class CreateVariableResponse:
    def __init__(self, var):
        self.name = var.name
        self.type = var.type
        self.universe = var.universe
        self.fuzzy_var = var.fuzzy_variable

class AddMembershipResponse:
    def __init__(self, var):
        self.name = var.name
        self.memberships = var.memberships

class CreateRuleResponse:
    def __init__(self, rule):
        self.name = rule.name
        self.ant = rule.ant
        self.con = rule.con

class GetAllExistingVariableResponse:
    def __init__(self, variables):
        self.variables = variables

class ProcessVariableOrdinalsForDisplayResponse:
    def __init__(self, variable_ordinal_for_display):
        self.variableOrdinalForDisplay = variable_ordinal_for_display



