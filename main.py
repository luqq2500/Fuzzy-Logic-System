from infra.dependency.set_dependencies import setDependenciesReturnStrategies
from transport.cli.main_cli import CLI

cli_strategy = setDependenciesReturnStrategies()
cli = CLI(cli_strategy)
cli.execute()