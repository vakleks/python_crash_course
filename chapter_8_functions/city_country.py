def get_city_country(city, country):
    """Return info abot city and country"""
    full_info = f"{city}, {country}"
    return full_info.title()

while True:
    print("\nEnter city and county! ")
    print("(or press 'q' to quit)")

    city_name = input("The city is: ")
    if city_name == 'q':
        break

    country_name = input("The country is: ")
    if country_name == 'q':
        break

    formated_info = get_city_country(city_name, country_name)
    print(f"\n{formated_info.title()}")


