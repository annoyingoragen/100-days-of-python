travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(name_of_country,number_of_visits,cities_visited):
    empty_dict={}
    empty_dict["country"]=name_of_country
    empty_dict["visits"]=number_of_visits
    empty_dict["cities"]=cities_visited
    travel_log.append(empty_dict)



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)