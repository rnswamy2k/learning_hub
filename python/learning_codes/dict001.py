
result = []

def travel_log(country, cities, no_of_times):
    
    data = {}
    data["country"] = country
    data["cities"] = cities.split(',')
    data["no_of_times"] = no_of_times

    result.append(data)


travel_log('india','bangalore,mysore',10)
travel_log('mexico','cancun',1)

print(result)