import json, requests, coords
CITY1_NAME = raw_input("Choose destination city: ")
CITY2_NAME = raw_input("Choose your current city: ")

print coords.find_coords(CITY1_NAME)
