"""Defines the Space class.

Author: Bella Miller
Version: 04/25/23

This work complies with the JMU Honor Code.
"""


class Space:
    """An individual parking space in the garage.

    Attributes:
        _label (str): The label for the space (Ex: "A 0").
        _dimensions (tuple): The space's length, width, and height.
        _car (Car): The car currently parked in this space.
    """

    def __init__(self, label, dimensions, car=None):
        self._label = label
        self._dimensions = dimensions
        self._car = car

    def get_label(self):
        return self._label

    def get_dimensions(self):
        return self._dimensions

    def get_car(self):
        return self._car

    def set_car(self, car):
        self._car = car

    def is_occupied(self):
        if self._car is None:
            return False
        else:
            return True

    def can_park(self, car):
        car_dimensions = car.get_dimensions()  # corrected method call
        if self._dimensions[0] < car_dimensions[0]:  
            return False
        if self._dimensions[1] < car_dimensions[1] + 4:  # width
            return False
        if self._dimensions[2] < car_dimensions[2] + 1:  # height
            return False
        else:
            return True

    def __str__(self):
        if self._car:
            return (f'Space: {self._label}, {self._dimensions[0]}x'
                    f'{self._dimensions[1]}x{self._dimensions[2]}, {self._car.get_plate()}')
        else:
            return (f'Space: {self._label}, {self._dimensions[0]}x'
                    f'{self._dimensions[1]}x{self._dimensions[2]}, not occupied')
