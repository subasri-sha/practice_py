# Nested Lists and Dictionaries in Python

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 2
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 3
    }

}
print(travel_log)
print(travel_log["France"])
print(travel_log["France"]["cities_visited"])
print(travel_log["Germany"]["total_visits"])
print(travel_log["Germany"]["cities_visited"][1])