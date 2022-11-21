def create_sandwich(*toppings):
    """Get the list of topping for sandwich."""
    print(f"\nMaking a sandwich with:")
    for topping in toppings:
        print(f" {topping}")

create_sandwich('chease')
create_sandwich('butter', 'beaf')
create_sandwich('butter', 'tomato', 'sausage')