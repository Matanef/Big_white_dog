keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


# method 1
my_dict = {}
for key, value in zip(keys,values):
    my_dict.update({key:value})

# method 2 - dictionary comprehension
my_dict = {key:value for key, value in zip(keys,values) }
print(my_dict)

# method 3 - typecasting a list of tuples into a dictionary
print(dict(zip(keys,values)))