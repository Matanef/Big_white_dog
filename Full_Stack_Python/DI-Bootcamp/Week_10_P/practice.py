s = "hello i'm happy"

print(s.capitalize())

print(s.upper())

print(s.swapcase())

print(s.lower())

print(len(s))
print(s.replace('happy', 'cool'))

# count number of "h" in the string
sub = "h"
print(s.count(sub))

# return true if the string starts with the provided string inside the function
print(s.startswith('hello'))

# return true if the string ends with the provided string inside the function
print(s.endswith('d'))

# split the string into list
print(s.split())

# will provide the location of the string inside the s string
print(s.find("i'm"))

# check if the provided variable contains both numerics and string
print(s.isalnum())

# check if the provided variable contains onyl alphabetics
print(s.isalpha())

# if the provided variable contains only numerics
print(s.isnumeric())


