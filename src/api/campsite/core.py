from .helper import *
from .makerequest import get_request, post_request

def get_all_parks():
  parks = []
  response = get_request('/resourcelocation/rootmaps')
  for index, item in enumerate(response):
    park = {}
    park["map_id"] = item["mapId"]
    park["name"] = item["resourceLocationLocalizedValues"]["en-CA"]
    parks.append(park)
  return parks

def get_parks_status(from_date, to_date, park_name):
  # Get root mapId
  root_response = get_request('/resourcelocation/rootmaps')
  park_map_id = get_park_map_id(root_response, park_name)

  # Recursion - Start populating location_list arr recursively starting from map-of-ontario map_id
  return get_location_list([], park_map_id, from_date, to_date, "")

def get_location_list(location_list, map_id, from_date, to_date, parent):
  post_request_body = construct_post_request_body(map_id, from_date, to_date)
  response = post_request('/maps/mapdatabyid', post_request_body)
  print(response)
  parent = parent + "->" + response["map"]["localizedValues"][0]["title"] 
  
  # If map has sub-links, recursively call again
  if response["mapLinkAvailabilityMap"]:
    map_list = get_keys_from_dict(response["mapLinkAvailabilityMap"])
    for index, item in enumerate(map_list):
      get_location_list(location_list, item, from_date, to_date, parent)

  # If resources area available, get availability and push
  if response["resourceAvailabilityMap"]:
    map_list = get_keys_from_dict(response["resourceAvailabilityMap"])
    for index, item in enumerate(map_list):
      location = {}
      location["mapId"] = response["map"]["mapId"]
      location["resourceId"] = item
      location["parent"] = parent
      location["name"] = response["map"]["localizedValues"][0]["title"]
      location["site_availability"] = get_site_availability(response["resourceAvailabilityMap"], item)
      if len(location["site_availability"]) > 0:
        location["site_name"] = get_site_name(response["resourcesOnMap"], item)
        location["site_category"] = get_site_category(response["resourcesOnMap"], response["resourceCategoryMap"], item)
        location_list.append(location)   
  return location_list
