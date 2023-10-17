from Item import *
import datetime
from BudgetError import *

class Transaction:

    date= datetime.date.today()
    transactions= list()

    def __init__(self,customer , item):
        if not isinstance(item,Item):
            raise ValueError("This is not a customer!!")
        if customer.badget < item.price:
            raise BudgetError()

        self.customer=customer
        self.item=item

        Transaction.transactions.append(self)

    def __str__(self):
        return f'{self.item.name} for {self.item.price}$'