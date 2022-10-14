import random
people = []

for x in range(0, 5):
    person = input("type the name of the person: ")
    people.append(person)

name = random.randint(0, 5)

randomperson = people[name]
print("picking random person: ", randomperson)
