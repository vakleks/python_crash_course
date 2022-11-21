favourite_languges = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favourite_languges['sarah'].title()
print(f"Sarah's favorite language is {language}.")

favourite_languges['sarah']

for name, language in favourite_languges.items():
    print(f"{name.title()}'s fovorite language is {language.title()}.")

#output of keys
for name in favourite_languges.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in sorted(favourite_languges.keys()):
    print(name.title())

    if name  in friends:
        language = favourite_languges[name].title()
        print(f"\t{name.title()}, I see you like {language}!")

#output of sorted languages
print("\nThe following languages have been mentioned:")
for language in sorted(favourite_languges.values()):
    print(language.title())

#output of unique languages
print("\nThe unique languages have been mentioned:")
for language in set(favourite_languges.values()):
    print(language.title())