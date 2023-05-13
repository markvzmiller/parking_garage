"""Defines the DukesParking class.

Author: Bella Miller
Version: 04/25/23

This work complies with the JMU Honor Code.
"""
from datetime import datetime
from car import Car
from garage import Garage
import math


class DukesParking:
    """Simulation of cars arriving/departing and making payments.

    Attributes:
        _garage_data (list): Lines of the garage file.
        _events_data (list): Lines of the events file.
    """

    def __init__(self, garage_file, events_file):
        with open(garage_file) as f:
            self._garage_data = f.readlines()  # self._garage_data is a list
        with open(events_file) as f:
            self._events_data = f.readlines()  # self._events_data is a list

    def run(self):
        garage = Garage(self._garage_data)
        for item in self._events_data:  # item is string
            info = item.split(',')  # makes string a list
            event_time = datetime.fromisoformat(info[0])
            plate = info[2]
            dimension_str = info[3]
            dimension_list = dimension_str.split('x')
            length = int(dimension_list[0])
            width = int(dimension_list[1])
            height = int(dimension_list[2])
            dimensions = (length, width, height)
            if info[1] == 'Arrive':
                car = Car(plate, dimensions, event_time)
                print(f'ARRIVAL {car}')
                space = garage.assign_space(car)
                if space is not None:
                    print(f'PARK_IN {space}')
                else:
                    print('NO SPACES AVAILABLE')
            elif info[1] == 'Depart':
                car = garage.remove_car(plate)
                print(f'EXITING {car}')
                fee = self.payment(car.get_arrival(), event_time)
                print(f'PAYMENT ${fee:.2f}')
            impounded_cars = garage.impound_cars(event_time)
            for car in impounded_cars:
                print(f'IMPOUND {car}')

    @staticmethod
    def payment(arrive, depart, hourly_rate=1, daily_limit=20):
        seconds = (depart - arrive).total_seconds()
        hours = math.ceil(seconds / 3600)
        days = math.floor(hours / 24)
        hours %= 24
        fee = days * daily_limit + hours * hourly_rate
        return min(fee, 24 * hourly_rate * 7)
