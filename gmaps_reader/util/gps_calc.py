import math

EARTH_RADIUS = 6378.1 # kilometers
BEARING = 1.57
R = EARTH_RADIUS
METER_PROPORTION_LATITUDE = -0.000008964

def add_horizontally(coordinates, distance):
    """
        Calcule the new coordinates after adding some distance
        horizontally.
        The coordinates parameter is a tuple with (latitude, longitude).
        The distance parameter is the distance in kilometers.
    """
    initial_latitude, initial_longitude = coordinates
    initial_latitude = math.radians(initial_latitude)
    initial_longitude = math.radians(initial_longitude)

    proportion = distance / EARTH_RADIUS


    next_latitude = math.asin( math.sin(initial_latitude) *
                math.cos(proportion) + math.cos(initial_latitude) *
                math.sin(proportion) * math.cos(BEARING))
    next_longitude = initial_longitude + math.atan2( math.sin(BEARING) *
                math.sin(proportion) - math.sin(initial_latitude) *
                math.sin(next_latitude))
    return (math.degress(next_latitude), math.degrees(next_longitude))

def add_vertically(latitude, distance):
    return latitude + (distance * METER_PROPORTION_LATITUDE)
