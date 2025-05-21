from application.builder.concrete.concrete_variable_builder import VariableBuilder
from application.builder.director.director_variable_builder import VariableBuilderDirector
from application.interactor.build_variable_interactor import BuildVariableInteractor
from infra.engine_adapter.skfuzzy.skfuzzy_engine import SkFuzzyEngine
from infra.interface_adapter.cli.cli_adapter import BuildVariableCLIAdapter
from infra.repository.inmemory.in_memory_variable_repo import InMemoryVariableRepository

def set_cli_dependencies():
    engine = SkFuzzyEngine()
    variable_builder = VariableBuilder(engine)
    variable_builder_director = VariableBuilderDirector(variable_builder)
    variable_repository = InMemoryVariableRepository()

    build_variable_interactor = BuildVariableInteractor(variable_builder_director, variable_repository)
    build_variable_cli_adapter = BuildVariableCLIAdapter(build_variable_interactor)

    return build_variable_cli_adapter, variable_repository