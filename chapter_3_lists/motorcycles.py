motorcycles = ['honda', 'yamaha', 'suuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#add 'harley;
motorcycles.append('harley')
print(motorcycles)

#create 'cars' list and full it
cars = []

cars.append('ford')
cars.append('nissan')
cars.append('reno')
print(cars)

#insert 'opel' in first position in the list
cars.insert(0, 'opel')
print(cars)

#delete 'nissan' from list
del cars[2]
print(cars)

#pop one of motorcycles
popped_motrcycle = motorcycles.pop()
print(motorcycles)
print(popped_motrcycle)

#last owned motorcycle
motorcycles = ['honda', 'suzuki', 'yamaha']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

#pop by index
first_owned = motorcycles.pop(0)
print(f"The last motorcycle I owned was a {first_owned.title()}.")

#pop by value
motorcycles = ['honda', 'suzuki', 'yamaha']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)

#reason to pop
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is to expensive for me.")

print(motorcycles[1])