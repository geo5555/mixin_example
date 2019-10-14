class Vehicle(object):
    """A generic vehicle class."""

    def __init__(self, name="unknown"):
        self.name = name

    def travel(self, townstart, destination):
        print(f"travelling from {townstart} to {destination} ")


class Boat(Vehicle):
    def __init__(self, name):
        print("__init__ boat called")


class Car(Vehicle):
    def __init__(self, name):
        print("__init__ Car called")


class RadioUserMixin(object):
    def __init__(self):
        print("init mixin called")

    def play_song_on_station(self, song):
        print(f"playing song {song}")


class PrintJsonMixin(object):
    def __init__(self):
        print("init mixin called")

    def return_json(self, name):
        print(f'{"name"} : {name}')


class Bike(Vehicle, RadioUserMixin, PrintJsonMixin):
    def __init__(self, name):
        self.name = name
        print("__init__ bike called")


car1 = Car("mycar")
car1.travel("NY", "Las Vegas")
boat1 = Boat("myboat")
boat1.travel("NY", "Las Vegas")
bike1 = Bike("mybike")
bike1.travel("paris", "london")
bike1.play_song_on_station("hello how are you")
#mix1 = RadioUserMixin()
bike1.return_json(bike1.name)
