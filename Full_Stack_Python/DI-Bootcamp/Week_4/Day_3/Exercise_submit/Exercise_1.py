keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


my_dict = {}
for key, value in zip(keys,values):
    my_dict.update({key:value})

my_dict = {key:value for key, value in zip(keys,values) }
print(my_dict)

print(dict(zip(keys,values)))