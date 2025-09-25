class car:
    def __init__(self, brand, color, speed, doors):
        self.brand = brand
        self.color = color
        self._speed = speed
        self.doors = doors
    def drive(self):
        print(f"the {self.color} {self.brand} car going with a speed of {self._speed}.")
    def stop(self):
        print(f"the {self.color} {self.brand} car stops.")
    def accelerate(self, amount):
        self._speed += amount
        
class electricar(car):
    def drive(self):
        print(f"the {self.color} {self.brand} car going with a speed of {self._speed}.")
    def stop(self):
        print(f"the {self.color} {self.brand} car stops.")
    def accelerate(self, amount):
        self._speed += amount

class sportcar(car):
    def drive(self):
        print(f"the {self.color} {self.brand} car going with a speed of {self._speed}.")
    def stop(self):
        print(f"the {self.color} {self.brand} car stops.")
    def accelerate(self, amount):
        self._speed += amount

my_car = car("dacia", "blue", 80, 4)
panamera = sportcar("porche", "mateblack", 260, 2)
cybertruck = electricar("tesla", "gray", 150, 4)

cars = [my_car, panamera, cybertruck]
for car in cars:
    car.drive()
    car.accelerate(10)
    car.drive()
    car.stop() 