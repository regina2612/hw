class Airplane:
    def __init__(self, make, model, year, max_speed, odometer, is_flying):		
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False

    def takeoff(self, take):
        self.is_flying = True 
        self.odometer += take
        print('Take')

    def fly(self, flight):
        self.is_flying = True
        self.odometer += flight
        print('Fly')

    def lang(self, lang):
        self.is_flying = False
        self.odometer += lang
        print('Lang')

ty_airplane = Airplane('Tu', '154m', 2006, 935, 0, 0)
print(f'{ty_airplane.make}, {ty_airplane.model}, {ty_airplane.year}, {ty_airplane.max_speed}')

print(ty_airplane.odometer, ty_airplane.is_flying)
ty_airplane.takeoff(100)
print(ty_airplane.odometer, ty_airplane.is_flying)

print(ty_airplane.odometer, ty_airplane.is_flying)
ty_airplane.lang(0)
print(ty_airplane.odometer, ty_airplane.is_flying)
