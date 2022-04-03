import random
userString = input("Please Enter a string with percisely 10 letters: ")
print(len(userString))
first_char = userString[0]
last_char = userString[-1]



if len(userString) < 10:
    print("string not long enough.")
elif len(userString) > 10:
    print("string too long.")
else:
    print(first_char, last_char)

emptyString = ""
for x in userString:
    emptyString+=x
    print(emptyString)

jumble = "".join(random.sample(userString, len(userString)))
print(jumble)