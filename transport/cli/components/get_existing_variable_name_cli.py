class GetExistingVariableNameCLI:
    def __init__(self,adapter):
        self.adapter = adapter
    def execute(self):
        res = self.adapter.execute()
        if res.existing_variable_name:
            print(f'Existing variables: {res.existing_variable_name}')
            return res.existing_variable_name
        else:
            print(f'No existing variables found.')
            return False