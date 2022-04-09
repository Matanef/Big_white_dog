my_text ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

firstChar = my_text[0]
print("The first character of the sentence is", firstChar)

my_textLength = len(my_text)
print("this is the amount of Characters in the sentence including spaces", my_textLength)

textNoSpace = my_text.replace(" ","")
textNoSpaceAmount = len(textNoSpace)
print("this is the amount of Characters in the sentence without spaces", textNoSpaceAmount)