from application.interactor.add_membership import AddMembership
from application.interactor.create_variable import CreateVariable
from application.interactor.process_variable_ordinal_for_display import ProcessVariableOrdinalForDisplay
from infra.engine.skfuzzy.skfuzzy_engine import SkFuzzyEngine
from transport.cli.adapter.cli_adapter import CreateVariableCLIAdapter, AddMembershipCLIAdapter, DisplayVariableOrdinalCLIAdapter
from infra.repository.inmemory.in_memory_variable_repo import InMemoryVariableRepository
from transport.cli.components.add_membership_cli import AddMembershipCLI
from transport.cli.components.create_variable_cli import CreateVariableCLI
from transport.cli.components.display_variable_ordinal_cli import DisplayVariableOrdinalCLI
from transport.cli.strategy.cli_strategy import CLIStrategy


def set_cli_dependencies():
    engine = SkFuzzyEngine()
    var_repo = InMemoryVariableRepository()

    create_var_interactor = CreateVariable(engine, var_repo)
    create_var_adapter = CreateVariableCLIAdapter(create_var_interactor)
    create_var_cli = CreateVariableCLI(create_var_adapter)

    add_mem_interactor = AddMembership(engine, var_repo)
    add_mem_adapter = AddMembershipCLIAdapter(add_mem_interactor)
    add_mem_cli = AddMembershipCLI(add_mem_adapter)

    display_var_ordinal_interactor = ProcessVariableOrdinalForDisplay(var_repo)
    display_var_ordinal_adapter = DisplayVariableOrdinalCLIAdapter(display_var_ordinal_interactor)
    display_variable_ordinal_cli = DisplayVariableOrdinalCLI(display_var_ordinal_adapter)

    cli_strategy = CLIStrategy(create_var_cli, add_mem_cli, display_variable_ordinal_cli)

    return cli_strategy
