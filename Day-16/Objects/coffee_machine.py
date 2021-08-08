class Coffee_Machine:
  water = 500 
  milk = 200
  coffee = 100

  def make_coffee(self, ):
    self.water -= 100
    self.milk -= 50
    self.coffee -= 18

  def take_order(self):
    task = input("What coffee would you like? (1/2/3)\n1. Esspress\n2.Latte\n3.Americano")
    if task == "1":
