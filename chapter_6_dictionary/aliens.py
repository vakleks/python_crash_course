#create dictionaries
alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'red', 'points': '15'}

#add dictionaries in list
aliens = [alien_0, alien_1, alien_2]

#output info about every alien
for alien in aliens:
    print(alien)

#create empty lsit for alins save
aliens = []

#create 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#show firs 5 aliens
print("\nThe first five aliens: ")
for alien in aliens[:5]:
    print(alien)

#show total created aliens amount
print(f"\nTotal number of aliens: {len(aliens)}")

#change first three aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#show firts three aliens
print("Updated first three aliens are:")
for aliens in aliens[:3]:
    print(alien)

