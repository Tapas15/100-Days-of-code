class MyClass:
  a = 12

new_object = MyClass()

setattr(new_object, "a", 10)


# class Robot_Vacuum:
#   battery = 100
#   dust_storage = 0

#   def charge(self):
#     self.battery = 100

#   def clean(self):
#     self.dust_storage += 30
#     self.battery -= 20

#   def empty(self):
#     self.dust_storage = 0


# robot_1 = Robot_Vacuum(battery=100, dust_storage=0)
# robot_1.battery = 20
# robot_1.clean()
# robot_1.charge()

# robot_2 = Robot_Vacuum()
# robot_2.clean()
# robot_2.empty()