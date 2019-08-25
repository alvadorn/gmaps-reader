def is_latitude_norther_than(lat_a, lat_b):
    """
      Check if lat_a is norther than lat_b
    """

    is_latitude_a_negative = lat_a < 0
    is_latitude_b_negative = lat_b < 0

    same_sign = is_latitude_a_negative == is_latitude_b_negative

    if not is_latitude_a_negative and is_latitude_b_negative:
        return True

    if is_latitude_a_negative and not is_latitude_b_negative:
        return False

    if same_sign:
        return lat_a > lat_b

    return lat_a < lat_b


def is_longitude_wester_than(lon_a, lon_b):
    """
      Check if lon_a is wester than lon_b
    """

    is_longitude_a_negative = lon_a < 0
    is_longitude_b_negative = lon_b < 0

    both_negative = is_longitude_a_negative and is_longitude_b_negative
    both_positive = not is_longitude_a_negative and not is_longitude_b_negative

    if both_negative:
      return lon_a > lon_b
    
    if (is_longitude_a_negative and not is_longitude_b_negative) or both_positive:
      return lon_a < lon_b

    return False

    # if is_longitude_a_negative and is_longitude_b_negative:
    #     return False
    


    # if 

    # if is_longitude_a_negative and is_longitude_b_negative:
    #     return lon_a > lon_b

    return lon_a < lon_b
