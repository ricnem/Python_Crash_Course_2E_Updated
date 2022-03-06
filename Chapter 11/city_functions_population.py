def city_country_population(city_name, city_country, population=None):
    if population:
        return f"{city_name.title()}, {city_country.title()} - population {population}"
    else:
        return f"{city_name.title()}, {city_country.title()}"