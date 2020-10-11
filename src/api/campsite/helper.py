
def get_park_map_id(array, park_name):
  print(park_name)
  filter_map = filter(lambda item: item["resourceLocationLocalizedValues"]["en-CA"] == park_name, array) #Killarney Provincial Park, Map of Ontario
  return list(filter_map)[0]["mapId"]

def construct_post_request_body(map_id, from_date, to_date):
  post_body = {
    "mapId": map_id,
    "startDate": from_date + "T00:00:00.000Z",
    "endDate": to_date + "T00:00:00.000Z",
    "isReserving": True,
    "getDailyAvailability": True,
    "partySize": 2, #No. of persons         
    "filterData": "[]",
    "equipmentCategoryId": -32768, # campsite with tent
    "subEquipmentCategoryId": -32767, # sub category: campsite for 2 tents
    "boatLength": None,
    "boatDraft": None,
    "boatWidth": None,
    "resourceAccessPointId": None
  }
  return post_body

def get_keys_from_dict(dict):
  return list(dict.keys())

def get_site_name(resources_on_map, resource_id):
  filter_resource = filter(lambda item: str(item["resourceId"]) == resource_id, resources_on_map)
  filter_res = list(filter_resource)
  return filter_res[0]["localizedValues"][0]["name"] if len(filter_res) > 0 else []

def get_site_availability(resource_availability_map, resource_id):
  available = False
  availability_map = resource_availability_map[resource_id]
  for index, item in enumerate(availability_map):
    if not item["availability"] == 1:
      available = True
  return availability_map if available else []

def get_site_category(resources_on_map, resource_category_map, resource_id):
  filter_resource = filter(lambda item: str(item["resourceId"]) == resource_id, resources_on_map)
  filter_res = list(filter_resource)
  if len(filter_res) > 0:
    category_id = filter_res[0]["resourceCategoryId"]
    filter_category = resource_category_map[str(category_id)]
    return filter_category["localizedValues"][0]["name"]
  else:
    return ""
