from infra.dependency.set_dependencies import set_cli_dependencies
from presentation.modules.build_variable_cli import build_variable_cli

build_variable_cli_adapter, var_repo = set_cli_dependencies()

response = build_variable_cli(build_variable_cli_adapter)

print(response.name,
      response.type,
      response.universe,
      response.fuzzy_variable,
      response.memberships)