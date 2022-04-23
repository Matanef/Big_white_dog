# tuples cannot be changed, we create them but once created we cannot add, remove or modify them. imutable. a read only list.

some_tuple = (1,2,3,4,)
print(some_tuple)
print(type(some_tuple))

#  a tuple can be indexed meaning accessing the tuple using indexes [1], for example:
print(some_tuple[2])

# the proper way to write a tupple is as follows:
some_tuple1 = 1,2,3
print(some_tuple1)
print(type(some_tuple1))

# we can switch tuples value like this:

a = 1,2,3,4
b = "boba","toba","coba"
print(f'this is "a" now{a}')
print(f'this is type a {type(a)}')
print(f'this is type b {type(b)}')

a, b = b, a
print(f'and now this is "a"{a}')

# extracting values from tuples:
# i'll need variables in the amount of items in the tuple
t= 1,2
t1, t2 = t

print(f'this is "t1" {t1}')

# in this way we gave the value inside the tuple a varialbe

# Unpack the following tuple into 4 variables
a_tuple = (10, 20, 30, 40)
a_tuple1, a_tuple2, a_tuple3, a_tuple4 = a_tuple
print(f'this is the first value {a_tuple1}')
print(f'this is the second value {a_tuple2}')
print(f'this is the third value {a_tuple3}')
print(f'this is the forth value {a_tuple4}')