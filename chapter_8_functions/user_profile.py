def build_profile(first, last, **user_info):
    """Create a dictionary which contains all information about the user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('oleks', 'vak', location='praha', field='computer science', hobbie='cycling', music='metalcore')
print(user_profile)

