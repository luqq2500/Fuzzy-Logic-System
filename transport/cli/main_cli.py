from infra.dependency.set_dependencies import set_cli_dependencies

create_var_cli, add_mem_cli = set_cli_dependencies()

var_res = create_var_cli.execute()
var_mem_res = add_mem_cli.execute(var_res.name)

print(var_mem_res.name, var_mem_res.memberships)