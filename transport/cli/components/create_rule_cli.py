# information required: rule name, sequence of variable[ordinal] and logic, consequent variable.

class CreateRuleCLI:
    def __init__(self, adapter):
        self.adapter = adapter

    def execute(self):
        name = self.get_rule_name()
        var_logic_seq = self.get_variable_logic_seq()
        con_var = self.get_consequent_variable()
        res = self.adapter.execute(name, var_logic_seq, con_var)
        print(f'Rule created: {res.name},{res.ant},{res.con}')
        return res

    @staticmethod
    def get_rule_name():
        name = input("Enter rule name: ")
        return name

