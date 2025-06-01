from dataclasses import dataclass

@dataclass
class Rule:
    def __init__(self, name:str):
        self.name:str = name
        self.var_term_label: dict[str:str] = {}
        self.fuzzy_rule:object = None
    def setFuzzyRule(self, fuzzy_rule:object) -> None:
        self.fuzzy_rule = fuzzy_rule