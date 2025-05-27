from infra.engine.fuzzy_engine_interface import IFuzzyEngine
from infra.repository.variable_repo_interface import IRepository
from models.rule import Rule
import operator
from models.variable import Variable


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
        self.validate(req)
        assert len(req.var_logic_seq) % 2 == 1
        rule_base = Rule(req.name)
        antecedent = req.var_logic_seq[-1]
        for i in range(len(req.var_logic_seq)-2,0,-2):
            logic = req.var_logic_seq[i]
            var_set = req.var_logic_seq[i-1]
            antecedent = logic(var_set, antecedent)
        fuzzy_rule = self.engine.createRule(antecedent, req.con_var)
        rule_base.fuzzy_rule = fuzzy_rule
        rule_term_label = self.engine.getRuleTermAndLabel(rule_base.fuzzy_rule)
        rule_base.var_term_label = rule_term_label

    def validate(self, req):
        if not isinstance(self.engine, IFuzzyEngine):
            raise ValueError("Engine must be an instance of IFuzzyEngine.")
        if not isinstance(self.repo, IRepository):
            raise ValueError("Repository must be an instance of IRepository.")
        if req.name is None:
            raise ValueError("Rule name cannot be None.")
        if not isinstance(req.name, str): # Added check for string type
            raise ValueError("Rule name must be a string.")
        if not req.name.strip(): # Simplified from checking strip() != ""
            raise ValueError("Rule name cannot be empty or whitespace.")
        if not isinstance(req.var_logic_seq, list):
            raise ValueError("Variable logic sequence must be a list.")
        if not req.var_logic_seq: # Added check for empty list
            raise ValueError("Variable logic sequence cannot be empty.")
        if len(req.var_logic_seq) % 2 == 0: # Changed to check for even length, as odd is expected
            raise ValueError("Variable logic sequence must have an odd number of elements (variable, logic, variable...).")
        for i in range(0, len(req.var_logic_seq) - 1, 2):
            var_set = req.var_logic_seq[i]
            # The last element is a variable, not followed by a logic operator
            if i + 1 < len(req.var_logic_seq):
                logic = req.var_logic_seq[i+1]
                if not (logic is operator.and_ or logic is operator.or_): # Use 'is' for singletons
                    raise ValueError(f"Logic operator at index {i+1} must be 'operator.and_' or 'operator.or_'. Found: {logic}")
            if not isinstance(var_set, Variable):
                raise ValueError(f"Element at index {i} in variable logic sequence must be a Variable instance. Found: {type(var_set)}")
        last_element = req.var_logic_seq[-1]
        if not isinstance(last_element, Variable):
            raise ValueError(f"The last element in variable logic sequence must be a Variable instance. Found: {type(last_element)}")
        if not isinstance(req.con_var, float):
            raise ValueError(f"Consequent variable (con_var) must be a float instance. Found: {type(req.con_var)}")