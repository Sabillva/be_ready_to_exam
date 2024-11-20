#!/usr/bin/python3

def sayhi():
    print("Hello User")

print("Top")
sayhi()
print("Bottom")

# with parameter
def say_hi(name):
    print("Hello " + name)

say_hi("Mike")
say_hi("Steve")

# with many parameters
def say_hi(name, age):
    print("Hello "+ name + ", you are " + age)
say_hi("Mike", "35")
say_hi("Steve", "70")