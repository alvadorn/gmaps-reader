import unittest

from ..coordinates import is_latitude_norther_than, is_longitude_wester_than

class TestIsLatitudeNortherThan(unittest.TestCase):
  def test_when_both_latitudes_are_negatives(self):
    lat_a = -10
    lat_b = -11

    result = is_latitude_norther_than(lat_a, lat_b)

    self.assertTrue(result)

  def test_when_both_latitudes_are_positive(self):
    lat_a = 10
    lat_b = 11

    result = is_latitude_norther_than(lat_a, lat_b)

    self.assertFalse(result)

  def test_when_lat_a_is_negative_and_b_is_positive(self):
    lat_a = -10
    lat_b = 11

    result = is_latitude_norther_than(lat_a, lat_b)

    self.assertFalse(result)

  def test_when_lat_a_is_positive_and_b_is_negative(self):
    lat_a = 10
    lat_b = -11

    result = is_latitude_norther_than(lat_a, lat_b)

    self.assertTrue(result)


class TestIsLongitudeWesterThan(unittest.TestCase):
  def test_when_both_longitudes_are_negatives(self):
    lat_a = -10
    lat_b = -11

    result = is_longitude_wester_than(lat_a, lat_b)

    self.assertTrue(result)

  def test_when_both_longitudes_are_positive(self):
    lat_a = 10
    lat_b = 11

    result = is_longitude_wester_than(lat_a, lat_b)

    self.assertTrue(result)

  def test_when_lon_a_is_negative_and_b_is_positive(self):
    lat_a = -10
    lat_b = 11

    result = is_longitude_wester_than(lat_a, lat_b)

    self.assertTrue(result)

  def test_when_lon_a_is_positive_and_b_is_negative(self):
    lat_a = 10
    lat_b = -11

    result = is_longitude_wester_than(lat_a, lat_b)

    self.assertFalse(result)