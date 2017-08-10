import argparse
import gmaps
from util.image import COUNT
from concurrent.futures import ThreadPoolExecutor
import sys

N_THREADS = 20

counting = 0

parser = argparse.ArgumentParser(description="Get maps from GoogleMaps")
parser.add_argument("api", help="Api KEY from Google Maps Static")
parser.add_argument("--init_lat", type=float, default=0.0,
    help="Initial Latitude")
parser.add_argument("--init_lon", type=float, default=0.0,
        help="Initial longitude")
parser.add_argument("--max_lat", type=float, default=0.0,
    help="Max Latitude")
parser.add_argument("--max_lon", type=float, default=0.0,
    help="Max Longitude")
parser.add_argument("--distance", type=int, default=100,
    help="Distance between prints(default = 100m)")
parser.add_argument("--prints", type=int, default=25000,
    help="Max number of prints(default = 25000)")
parser.add_argument("--path", default="/tmp", help="Path to Save Image (Default = tmp)")
parser.add_argument("--quality", default='png', help="Image Quality (Default = png)")
parser.add_argument("--scale", default=1, type=int , help="Image Scale (Default = 1)")
parser.add_argument("--size", default='256x256', help="Image Size (Default = 256x256)")
parser.add_argument("--zoom", type=int, default=19,
    help="Image Zoom (default = 19)")
parser.add_argument("--prefix", default="default", help="Prefix name to save image (Default = default_*")
args = vars(parser.parse_args())

_gmaps = gmaps.GMaps(**args)

lat,lon = _gmaps.gps()
with ThreadPoolExecutor(max_workers=10) as executor:
    while lat > _gmaps.max_lat:
        while lon < _gmaps.max_lon:
            if counting >= _gmaps.prints:
                filename = _gmaps.path + '/last_gps.txt'
                with open(filename, 'w') as f:
                    f.write(str(_gmaps.gps))
                    f.write("COUNT: ")
                    f.write(COUNT)
                sys.exit(1)

            coord = str(_gmaps.gps)
            counting = counting + 1
            try:
                executor.submit(_gmaps.get_map, coord)
            except Exception:
                filename = _gmaps.path + '/last_gps.txt'
                with open(filename, 'w') as f:
                    f.write(str(_gmaps.gps))
                    f.write("COUNT: ")
                    f.write(COUNT)
                sys.exit(1)

            lon = _gmaps.gps.add_horizontally(_gmaps.distance)
        _gmaps.gps.add_vertically(_gmaps.distance)
        lat, lon = _gmaps.gps.initial_coordinates()
