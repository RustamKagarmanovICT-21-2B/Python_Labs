import json


class Vehicle:
    def __init__(self):
        self.__name = "null"
        self.__price = 1

    def print(self):
        print("Name: ", self.__name)
        print("Price: ", self.__price, "$")

    def json_read(self, jsonFilepath: str):
        with open(jsonFilepath) as text:
            allObjects = json.load(text)
            self.__name = allObjects["name"]
            self.__price = allObjects["price"]

    def json_save(self, json_filepath: str):
        toJson = {
            "name": self.__name,
            "price": self.__price
        }
        with open(json_filepath, 'w') as text:
            json.dump(toJson, text)


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.__HP = 1

    def print(self):
        super().print()
        print("Horse power: ", self.__HP)

    def json_read(self, jsonFilepath: str):
        with open(jsonFilepath) as text:
            allObjects = json.load(text)
            self.__name = allObjects["name"]
            self.__price = allObjects["price"]
            self.__HP = allObjects["HP"]

    def json_save(self, json_filepath: str):
        toJson = {
            "name": self.__name,
            "price": self.__price,
            "HP": self.__HP
        }
        with open(json_filepath, 'w') as text:
            json.dump(toJson, text)


class Airplane(Vehicle):
    def __init__(self):
        super().__init__()
        self.__countPassengers = 0
        self.__flightAltitude = 1

    def print(self):
        super().print()
        print("Passengers on a board: ", self.__countPassengers)
        print("Flight altitude: ", self.__flightAltitude, " kilometers")

    def json_read(self, jsonFilepath: str):
        with open(jsonFilepath) as text:
            allObjects = json.load(text)
            self.__name = allObjects["name"]
            self.__price = allObjects["price"]
            self.__countPassengers = allObjects["passengers on a board"]
            self.__flightAltitude = allObjects["flight altitude"]

    def json_save(self, json_filepath: str):
        toJson = {
            "name": self.__name,
            "price": self.__price,
            "passengers on a board": self.__countPassengers,
            "flight altitude": self.__flightAltitude
        }
        with open(json_filepath, 'w') as text:
            json.dump(toJson, text)


car_name = input("Введите название машины: ")
Vehicle.__name__ = car_name


car = Car()
car.json_read("Car_Read.json")
car.json_save("car.json")

airplane = Airplane()
airplane.json_read("Airplane_Read.json")
airplane.json_save("airplane.json")
