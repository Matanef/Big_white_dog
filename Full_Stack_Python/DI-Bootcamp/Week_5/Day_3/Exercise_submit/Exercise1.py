# Exercise 1 : Build-in functions

def printFunctions():
    ''' Returns the documentation of the functions abs(), int() and input()'''
    val = int(input('Choose 1 to print the document of abs(), Choose 1 to print the document of int(), Choose 1 to print the document of raw_input() : '))
    if val == 1:
        print('The abs() function {}'.format(abs.__doc__))
    elif val == 2:
        print('The int() function'.format(int.__doc__))
    elif val == 3:
        print(input.__doc__)



printFunctions()
print(printFunctions.__doc__)

# Exercise 2 : Currencies

class Currency():
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(obj):
        if obj.quantity >1:
            return str(obj.quantity) + ' '+obj.name +'s .'
        else:
            return str(obj.quantity) + ' '+obj.name

    def __int__(obj):
        return obj.quantity

    def __repr__(obj):
        if obj.quantity >1:
            return str(obj.quantity) + ' '+obj.name +'s .'
        else:
            return str(obj.quantity) + ' '+obj.name

    def __add__(self, other):
        if isinstance(other, int):
            val = self.quantity + other
        else:
            if self.name == other.name:
                val = self.quantity + other.quantity
            else:
                TypeError()

        return val

    def __iadd__(self, other):

        if isinstance(other, int):
            self.quantity = self.quantity + other
        else:
            self.quantity = self.quantity + other.quantity

        #val = self.quantity +other.quantity
        #self.quantity = val
        return self.quantity





c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c4 = Currency('shekel', 1)
c3 = Currency('shekel', 10)
print(str(c3))
print(int(c1))
print(repr(c2))
print(c1 + c2)
print(c1 + 5)

print(c1)

c1 += c2
print(c1)

print(c1 + c3)


