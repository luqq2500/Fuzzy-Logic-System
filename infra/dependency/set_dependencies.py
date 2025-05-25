from application.interactor.build_variable_interactor import BuildVariableInteractor
from infra.engine.skfuzzy.skfuzzy_engine import SkFuzzyEngine
from infra.interface_adapter.cli.cli_adapter import BuildVariableCLIAdapter
from infra.repository.inmemory.in_memory_variable_repo import InMemoryVariableRepository

def set_cli_dependencies():
    engine = SkFuzzyEngine()
    var_repo = InMemoryVariableRepository()
    int_build_var = BuildVariableInteractor(engine, var_repo)
    build_variable_cli_adapter = BuildVariableCLIAdapter(int_build_var)

    return build_variable_cli_adapter, var_repo