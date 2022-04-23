# in sets every item isa unique one, meaning that if i have a duplicate item in set only one of those (and it will be the first one) will be itterated.
# for example:

my_set = {1,2,3,4,5,5}

# in the set above we have a duplicate item which means that later on when we will need to use this set only one of those "5" will be counted.
print(my_set)
# in the print above we can see that the set looks like this : {1, 2, 3, 4, 5}
# only one 5 was counted.

# now like all other data types we can add to the set, like this:
my_set.add(100)
print(my_set)

#  nothing special in the above we only added an item to the set.
#  however, in the next example we can see that when trying to add a nuber or an item that is already part of the set, the item will not be 
#  added since as we disscussed set can only contain unique items.

my_set.add(2)
print(my_set)

# let's return a collection that has on;ly unique items.
# now lets say that in our example we have an already built-up list.

my_list = [1,2,3,4,5,5]

# what we can do in this situation is wrap our list in a set. this will only return unique items:

print(set(my_list))
# {1, 2, 3, 4, 5}

# we can see that althought the list contains a duplicate item, once we wrp the list in a set we will only receive a single item.

# now lets copy the list and define in as a set again (with a different name)

my_second_set = {1,2,3,4,5,5}

# if we would like to access the set we won't be able to do so using indexes and we will receive an error that states:
# print(my_second_set[0])
# TypeError: 'set' object is not subscriptable

# meaning that set does not support indexing.
# set only allows us to check if an item is in the set and we can do that like this:

print(1 in my_second_set)
#  the output we rcrived is "True".

#  another nice example will be to print the length of my_second_set.
print(len(my_second_set))
# the output we recieved is "5" meaning that as we stated before a set will only contain unique items, although my_second_set
# contains 6 items which include a duplicated 5 we see that the output declares that the set contains 5 items and not 6 since 5 is duplicated.

# methods:













