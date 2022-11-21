def get_formated_name(first_name, last_name):
    """Return full formated aname"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q': 
        break

    formated_name = get_formated_name(f_name, l_name)
    print(f"\nHello, {formated_name}!")

