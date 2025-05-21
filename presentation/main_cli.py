from infra.dependency.dependencies import set_cli_dependencies
from presentation.modules.build_variable_cli import build_variable_cli

build_variable_cli_adapter, variable_repo = set_cli_dependencies()

build_variable_cli(build_variable_cli_adapter)

print(variable_repo.getAll())