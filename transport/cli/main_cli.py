from transport.cli.strategy.user_strategy import IUserStrategyCLI

class CLI:
    def __init__(self, strategies:dict[str,IUserStrategyCLI]):
        self.strategies = strategies
        self.currentStrategy = None

    def execute(self):
        while True:
            self.displayStrategies()
            if not self.selectStrategy():
                print('See you again. Exiting system.')
                exit()
            result = self.currentStrategy.execute()
            if result:
                print(f"Strategy '{self.currentStrategy.getDescription()}': Ended with success.")
            else:
                print(f"Strategy '{self.currentStrategy.getDescription()}': Ended with failure.")

    def displayStrategies(self):
        for index, strategy in self.strategies.items():
            print(f'{index}: {strategy.getDescription()}')

    def selectStrategy(self):
        while True:
            mode = input('Choose mode index (q to quit): ').lower()
            if mode == 'q':
                return False
            if mode not in [key for key in self.strategies.keys()]:
                print('Invalid mode. Please try again.')
            else:
                self.currentStrategy = self.strategies[mode]
                return True

