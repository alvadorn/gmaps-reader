from .coordinates import Point
from util import gps_calc

class GPS:
    def __init__(self, coordinates, type='decimal'):
        self.initial_coordinates = Point(coordinates)
        self.present_coordinates = Point(coordinates)

    def __str__(self):
        return "%s,%s" % self.present_coordinates()

    def __call__(self):
        return self.present_coordinates()

    def add_horizontally(self, distance):
        self.present_coordinates = Point(gps_calc.add_horizontally(self.present_coordinates(), distance))
        _, lon = self.present_coordinates()
        return lon

    def add_vertically(self, distance):
        latitude = self.initial_coordinates()[0]
        next_latitude = gps_calc.add_vertically(latitude, distance)
        self.initial_coordinates.set_latitude(next_latitude)
        self.present_coordinates = self.initial_coordinates
