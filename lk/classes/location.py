from lk.classes.request import Request


class Location(object):

    def __init__(self, location):
        self._location = location

    @property
    def location(self):
        return self._location

    def to_geo_point(self):

        url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}'.format(lat=lat, lon=lon)
        response = Request().get(url)
        response_dict = response.dict

        pass

    def to_lat_lon(self):

        url = 'https://maps.googleapis.com/maps/api/geocode/json?address={location}'.format(location=self.location)

        response = Request().get(url)

        lat_lon_dict = response.odict['results'][0]['geometry']['location']

        lat = lat_lon_dict['lat']
        lon = lat_lon_dict['lng']

        return lat, lon


