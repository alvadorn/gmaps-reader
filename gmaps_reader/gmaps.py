#!/usr/bin/python

import requests
from gps.gps_system import GPS
from util.image import save_image, select_name

URL = 'https://maps.googleapis.com/maps/api/staticmap'


class GMaps:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.gps = GPS((kwargs.get('init_lat'), kwargs.get('init_lon')))

    def _params(self):
        return {
            'key': self.api,
            'maptype': 'satellite',
            'size': self.size,
            'zoom': self.zoom,
            'format': self.quality,
            'scale': self.scale
        }

    def get_map(self, gps):
        params = self._params()
        params['center'] = gps
        res = requests.get(URL, params=params)
        name = select_name()
        filename = self.path + "/" +  name + '.' + self.quality
        print("Writing: %s" % name)
        save_image(filename, res.content)
