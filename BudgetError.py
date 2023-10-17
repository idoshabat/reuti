class BudgetError(Exception):

    def __init__(self, message="You don't have enough money !!!"):
        self.message = message
        super().__init__(self.message)