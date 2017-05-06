from .coordinates import Point
from gmaps_reader.util import gps_calc 

EARTH_RADIUS = 6378.1 # kilometers
bearing = 1.57


class GPS:
    def __init__(self, coordinates, type='decimal'):
        self.initial_coordinates = Point(coordinates)
        self.present_coordinates = Point(coordinates)

    def add_horizontally(self, distance):
        self.present_coordinates = Point(gps_calc.add_horizontally(self.coordinates()))

    def add_vertically(self, distance):
        latitude = self.initial_coordinates()[0]
        next_latitude = gps_calc.add_vertically(latitude, distance)
        self.initial_coordinates.set_latitude(next_latitude)
        self.present_coordinates = self.initial_coordinates
