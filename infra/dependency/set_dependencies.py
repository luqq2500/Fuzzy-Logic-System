from application.interactor.add_membership import AddMembership
from application.interactor.create_variable import CreateVariable
from application.interactor.format_existing_antecedent import FormatExistingAntecedent
from application.interactor.get_existing_variable_name import GetExistingVariableName
from application.interactor.get_variable_info_by_name import GetVariableInfoByName
from infra.engine.skfuzzy.skfuzzy_engine import SkFuzzyEngine
from infra.repository.inmemory.in_memory_variable_repo import InMemoryVariableRepository
from transport.cli.adapter.cli_adapter import CreateVariableCLIAdapter, AddMembershipCLIAdapter, FormatExistingAntecedentCLIAdapter, GetVariableInfoByNameCLIAdapter, GetExistingVariableNameCLIAdapter
from transport.cli.components.add_membership_cli import AddMembershipCLI
from transport.cli.components.create_variable_cli import CreateVariableCLI
from transport.cli.components.display_variable_ordinal_cli import DisplayExistingAntecedentCLI
from transport.cli.components.get_existing_variable_name_cli import GetExistingVariableNameCLI
from transport.cli.components.get_variable_cli import GetVariableInfoCLI
from transport.cli.strategy.user_strategy import IUserStrategyCLI,UserCreateVariableCLI, UserPutVariableNameAddMembershipCLI, UserCreateVariableAddMembershipCLI
from transport.cli.strategy.get_variable_info_strategy import GetVariableInfoByNameStrategy


def setDependenciesReturnStrategies():
    engine = SkFuzzyEngine()
    var_repo = InMemoryVariableRepository()

    create_var_interactor = CreateVariable(engine, var_repo)
    create_var_adapter = CreateVariableCLIAdapter(create_var_interactor)
    create_var_cli = CreateVariableCLI(create_var_adapter)

    add_mem_interactor = AddMembership(engine, var_repo)
    add_mem_adapter = AddMembershipCLIAdapter(add_mem_interactor)
    add_mem_cli = AddMembershipCLI(add_mem_adapter)

    # format_existing_antecedent_interactor = FormatExistingAntecedent(var_repo)
    # display_existing_antecedent_adapter = FormatExistingAntecedentCLIAdapter(format_existing_antecedent_interactor)
    # display_existing_antecedent_cli = DisplayExistingAntecedentCLI(display_existing_antecedent_adapter)

    get_existing_var_name_interactor = GetExistingVariableName(var_repo)
    get_existing_var_name_adapter = GetExistingVariableNameCLIAdapter(get_existing_var_name_interactor)
    get_existing_var_name_cli = GetExistingVariableNameCLI(get_existing_var_name_adapter)

    get_variable_by_name_interactor = GetVariableInfoByName(var_repo)
    get_variable_by_name_adapter = GetVariableInfoByNameCLIAdapter(get_variable_by_name_interactor)
    get_variable_by_name_strategy = GetVariableInfoByNameStrategy(get_variable_by_name_adapter)
    get_variable_info_cli = GetVariableInfoCLI(get_variable_by_name_strategy)

    create_variable = UserCreateVariableCLI(create_var_cli)
    get_var_name_add_membership = UserPutVariableNameAddMembershipCLI(get_existing_var_name_cli,get_variable_info_cli,add_mem_cli)
    create_variable_add_membership = UserCreateVariableAddMembershipCLI(create_var_cli, add_mem_cli)

    strategies:dict[str,IUserStrategyCLI] = {
        '1': create_variable,
        '2': get_var_name_add_membership,
        '3': create_variable_add_membership
    }

    return strategies

