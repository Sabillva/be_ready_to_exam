#!/usr/bin/python3
text = "This is a short text for my tasks"
print(text.lower())
print(text.upper())
print(text.isupper())

print(text.upper().isupper())

print(len(text))

print(text[0])
print(text[3])
print(text[4])

print(text.index("T"))
print(text.index("i"))
print(text.index("shor"))

print(text.replace("short", "long"))