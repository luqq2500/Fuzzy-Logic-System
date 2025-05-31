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

class FormatExistingAntecedentForDisplayResponse:
    def __init__(self, formatted_antecedent):
        self.formatted_antecedent = formatted_antecedent



