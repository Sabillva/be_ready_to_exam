#!/usr/bin/python3

for letter in "Sabina is a female":
    print(letter)

friends = ["Sabina", "Hamida", "Xadica", "Sakina", "Sabrina"]
for friend in friends:
    print(friend)

for index in range(10):
    print(index)
for index in range(3, 10):
    print(index)

friends = ["Sabina", "Hamida", "Xadica", "Sakina", "Sabrina"]
for index in range(len(friends)):
    print(friends[index])

for index in range(len(friends)):
    if index == 0:
        print("First friend")
    else:
        print("Not first friend")

print("-----------------")

friends = ["Sabina", "Hamida", "Xadica", "Sakina", "Sabrina"]
for index in friends:
    if index == "Sabina":
        print("First friend")
    else:
        print("Not first friend")