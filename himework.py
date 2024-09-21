class Vehicle:
    def move(self):
        print("Транспортное средство движется")

    def fuel(self):
        return "Топливо"

class Car(Vehicle):
    def move(self):
        print("Машина едет по дороге")

    def fuel(self):
        return "Бензин"

class Bicycle(Vehicle):
    def move(self):
        print("Велосипед едет по велосипедной дорожке")

    def fuel(self):
        return "Не требует толпива"

class Boat(Vehicle):
    def move(self):
        print("Лодка плывет по воде")

    def fuel(self):
        return "Электричество"

vehicles = [Car(), Bicycle(), Boat()]

for vehicle in vehicles:
    vehicle.move()
    print(f"Топливо: {vehicle.fuel()}")
    