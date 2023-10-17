from Item import *
from Customer import *

i1=Item('Table',29.99)
c1=Customer('Ido',123,50,"mokpydunk@gmail.com")
print(i1)

c1.buy(i1)
c1.print_transaction()
print(c1.badget)




