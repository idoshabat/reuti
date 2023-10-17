class Item:

    item_list=list()

    def __init__(self,name,price):
        if not isinstance(name,str):
            raise ValueError("Name has to be a string")
        if not isinstance(price,float) or isinstance(price, int):
            raise ValueError("Price has to be a number")

        self.name=name
        self.price=price
        Item.item_list.append(self)

    def __str__(self):
        return (f"Item's name: {self.name}\n"
                f"Price: {self.price}$\n")

