import argparse

parser = argparse.ArgumentParser(description="Get maps from GoogleMaps")
parser.add_argument("api", help="Api KEY from Google Maps Static")
parser.add_argument("--init_lat", type=float, default=0.0,
    help="Initial Latitude")
parser.add_argument("--init_long", type=float, default=0.0,
        help="Initial longitude")
parser.add_argument("--max_lat", type=float, default=0.0,
    help="Max Latitude")
parser.add_argument("--max_long", type=float, default=0.0,
    help="Max Longitude")
parser.add_argument("--distance", type=int, default=100,
    help="Distance between prints(default = 100m)")
parser.add_argument("--prints", type=int, default=25000,
    help="Max number of prints(default = 25000)")
parser.add_argument("path", default="~/", help="Path to Save Image (Default = Home)")
parser.add_argument("--quality", default='png', help="Image Quality (Default = png)")
parser.add_argument("--size", default='256x256', help="Image Size (Default = 256x256)")
parser.add_argument("--zoom", type=int, default=19,
    help="Image Zoom (default = 19)")
args = parser.parse_args()
print(args)
