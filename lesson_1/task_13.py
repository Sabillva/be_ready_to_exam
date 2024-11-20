#!/usr/bin/python3
def cube(num):
    num*num*num
# if we want see the result, we should use print
cube(3)


def cube(num):
    num*num*num
# but there is no any back value from function to us to use it
print(cube(3))


def cube (num):
    return num*num*num

print(cube(3))

result = cube(4)
print(result)