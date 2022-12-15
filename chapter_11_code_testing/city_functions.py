def full_city_info(city, country, population=''):
    """Create full info about the city."""
    if population:
        full_info = f"{city}, {country} - {population}"
    else:
        full_info = f"{city}, {country}" 
    return full_info.title()
