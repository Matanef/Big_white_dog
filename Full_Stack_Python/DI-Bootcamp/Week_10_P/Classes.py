class User:
    def __init__(self,name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f"My name is {self.name}, nice to meet you"

    def has_birthday(self):
        self.age += 1

class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self,balance):
        self.balance = balance

    def greeting(self):
        return f"My name in {self.name}, nice to meet you, I have {self.balance} BTC !"


matan = User('Matan', 'efratimatan@gmai.com', 37)
camila = User('Camila', 'camilacamlia@gmail.com', 38)

print(matan.greeting())
camila.has_birthday()
print(camila.age)

dov = Customer('dov', 'dov@blahblah.com', '25')
dov.set_balance(2000)

print(dov.greeting())
