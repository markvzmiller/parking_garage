"""Defines the Garage class.

Author: Bella Miller
Version: 4/25/23

This work complies with the JMU Honor Code.
"""
from space import Space


class Garage:
    """Represents a parking garage and assigns cars to spaces.

    Attributes:
        _spaces (list): Parking spaces, sorted by distance from the entrance.
        _cars (dict): Maps license plate strings to assigned parking spaces.
    """

    def __init__(self, data):
        self._spaces = []
        for line in data:
            line_list = line.split(',')
            label = line_list[0]
            dimensions = (int(line_list[1]), int(line_list[2]), int(line_list[3]))
            space = Space(label, dimensions)
            self._spaces.append(space)
        self._cars = {}
        self._capacity = 0

    def get_capacity(self):
        return len(self._spaces)

    def get_occupied(self):
        return len(self._cars)

    def assign_space(self, car):
        for space in self._spaces:
            if space.can_park(car) and space.is_occupied() is False:
                space.set_car(car)
                self._cars[car.get_plate()] = space
                return space
        return None

    def remove_car(self, plate):
        space = self._cars[plate]
        car = space.get_car()
        del self._cars[plate]
        space.set_car(None)
        return car

    def impound_cars(self, now):
        impound_cars = []
        for plate in self._cars.copy().keys():
            space = self._cars[plate]
            car = space.get_car()
            if car is not None:
                time = now - car.get_arrival()
                if time.days >= 7:
                    impound_cars.append(self.remove_car(plate))
        return impound_cars

    def __str__(self):
        return f'Garage: {self.get_capacity() - self.get_occupied()} spaces available'
