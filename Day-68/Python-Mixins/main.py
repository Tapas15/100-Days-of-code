class BaseClass:
    def __init__(self, *args, **kwargs):
        self.name="Flying Object"

class AddWingsMixin(object):
    def __init__(self, *args, **kwargs):
        self.wings=True

    def fly(self):
        print("Flying with wings.")

class AddJetEngineMixin(object):
    def __init__(self, *args, **kwargs):
        self.requires_electricity=True

    def fly(self):
        print("Flying with jet engine.")

class MyBirdClass(AddJetEngineMixin, AddWingsMixin, BaseClass):
    pass

class MyPlaneClass(AddJetEngineMixin, BaseClass):
    pass

bird = MyBirdClass("Robin")
bird.fly()
print(bird.name)
print(bird.requires_electricity)

plane=MyPlaneClass("The Red Baron")
plane.fly()