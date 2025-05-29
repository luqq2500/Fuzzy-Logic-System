from infra.engine.fuzzy_engine_interface import IFuzzyEnginePort
from infra.repository.repo_port import IVariableRepositoryPort
from domain.rule import Rule
import operator
from domain.variable import Variable


# This is 'create rule' business application code.
# Information required: name, variable and logic sequence, con_var => fuzzy rule.
# Additional info: ant_var_set{name:ordinal}, for further validation.
# 1. Get user input sequence of var[ordinal], and logic.
# 2. Convert logic sequence str into operator.logic_.
# 3. Create antecedent.
# 4. Create fuzzy rule (ant, con)
# 5. Save variable name and term in rule dictionary.


class CreateRule:
    def __init__(self, engine, repo):
        self.engine = engine
        self.repo = repo

    def execute(self, req):
        rule_base = Rule(req.name)
        antecedent = req.var_logic_seq[-1]
        for i in range(len(req.var_logic_seq)-2,-1,-2):
            logic = req.var_logic_seq[i]
            var_set = req.var_logic_seq[i-1]
            antecedent = logic(var_set, antecedent)
        fuzzy_rule = self.engine.createRule(antecedent, req.con_var)
        rule_base.fuzzy_rule = fuzzy_rule
        rule_term_label = {term.term.label:term.label for term in rule_base.fuzzy_rule.antecedent.term_set}
        rule_base.var_term_label = rule_term_label