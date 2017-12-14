import requests
#from pprint import pprint

MY_API_KEY = open("geocode_key.txt").read().strip()
CITY1_NAME = raw_input("Choose destination city: ")
CITY2_NAME = raw_input("Choose your current city: ")

def find_coords(cityName):
    CITY_NAME = cityName
    API_ENDPOINT = "https://maps.googleapis.com/maps/api/geocode/json?address="+CITY_NAME+"&key="+MY_API_KEY
    r = requests.get(API_ENDPOINT).json()
    coordinates = r["results"][0]["geometry"]["location"]
    result = {"city": cityName, "coordinates": coordinates}
    return result

find_coords(CITY1_NAME)
find_coords(CITY2_NAME)
