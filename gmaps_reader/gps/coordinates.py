

class Latitude:
    def __init__(self, latitude):
        self.latitude = latitude
    def __call__(self):
        return self.latitude

class Longitude:
    def __init__(self, longitude):
        self.longitude = longitude
    def __call__(self):
        return self.longitude

class Point:
    def __init__(self, coordinates):
        self.latitude = Latitude(coordinates[0])
        self.longitude = Longitude(coordinates[1])

    def __call__(self):
        return (self.latitude(), self.longitude())

    def set_latitude(self, latitude):
        self.latitude = Latitude(latitude)

    def set_longitude(self, longitude):
        self.longitude = Longitude(longitude)
