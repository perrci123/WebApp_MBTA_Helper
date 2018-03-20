import urllib.request   # urlencode function
import json


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):

    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """

    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

# url_testing = "https://maps.googleapis.com/maps/api/geocode/json?address=Prudential%20Tower"
#place = input('Enter a location:')
#new_name = place.replace(' ', '%20')
#url_testing = ("https://maps.googleapis.com/maps/api/geocode/json?address=" + new_name)



def get_lat_long(place_name):
    other = place_name.replace(' ', '%20')
    new_url = GMAPS_BASE_URL + '?address=' + other
    JSON = get_json(new_url)
    lat = JSON['results'][0]['geometry']['location']['lat']
    lng = JSON['results'][0]['geometry']['location']['lng']
    return lat, lng

#     # """
#     # Given a place name or address, return a (latitude, longitude) tuple
#     # with the coordinates of the given place.
#     # See https://developers.google.com/maps/documentation/geocoding/
#     # for Google Maps Geocode API URL formatting requirements.
#     # """
# place_testing = 'Boston College'
# print(get_lat_long(place_testing))
#
# lat = 0
# lng = 0


#
def get_nearest_station(lat, lng):

    url = MBTA_BASE_URL + '?api_key={}&lat={}&lon={}&format=json'.format(MBTA_DEMO_API_KEY, lat, lng)
    JSON = get_json(url)
    nearest_station = JSON['stop'][0]['stop_name']
    distance = JSON['stop'][0]['distance']
    return nearest_station, distance
#     """
#     Given latitude and longitude strings, return a (station_name, distance)
#     tuple for the nearest MBTA station to the given coordinates.
#     See http://realtime.mbta.com/Portal/Home/Documents for URL
#     formatting requirements for the 'stopsbylocation' API.
#     """
#     pass
#
# print(get_nearest_station(*get_lat_long('Boston College')))

def find_stop_near(place_name):
    lat, lng = get_lat_long(place_name)
    return get_nearest_station(lat, lng)

# print(find_stop_near("Boston College"))
#     """
#     Given a place name or address, return the nearest MBTA stop and the
#     distance from the given place to that stop.
#     """

