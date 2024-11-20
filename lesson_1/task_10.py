#!/usr/bin/python3
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Sabina", "Hamida", "Xadica", "Sakina", "Sabrina"]

# add another list to the this list
friends.extend(lucky_numbers)
print(friends)

# add an item to the last index of list
friends.append("Sara")
print(friends)

# add a specific item to the specific index of list
friends.insert(1, "Mike")
print(friends)

# remove the specific item from the list
friends.remove("Mike")
print(friends)

# remove the last item from list
friends.pop()
print(friends)

print(friends.index("Sabina"))

friends = ["Sabina", "Hamida", "Sabina", "Xadica", "Sakina", "Sabrina"]
print(friends.count("Sabina"))

lucky_numbers = [42, 16, 15, 8, 23, 4]
# to sort from min to max
lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers = [4, 8, 15, 16, 23, 42]
# to reserve the items of list
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)