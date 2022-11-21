alien_0 = {'color': 'green', 'speed': 'slow'}
#error print
print(alien_0['points'])

#fix issue if points not exist
poin_value = alien_0.get('points', 'No point value assigned.')
print(poin_value)

