class GetExistingVariableNameCLI:
    def __init__(self,adapter):
        self.adapter = adapter
    def execute(self):
        res = self.adapter.execute()
        if not res.existing_variable_name:
            print(f'No existing variables found.')
            return False
        print(f'Existing variables: {res.existing_variable_name}')
        return res.existing_variable_name
