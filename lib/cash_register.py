#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = []

  lastTitle=""
  lastPrice=0
  lastQuantity=1

  def add_item(self, title, price, quantity=1):
    self.lastTile=title
    self.lastPrice=price
    self.lastQuantity=quantity
    for i in range(0,quantity):
        self.items.append(title)
    self.total+=price*quantity

  def apply_discount(self):
    if self.discount != 0:
      self.total=self.total*(1-self.discount/100)
      print("After the discount, the total comes to $"+str(int(self.total))+".")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total-=self.lastPrice*self.lastQuantity
