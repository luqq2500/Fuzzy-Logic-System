from application.interactor.add_membership import AddMembership
from application.interactor.build_variable import BuildVariableInteractor
from application.interactor.create_variable import CreateVariable
from infra.engine.skfuzzy.skfuzzy_engine import SkFuzzyEngine
from infra.transport.cli.cli_adapter import BuildVariableCLIAdapter, CreateVariableCLIAdapter, AddMembershipCLIAdapter
from infra.repository.inmemory.in_memory_variable_repo import InMemoryVariableRepository
from presentation.modules.add_membership_cli import AddMembershipCLI
from presentation.modules.create_variable_cli import CreateVariableCLI


def set_cli_dependencies():
    engine = SkFuzzyEngine()
    var_repo = InMemoryVariableRepository()

    build_var_interactor = BuildVariableInteractor(engine, var_repo)
    create_var_interactor = CreateVariable(engine, var_repo)
    add_mem_interactor = AddMembership(engine, var_repo)

    build_var_adapter = BuildVariableCLIAdapter(build_var_interactor)
    create_var_adapter = CreateVariableCLIAdapter(create_var_interactor)
    add_mem_adapter = AddMembershipCLIAdapter(add_mem_interactor)

    create_var_cli = CreateVariableCLI(create_var_adapter)
    add_mem_cli = AddMembershipCLI(add_mem_adapter)

    return create_var_cli, add_mem_cli
