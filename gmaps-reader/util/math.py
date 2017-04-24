def decimal2degrees(decimal):
    integer = int(decimal)
    residue = (decimal - integer) * 60
    minutes = int(residue)
    seconds = int((residue - minutes) * 60)
    return (integer, minutes, seconds)

def degrees2decimal(degrees):
    integer, minutes, seconds = degrees
    value = integer + minutes/60 + seconds/3600
    return value
