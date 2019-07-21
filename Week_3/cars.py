import os
import csv


N_columns = 7


class BaseCar:

    def __init__(self, brand, photo_file_name, carrying):
        self.car_type = None
        self.photo_file_name = brand
        self.brand = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)


class Car(BaseCar):

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        self.body_length = None
        self.body_width = None
        self.body_height = None
        self._parse_whl(body_whl)

    def _parse_whl(self, body_whl):
        if body_whl == "":
            self.body_length = 0
            self.body_width = 0
            self.body_height = 0
        else:
            body_list = list(map(float, body_whl.split(sep='x')))
            self.body_length = body_list[0]
            self.body_width = body_list[1]
            self.body_height = body_list[2]

    def get_body_volume(self):
        l = self.body_length
        w = self.body_width
        h = self.body_height
        return l * w * h


class SpecMachine(BaseCar):

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if len(row) < N_columns:
                continue
            else:
                car_list.append(parse_row(row))
    return car_list


def parse_row(row):
    car_type = row[0]
    brand = row[1]
    photo_file_name = row[3]
    carrying = row[5]

    if car_type == 'car':
        vehicle = Car(brand, photo_file_name, carrying, row[2])
    elif car_type == 'truck':
        vehicle = Truck(brand, photo_file_name, carrying, row[4])
    elif car_type == 'spec_machine':
        vehicle = SpecMachine(brand, photo_file_name, carrying, row[5])

    return vehicle


if __name__ == '__main__':
    A = get_car_list("_af3947bf3a1ba3333b0c891e7a8536fc_coursera_week3_cars.csv")
