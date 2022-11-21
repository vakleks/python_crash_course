#numbers from 1 to 20
for number in range(1,21):
    print(number)

#from 1 to 1000000
#for number in range(1, 1_000_000):
#    print(number)

#list
million = [number for number in range (1, 1_000_000)]
print(min(million))
print(max(million))
print(sum(million))

#even numbers from 1 to 20
for number in range(2,21, 2):
    print(number)
    
#devide into 3 from 1 to 30
for number in range(3,31,3):
    print(number)

#**3 from 1 to 10
cube = [value**3 for value in range(1,11)]
print(cube)
#or the same in more code
cubes = []
for value in range(1,11):
    cube = value ** 3
    cubes.append(cube)

print(cubes)