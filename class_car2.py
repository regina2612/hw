class Car:
    def __init__(self, owner, make, model, year):
        self.owner = owner
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.is_going = False

    def go(self, distance):
        self.is_going = True
        self.odometer = self.odometer + distance
        print('Syezdili v Typ')

    def stop(self, brake):
        self.is_going = False
        self.odometer += brake
        print('Pit stop')

bekzats_car = Car('Bekzat', 'Dodge', 'Charger', 2015)
print(f'{bekzats_car.make} {bekzats_car.model}')

print(bekzats_car.odometer, bekzats_car.is_going)
bekzats_car.go(500)
print(bekzats_car.odometer, bekzats_car.is_going)

print(bekzats_car.odometer, bekzats_car.is_going)
bekzats_car.stop(0)
print(bekzats_car.odometer, bekzats_car.is_going)
