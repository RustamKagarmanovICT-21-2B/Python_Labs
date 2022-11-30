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
            json.dump(toJson, text, indent=4)
        json_string = json.dumps(text)


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
            json.dump(toJson, text, indent=4)


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
            json.dump(toJson, text, indent=4)


def Menu(Choose_Action):
    if Choose_Action == 1:
        car_name = input("Введите название машины: ")
        car_price = input("Введите стоимость машины: ")
        car_HP = input('Введите мощность машины в лошадинных силах: ')
        with open("car.json", "rt", encoding="utf-8") as file:
            text = json.load(file)

        text["name"] = car_name
        text["price"] = car_price
        text["HP"] = car_HP

        with open("car.json", "wt", encoding="utf-8") as file:
            json.dump(text, file, indent=4)
    elif Choose_Action == 2:
        airplane_name = input("Введите название самолета: ")
        airplane_price = input("Введите стоимость самолета: ")
        airplane_passengers = input('Введите количество пассажиров на борту самолета: ')
        airplane_altitude = input('Введите максимальную высоту полета самолета: ')
        with open("airplane.json", "rt", encoding="utf-8") as file:
            text = json.load(file)

        text["name"] = airplane_name
        text["price"] = airplane_price
        text["passengers on a board"] = airplane_passengers
        text["flight altitude"] = airplane_altitude

        with open("airplane.json", "wt", encoding="utf-8") as file:
            json.dump(text, file, indent=4)
    elif Choose_Action == 3:
        car = Car()
        car.json_read("Car_Read.json")
        car.json_save("car.json")

        airplane = Airplane()
        airplane.json_read("Airplane_Read.json")
        airplane.json_save("airplane.json")
    elif Choose_Action == 4:
        with open("car.json", "rt", encoding="utf-8") as file:
            car_read = json.load(file)
        print("Название:", car_read["name"], "Цена: ", car_read["price"], "$", "Мощность: ", car_read["HP"], "Л.С.")
        with open("airplane.json", "rt", encoding="utf-8") as file:
            airplane_read = json.load(file)
        print("Название:", airplane_read["name"], "Цена:", airplane_read["price"], "$",
              "Пассажиров на борту:", airplane_read["passengers on a board"],
              "Максимальная высота", airplane_read["flight altitude"], "КМ")


num = int(input("Выберете действие: \n"
                "1.Задание машины вручную\n"
                "2.Задание самолета вручную\n"
                "3.Задание объектов из файла\n"
                "4.Вывод объектов из файла\n"
                ">>>"))
Menu(num)
