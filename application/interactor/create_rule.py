from models.rule import Rule
import operator

# This is 'create rule' interactor.
# Information required: name, variable and logic sequence, con_var => fuzzy rule.
# Additional info: ant_var_set{name:ordinal}, for further validation.
# 1. get user input sequence of var[ordinal], and logic.
# 2. convert logic sequence str into operator.logic_.
# 3. create antecedent.
# 4. create fuzzy rule (ant, con)
# 5. save variable name and term in rule dictionary.


class CreateRule:
    def __init__(self, engine, repo):
        self.engine = engine
        self.repo = repo

    def execute(self, req):
        assert len(req.var_logic_seq) % 2 == 1
        rule_base = Rule(req.name)
        antecedent = self.sortVarLogicSequenceReturnAntecedent(req.var_logic_seq)
        fuzzy_rule = self.engine.createRule(antecedent, req.con_var)
        rule_base.fuzzy_rule = fuzzy_rule
        rule_term_label = self.engine.getRuleTermAndLabel(rule_base.fuzzy_rule)
        rule_base.var_term_label = rule_term_label

    @staticmethod
    def sortVarLogicSequenceReturnAntecedent(var_logic_seq):
        antecedent = var_logic_seq[-1]
        for i in range(len(var_logic_seq)-2,0,-2):
            logic = var_logic_seq[i]
            var_set = var_logic_seq[i-1]
            antecedent = logic(var_set, antecedent)
        return antecedent

