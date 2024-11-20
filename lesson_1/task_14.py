#!/usr/bin/python3
is_female = True
is_tall = False

if is_female:
    print("You are a female")
else:
    print("You are not a female")


if is_female or is_tall:
    print("You are a female or tall or both")
else:
    print("You neither female nor tall")


is_female = True
is_tall = False

if is_female and is_tall:
    print("You are a tall female")
else:
    print("You are either not female or not tall or both")


if is_female and is_tall:
    print("You are a tall female")
elif is_female and not(is_tall):
    print("You are a female but not tall")
elif not(is_female) and is_tall:
    print("You are tall but not a female")
else:
    print("You are not female and not tall")