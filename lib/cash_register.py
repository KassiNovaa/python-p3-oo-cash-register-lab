
#Build a class with instance methods.
#Call instance methods inside of other instance methods.
#Use instance methods to track information pertinent to an instance of a class.
#Add items of varying quantities and prices
#Calculate discounts
#Keep track of what's been added to it
#Void the last transaction

class CashRegister:

  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []



  def add_item(self, item , price, quantity = 1):
    cart = price * quantity
    newtotal = cart + self.total
    self.total = newtotal
    for _ in range(quantity):
      self.items.append(item)
    

  def apply_discount(self):
    if self.discount > 0 :
      discountitem = (self.discount / 100) * self.total
      new_total = self.total - discountitem
      self.total = new_total
      print (f"After the discount, the total comes to ${int(self.total)}.")
    else: 
      print('There is no discount to apply.')



  def void_last_transaction(self):
    new_total = self.total - self.items.pop()
    self.total =  new_total 
