from infra.dependency.set_dependencies import set_cli_dependencies
from transport.cli.strategy.cli_strategy import CLIStrategy

strategy = set_cli_dependencies()

print('Welcome to Fuzzy Logic System!')
print('User mode: \n1. Create variable alone \n2. Create variable and add membership')
mode = input(f'Select mode: ')
if int(mode) == 1:
    strategy.createVariableAlone()
elif int(mode) == 2:
    strategy.createVariableAndAddMembership()