alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#change alien color
alien_0['color'] = 'yellow'
print("Now alien is yellow")
print(alien_0)

#add speed of alien
alien_0['speed'] = 'medium'
print(alien_0)

#move alien
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #fast alien
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New alien position: {alien_0['x_position']}")

#delete points
del alien_0['points']
print(alien_0)
