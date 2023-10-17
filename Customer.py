from BudgetError import *
from Item import *
from Transaction import *
from send_email import send_email_successful_buying , is_valid_email


class Customer:
    customers_list = list()

    def __init__(self, name, id, badget, email):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name must be a string")

        if isinstance(id, int):
            self.id = id
        else:
            raise ValueError("Id must be an int")

        if isinstance(badget, float) or isinstance(badget, int):
            self.badget = badget
        else:
            raise ValueError("Name must be a string")

        if isinstance(email, str):
            if not is_valid_email(email):
                raise ValueError("Invalid email !!")
            self.email = email
        else:
            raise ValueError("Name must be a string")

        Customer.customers_list.append(self)
        self.transactions = list()

    def __str__(self):
        return (f"Customer's name: {self.name}\n"
                f"ID: {self.id}\n"
                f"Budget: {self.badget}\n"
                f"Email: {self.email}\n")

    def buy(self, item):
        if not isinstance(item, Item):
            raise ValueError('Not an Item !!!')

        try:
            transaction = Transaction(self, item)
            self.transactions.append(transaction)
            self.badget -= item.price
        except BudgetError:
            missing=item.price-self.badget
            print(f"You don't have enough money. You need more {missing}$")

        # try:
        #     send_email_successful_buying(to_email=self.email, item=item)
        # except ValueError as err:
        #     print('')


    def print_transaction(self):
        print('Customer '+self.name+':')
        for trans in self.transactions:
            print(trans)