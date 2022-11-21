def about_car(brand, model, year, **car_info):
    """Create a dictionary which contains all information about the car."""
    car_info['car_brand'] = brand
    car_info['car_model'] = model
    car_info['car_year'] = year
    return car_info

car_specifications = about_car('subaru', 'outback', '2020', color='blue', transmission='automatiс')
print(car_specifications)
